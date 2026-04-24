# CN-jackfruit-problem-
Multi-client online quiz system with real-time ranking
Multi-Client Quiz System (Python Socket Programming)

A real-time multi-client quiz application built using Python sockets and multithreading. The system allows multiple users to connect to a server, answer quiz questions within a time limit, and view a live leaderboard.

Overview

This project demonstrates:

Client-server communication using TCP sockets
Handling multiple clients using multithreading
Real-time quiz interaction with time-bound responses
Dynamic leaderboard updates
Features
Multiple clients can join simultaneously
Time-limited questions
Live leaderboard after each question
Final standings at the end of the quiz
JSON-based message communication
Tech Stack
Language: Python
Concepts Used:
Socket Programming
Multithreading
JSON Communication
Queue-based message handling
Project Structure
.
├── server.py   # Quiz server (handles logic, scoring, clients)
├── client.py   # Client program (user interaction)
└── README.md   # Project documentation
Installation and Setup
Clone the repository:
git clone <your-repo-link>
cd <repo-folder>
Run the server:
python server.py
Run the client (in multiple terminals):
python client.py
Usage
Start the server
Run one or more clients
Enter your nickname
Answer questions (A/B/C/D) within the given time
View leaderboard updates after each question
Check final results at the end
How It Works
Server (server.py)
Listens for incoming client connections
Stores client details such as name, score, and response times
Sends quiz questions sequentially
Collects answers within a time limit
Evaluates responses and updates scores
Broadcasts leaderboard after each question
Client (client.py)
Connects to the server
Sends user nickname
Receives and displays questions
Sends answers to the server
Displays leaderboard and final results
Sample Flow
Client joins → Server starts quiz → Question sent → 
Client answers → Server evaluates → 
Leaderboard updated → Next question → 
Final results displayed
Future Improvements
Add graphical user interface (GUI)
Store questions in a database
Support multiple quiz categories
Add user authentication
Improve response time tracking
Contributors
Your Name
License

This project is intended for academic and learning purposes.

Notes
The server must be started before clients connect
Default host: 127.0.0.1
Default port: 5000
These values can be modified in the code if required
