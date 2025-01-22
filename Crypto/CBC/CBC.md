# Breaking CBC Encryption

## Description:

This ciphertext was encrypted using AES in CBC mode. However, it contains a weakness: identical plaintext blocks have led to identical ciphertext blocks.

Your goal:

1. Analyze the provided ciphertext and exploit the weakness in CBC mode.
2. Recover the plaintext.
3. Extract the flag from the plaintext in the format `Alphabit{...}`.

---

## Provided

- **Ciphertext**: Hex-encoded ciphertext.
- **IV**: Initialization vector.
- **Block Size**: 16 bytes.

## Objective

- Submit the flag hidden in the plaintext as proof of your decryption skills.

Good luck!
