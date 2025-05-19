# 🎮 Word Guessing Game (Client-Server with GUI)

A simple **Word Guessing Game** built using **Python**, **Tkinter GUI**, and **Sockets**.

This project includes two parts:
- A **server** that manages and sends words.
- A **client** where the player guesses the word using a graphical interface.

---

## 🧠 How It Works

### Server
- User inputs a list of **capitalized words** (e.g., `APPLE BANANA ORANGE`).
- Randomly selects one word and sends it to each connecting client.
- Uses multithreading to handle multiple clients.

### Client
- Connects to the server and receives a hidden word.
- GUI displays:
  - The word with underscores.
  - A-Z buttons to guess letters.
  - Remaining guesses (max 5).
  - Messages for correct or incorrect guesses.

---

## 📁 Files
word_guessing_game/
├── client.py # GUI for the player
├── server.py # GUI server that sends words
└── README.md # This file
