import socket
import numpy as np

weights = np.array([
    65, 108, 112, 104, 97, 98, 105, 116, 123, 67, 104, 49, 116, 52, 110, 52, 95, 33, 53, 95, 72, 51, 114, 51, 125
])

# Define bias (arbitrary constant)
bias = 77

def predict(inputs):
    return int(np.dot(inputs, weights) + bias)

def handle_client(conn):
    conn.sendall(b"Welcome to the Linear Model Challenge !\n")
    conn.sendall(b"Enter inputs to get the prediction (25 inputs). ex: 12 34 54 65 67 89 34 12 45 67 45 22 34 56 78 45 23 76 85 23 86 24 19 23 54 \n")
    
    while True:
        data = conn.recv(1024).strip()
        if not data:
            break
        
        try:
            # Parse input into an array of integers
            inputs = list(map(int, data.decode().split()))
            if len(inputs) != len(weights):
                conn.sendall(b"Invalid input length ! Try again.\n")
                continue
            
            # Get prediction
            result = predict(np.array(inputs))
            conn.sendall(f"Prediction: {result} $\n".encode())

        except Exception as e:
            conn.sendall(b"Error processing input.\n")

    conn.close()

def start_server(host='0.0.0.0', port=1337):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen()
        print(f"[*] Listening on {host}:{port}")
        while True:
            conn, addr = server.accept()
            print(f"[+] Connection from {addr}")
            handle_client(conn)

if __name__ == "__main__":
    start_server()
