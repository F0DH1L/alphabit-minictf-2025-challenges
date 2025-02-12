                         
import numpy as np
from egcd import egcd  # pip install egcd

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/ "


letter_to_index = {char: idx for idx, char in enumerate(alphabet)}
index_to_letter = {idx: char for idx, char in enumerate(alphabet)}

def matrix_mod_inv(matrix, modulus):
    """We find the matrix modulus inverse by
    Step 1) Find determinant
    Step 2) Find determinant value in a specific modulus (usually length of alphabet)
    Step 3) Take that det_inv times the det*inverted matrix (this will then be the adjoint) in mod 26
    """
    det = int(np.round(np.linalg.det(matrix)))  # Step 1
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2
    if det == 0 or np.gcd(det, modulus) != 1:
        return None

    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3
    return matrix_modulus_inv

def encrypt(message, K):
    encrypted = ""
    message_in_numbers = [letter_to_index[letter] for letter in message]

    split_P = [
        message_in_numbers[i : i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0]))
    ]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]

        numbers = np.dot(K, P) % len(alphabet)

        for idx in range(numbers.shape[0]):
            encrypted += index_to_letter[int(numbers[idx, 0])]

    return encrypted

def decrypt(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = [letter_to_index[letter] for letter in cipher]

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]
    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabet)

        for idx in range(numbers.shape[0]):
            decrypted += index_to_letter[int(numbers[idx, 0])]

    return decrypted

encrypted_message = "XM03IH)1{0$KC3@B>C *2<._1(;W"
# encrypted_message = "XM"

# for i in range(26):
#     for j in range(26):
#         for k in range(26):
#             for l in range(26):
#                 K = np.matrix([[i, j], [k, l]])
                
#                 Kinv = matrix_mod_inv(K, 65)
#                 if Kinv is not None:
#                     print(K)
#                     Kinv = np.array(Kinv)  # Ensure Kinv is a NumPy array
#                     decrypted_message = decrypt(encrypted_message, Kinv)
#                     if 'ALPHABIT' in decrypted_message:
#                         print(f"Key: {K}")
#                         print(f"Decrypted message: {decrypted_message}")
                        # exit()
         
print(len(alphabet))                                                        
K = np.matrix([[ 11, 8], [ 3, 7]])
Kinv = matrix_mod_inv(K, 65)
decrypted_message = decrypt(encrypted_message, Kinv)

print(decrypted_message)