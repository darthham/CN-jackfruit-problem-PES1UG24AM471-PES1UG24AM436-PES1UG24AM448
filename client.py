import socket
import threading
import json
import time
import sys

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000


def send_json(sock, obj):
    data = json.dumps(obj).encode("utf-8") + b"\n"
    sock.sendall(data)


def receiver_loop(sock):
    buf = b""
    while True:
        try:
            data = sock.recv(4096)
            if not data:
                print("[INFO] Disconnected from server.")
                break
            buf += data
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                line = line.strip()
                if not line:
                    continue
                try:
                    msg = json.loads(line.decode("utf-8"))
                    handle_server_msg(sock, msg)
                except json.JSONDecodeError:
                    continue
        except OSError:
            break


def handle_server_msg(sock, msg):
    t = msg.get("type")
    if t == "info":
        print(f"[INFO] {msg.get('msg')}")
    elif t == "question":
        qid = msg["qid"]
        print("\n" + "=" * 40)
        print(f"Question {qid} (time limit: {msg['time_limit']}s):")
        print(msg["text"])
        for opt in msg["options"]:
            print(opt)
        print("Enter your choice (A/B/C/D) and press Enter:")

        # Take input in the main thread for simplicity.
        # Server enforces time limit; late answers are discarded.
        def get_answer():
            choice = sys.stdin.readline().strip().upper()
            if choice not in {"A", "B", "C", "D"}:
                print("[WARN] Invalid choice, ignoring.")
                return
            send_json(
                sock,
                {
                    "type": "answer",
                    "qid": qid,
                    "choice": choice,
                    "client_send_ts": time.time(),
                },
            )

        threading.Thread(target=get_answer, daemon=True).start()

    elif t == "leaderboard":
        print("\n--- Leaderboard after question", msg["qid"], "---")
        for entry in msg["entries"]:
            print(f"{entry['name']}: {entry['score']}")
    elif t == "quiz_end":
        print("\n=== FINAL STANDINGS ===")
        for entry in msg["entries"]:
            print(f"{entry['name']}: {entry['score']}")
        print("Quiz finished. Press Ctrl+C to exit.")
    else:
        print("[DEBUG] Unknown message from server:", msg)


def main():
    name = input("Enter your nickname: ").strip() or "Player"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_HOST, SERVER_PORT))
    print(f"[INFO] Connected to {SERVER_HOST}:{SERVER_PORT}")

    # Send join message
    send_json(sock, {"type": "join", "name": name})

    threading.Thread(target=receiver_loop, args=(sock,), daemon=True).start()

    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Exiting...")
    finally:
        sock.close()


if __name__ == "__main__":
    main()
