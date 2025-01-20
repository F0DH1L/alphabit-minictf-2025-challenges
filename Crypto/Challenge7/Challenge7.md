# ECC Shared Secret

**Author**: [Senhadji M Said](https://github.com/SenhadjiMSaid)

## Description

Alice and Bob are exchanging secret messages using elliptic curve cryptography (ECC). You have intercepted their public keys and, surprisingly, Bob's private key. Using this information, your task is to compute their shared secret and decrypt the flag.

Elliptic Curve Diffie-Hellman (ECDH) is a cryptographic protocol used to securely compute a shared secret over an insecure channel. It leverages the mathematical properties of elliptic curves, ensuring strong security with smaller key sizes compared to other cryptosystems like RSA.

### Key Concepts:

1. **Elliptic Curve Equation**:

   - $ y^2 = x^3 + ax + b \mod p $, where $ a $, $ b $, and $ p $ define the curve.
   - Points on the curve form a group with well-defined addition and scalar multiplication operations.

2. **ECDH Process**:
   - Each party generates a private key ($d_A, d_B$) and computes a public key ($P_A = d_A \cdot G, P_B = d_B \cdot G$).
   - Both parties exchange public keys and compute the shared secret:
     $$
          S = d_A \cdot P_B = d_B \cdot P_A
     $$
   - The shared secret $ S $ is the same for both parties.

### Your Task:

Use the provided public keys, Bob's private key, and the encrypted flag to recover the original flag.

## Hints:

1. **Shared Secret Formula**: The shared secret is computed as:
   $$
   S = \text{Bob's Private Key} \cdot \text{Alice's Public Key}
   $$
2. The elliptic curve used in this challenge is **brainpoolP256r1**.
3. You can use Python libraries like `tinyec` to perform elliptic curve operations.

## Resources

- [Elliptic Curve Cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography)
- [Elliptic Curve Diffie-Hellman (ECDH)](https://cryptobook.nakov.com/asymmetric-key-ciphers/ecdh-key-exchange)
- [Python tinyec Library Documentation](https://pypi.org/project/tinyec/)

## File Provided:

- **challenge.txt**: Contains:
  - Alice's public key.
  - Bob's public key.
  - Bob's private key.
  - Encrypted flag.

## Goal:

Submit the decrypted flag in the format: `Alphabit{...}`.
