import socket as sk
import threading as th


class Server:
    def __init__(self):
        self.host = "192.168.1.10"
        self.port = 7500
        self.server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.clients = set()

    def setsockopt(self):
        self.server_socket.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)

    def bind(self):
        self.server_socket.bind((self.host, self.port))

    def listen(self):
        self.server_socket.listen()

    def accept(self):
        print("Waiting for connection...")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(
                f"Connection established with: {client_address[0]}:"
                f"{client_address[1]}"
            )

            self.clients.add(client_socket)
            self.run_thread(client_socket, client_address)

    def process_request(self, client_socket, client_address):
        while True:
            message = client_socket.recv(1024).decode("utf-8")

            if message:
                print(
                    f"{client_address[0]}:{str(client_address[1])} says:"
                    f"{message}"
                )

                for client in self.clients:
                    if client is not client_socket:
                        # client.send(bytes(message, "utf-8"))
                        client.send(message.encode("utf-8"))
            else:
                self.clients.remove(client_socket)
                print(
                    f"{client_address[0]}:{str(client_address[1])} "
                    f"disconnected"
                )
                break
        client_socket.close()

    def run_thread(self, client_socket, client_address):
        client_thread = th.Thread(
            target=self.process_request, args=(client_socket, client_address)
        )
        client_thread.start()


if __name__ == "__main__":
    server = Server()
    server.setsockopt()
    server.bind()
    server.listen()
    server.accept()
