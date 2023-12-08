import time as tm
import socket as sk
import tkinter as tk
import threading as th


class Socket:
    def __init__(self):
        self.host = "192.168.1.10"
        self.port = 7500
        self.client_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

    def setsockopt(self):
        self.client_socket.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)

    def connect(self):
        self.client_socket.connect((self.host, self.port))


class Client(tk.Tk, Socket):
    def __init__(self):
        tk.Tk.__init__(self)
        Socket.__init__(self)
        self.title(f"Connected to: {self.host}:{str(self.port)}")
        self.resizable(False, False)

        self.chat_text = tk.Text(self, width=50, state="disabled")
        self.chat_text.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(self)
        self.message_entry.pack(
            side="left",
            ipady=4,
            padx=(10, 10),
            pady=(0, 10),
            fill="x",
            expand=True,
        )

        self.send_btn = tk.Button(self, text="Send", command=self.send_message)
        self.send_btn.pack(side="right", padx=(0, 10), pady=(0, 10))

        self.setsockopt()
        self.connect()
        self.run_thread()

    def send_message(self):
        client_message = self.message_entry.get()
        self.client_socket.send(client_message.encode("utf-8"))

        self.chat_text.config(state="normal")
        self.chat_text.tag_config("right", justify="right")
        self.chat_text.insert(tk.END, client_message + "\n", "right")
        self.chat_text.config(state="disabled")

        self.reset_entry()

    def receive_message(self):
        while True:
            server_message = self.client_socket.recv(1024).decode("utf-8")

            self.chat_text.config(state="normal")
            self.chat_text.insert(tk.END, server_message + "\n")
            self.chat_text.config(state="disabled")

    def run_thread(self):
        recv_thread = th.Thread(target=self.receive_message, daemon=True)
        recv_thread.start()

    def reset_entry(self):
        tm.sleep(1)
        self.message_entry.delete(0, tk.END)


if __name__ == "__main__":
    client = Client()
    client.mainloop()
