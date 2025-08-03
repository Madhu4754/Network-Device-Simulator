#!/bin/bash
echo "Starting Device Simulator Server..."
gnome-terminal -- bash -c "python3 server/device_server.py; exec bash"

sleep 2

echo "Launching Client..."
gnome-terminal -- bash -c "python3 client/device_client.py; exec bash"
