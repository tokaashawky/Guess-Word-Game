import socket
import tkinter as tk
import tkinter.messagebox as messagebox
import random
import threading
#Medium Aquamarine- Light Steel Blue-Cadet Blue
class ServerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess Word Game")
        self.master.geometry("280x100")
        self.master.configure(bg="Teal")  # Set background color of the window

        self.label_font = ('Helvetica', 10,"bold")
        self.button_font = ('Helvetica', 10)

        self.label = tk.Label(master, text="Hello to Guess Word Game ^_^  ", bg="lightgray", fg="black",
                              font=self.label_font)
        self.label.pack()

        self.label = tk.Label(master, text="Enter words (separated by space '  ' )", bg="white", fg="black")
        self.label.pack()

        self.words_entry = tk.Entry(master, width=35, bg="white", fg="black", font=self.label_font)
        self.words_entry.pack(side=tk.TOP)

        self.start_button = tk.Button(master, text="Start", command=self.start_server,activebackground="Slate Gray",
                                      activeforeground="black", bg="lightgray", fg="black", font=self.button_font)
        self.start_button.pack()

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST = '127.0.0.1'
        self.PORT = 7000
        self.client_threads = []  # List to store client threads
    def start_server(self):
        words = self.words_entry.get().split(' ')
        if not words[0]:  # Check if no words are entered
            messagebox.showerror("Error", "You Must Enter At Least One Capital Word  ^_^  ")
            return

        # Check if all words are capitalized
        if not all(word.strip().isupper() for word in words):
            messagebox.showerror("Error", "Enter Capital Words Only  :)    ")
            return

        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen(5)

        while True:
            client_socket, _ = self.server_socket.accept()
            # Create a new thread to handle the client
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, words))
            client_thread.start()
            self.client_threads.append(client_thread)

    def handle_client(self, client_socket, words):
        chosen_word = random.choice(words).strip('  ')
        print("Chosen word:", chosen_word)
        client_socket.sendall(chosen_word.encode())
        client_socket.close()

def main():
    root = tk.Tk()
    server_gui = ServerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
