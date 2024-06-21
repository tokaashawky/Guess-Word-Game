import socket
import tkinter as tk

class WordGuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Guessing Game")

        self.label = tk.Label(master, text="Guess the word:", bg="lightgrey", fg="black")
        self.label.pack()

        self.entry = tk.Entry(master, state='disabled', width=20, font=('Helvetica', 14), bg="Teal")
        self.entry.pack()

        self.remaining_guesses_label = tk.Label(master, text="Guesses left: 5", bg="lightgrey", fg="black")
        self.remaining_guesses_label.pack()

        self.message_label = tk.Label(master, text="", bg="Teal", fg="black")
        self.message_label.pack()

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()

        # Define button layout
        button_layout = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y'],
            ['Z']
        ]
        self.buttons = []
        # Create buttons
        for row in button_layout:
            button_row = []
            for char in row:
                button = tk.Button(self.buttons_frame, text=char, command=lambda c=char: self.guess_char(c),
                                   bg="lightgrey", fg="black", width=4, height=2, font=('Helvetica', 12, 'bold'))
                button.grid(row=button_layout.index(row), column=row.index(char), padx=2, pady=2)
                button_row.append(button)
            self.buttons.append(button_row)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST = '127.0.0.1'  # Change to the actual server IP address
        self.PORT = 7000  # Change to the actual server port
        self.connect_to_server()

        self.num_guesses = 0

    def connect_to_server(self):
        try:
            self.client.connect((self.HOST, self.PORT))
            self.word_to_guess = self.client.recv(1024).decode()
            self.word_length = len(self.word_to_guess)
            underscore_spaces = ' ' * (self.word_length - 1)
            self.entry.config(state='normal')
            self.entry.delete(0, tk.END)
            self.entry.insert(0, '_{} '.format(underscore_spaces) * self.word_length)
            self.entry.config(state='disabled')
        except ConnectionRefusedError:
            self.message_label.config(text="Failed to connect to the server. Server may not be running.")
            print("Failed to connect to the server. Server may not be running.")
            self.disable_buttons()
        except Exception as e:
            self.message_label.config(text="Error: " + str(e))
            print("Error:", e)
            self.disable_buttons()

    def guess_char(self, char):
        if self.num_guesses >= 5:
            return

        guessed_word = ''
        correct_guess = False
        for c in self.word_to_guess:
            if c == char:
                guessed_word += c
                correct_guess = True
            elif c in self.entry.get():
                guessed_word += c
            else:
                guessed_word += '_'

        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.insert(0, guessed_word)
        self.entry.config(state='disabled')
        if correct_guess:
            if guessed_word == self.word_to_guess:
                self.message_label.config(text="Congratulations! You guessed the word correctly.")
                self.disable_buttons()
            else:
                self.message_label.config(text="Correct guess!")
        else:
            self.num_guesses += 1
            remaining_guesses = 5 - self.num_guesses
            self.remaining_guesses_label.config(
                text=f"Guesses left: {remaining_guesses}")
            if self.num_guesses >= 5:
                self.message_label.config(text="You failed to guess the word.")
                self.disable_buttons()
            else:
                self.message_label.config(text="Incorrect guess.")

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')
def main():
    root = tk.Tk()
    game_gui = WordGuessingGameGUI(root)
    root.configure(bg="Teal")  # Set background color of the root window
    root.mainloop()
if __name__ == "__main__":
    main()
