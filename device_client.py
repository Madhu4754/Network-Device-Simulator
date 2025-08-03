import socket
from utils.logger import log

IP = "127.0.0.1"
PORT = 8080

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))
    log(f"Connected to device at {IP}:{PORT}")

    while True:
        msg = input("Send Command: ")
        if msg.lower() == "exit":
            break
        client.send(msg.encode())
        response = client.recv(1024).decode()
        log(f"Response: {response}")
    client.close()

if __name__ == "__main__":
    main()
