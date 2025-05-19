🎮 Word Guessing Game (Client-Server with GUI)
A simple Word Guessing Game built using Python, Tkinter GUI, and Sockets. This project includes two parts:

A server that manages and sends words.

A client GUI where players guess the word, letter by letter.

🧠 How It Works
Server Side:
Accepts a list of CAPITALIZED words from the user.

Randomly chooses one of the words.

Sends the selected word to each connecting client.

Handles multiple clients using threads.

Client Side:
Connects to the server.

Displays a GUI with:

Hidden word (as underscores).

Letter buttons (A-Z) for guessing.

Message label and remaining guesses.

Allows 5 incorrect guesses before ending the game.

Gives feedback on correct/incorrect guesses.

📁 Project Structure
bash
Copy
Edit
word_guessing_game/
├── client.py      # Word guessing game GUI client
├── server.py      # Server GUI that selects and sends words
└── README.md
🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/word-guessing-game.git
cd word-guessing-game
2. Run the Server
bash
Copy
Edit
python server.py
Enter one or more capitalized words, separated by spaces.

Click Start.

3. Run the Client (on the same or different machine)
bash
Copy
Edit
python client.py
The client will connect to the server.

Use the letter buttons to guess the word.

🖥️ Requirements
Python 3.x

Tkinter (comes built-in with most Python installations)

⚙️ Customization
To change server IP or port, modify these lines in both files:

python
Copy
Edit
HOST = '127.0.0.1'
PORT = 7000
📝 Notes
The game only accepts uppercase words.

The client disables all buttons after winning or running out of guesses.

The server handles multiple clients concurrently.



