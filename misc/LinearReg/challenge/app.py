#!/usr/bin/env python3

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
    print(b"Welcome to the Linear Model Challenge !")
    print(b"Enter inputs to get the prediction (25 inputs). ex: 12 34 54 65 67 89 34 12 45 67 45 22 34 56 78 45 23 76 85 23 86 24 19 23 54 ")
    
    while True:
        data = conn.recv(1024).strip()
        if not data:
            break
        
        try:
            # Parse input into an array of integers
            inputs = list(map(int, data.decode().split()))
            if len(inputs) != len(weights):
                print(b"Invalid input length ! Try again.")
                continue
            
            # Get prediction
            result = predict(np.array(inputs))
            print(f"Prediction: {result} $".encode())

        except Exception as e:
            print(b"Error processing input.")

