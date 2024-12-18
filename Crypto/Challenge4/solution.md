# Solution for Participants

## Steps

### 1. Understand CBC Mode

- CBC encrypts each plaintext block $P_i$ as :
  $$C_i= E_k(P_i \oplus C_{i-1})$$
  For the first block:
  $$C_0= E_k(P_0 \oplus IV)$$
- Identical plaintext blocks result in identical ciphertext blocks.

### 2. Analyze Ciphertext

- Identify identical ciphertext blocks.
- Use the IV and decryption process to deduce plaintext blocks.

### Retrieve the Flag

- Recover the plaintext and extract the flag directly:

  ```text
    Flag : Alphabit{U_understand_CBC}
  ```
