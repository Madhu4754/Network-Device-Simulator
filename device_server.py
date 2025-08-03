import socket
import json
import threading
from utils.logger import log

CONFIG_PATH = 'config/device_config.json'

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def handle_client(client_socket, address):
    log(f"Connection from {address}")
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            log(f"Received: {data}")
            client_socket.send(f"ACK: {data}".encode())
        except:
            break
    client_socket.close()

def main():
    config = load_config()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((config["ip_address"], config["port"]))
    server.listen(5)
    log(f"Device {config['device_id']} ({config['device_type']}) listening on {config['ip_address']}:{config['port']}")

    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

if __name__ == "__main__":
    main()
