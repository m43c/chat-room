# Python Chat Room with Sockets

This project implements a chat room in Python using sockets. The application
consists of a server (`server.py`) and a client (`client.py`) that communicate
over a network connection. The server handles multiple clients simultaneously
using threads.

## Features

- Allows multiple users to connect to the server and communicate in real-time.
- Messages sent by one client are distributed to all other connected clients.

## Requirements

- Python 3.x installed on the system.
- Connection to a local network or the internet for communication between the
  server and clients.

## Setup

1. Clone this repository:
    ```bash
    clone https://github.com/m43c/chat-room.git
    ```
2. Navigate to the project directory:
    ```bash
    cd chat-room/
    ```
3. Open two terminals (one for the server and one for the client).
4. Run the server:
    ```bash
    python server.py
    ```
5. Run the client:
    ```bash
    python client.py
    ```

## Usage

- Once the client is running, you can type a message into the text entry and
  press the "Send" button to send it to the server and other connected clients.

## Notes

- Ensure the server is running before executing the client.
- The IP address and port of the server are configured in the `server.py`
  and `client.py` files. Adjust these values according to your network setup if
  necessary.

## Contributions

Contributions are welcome. If you find any issues or have any improvements, feel
free to open an issue or send a pull request.