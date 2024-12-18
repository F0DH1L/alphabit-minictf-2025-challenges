# The Affine Cipher Mystery

## Description:

You've intercepted a secret message encrypted using an Affine Cipher. Your mission is to decipher the text and retrieve the hidden flag.

Affine Cipher is an encryption technique defined by the formula:

$$ y = (a \cdot x + b) \mod m $$

Where:

- $ a $: Multiplier (coprime with $ m $)
- $ b $: Offset
- $ m $: Modular base (in this case, ASCII range, $ m = 128 $)
- $ x $: ASCII value of the plaintext character

### Given:

1. **Ciphertext**: A sequence of encrypted ASCII values saved in `challenge_ciphertext.txt`.
2. **Hints**:
   - The encryption parameters $ b = 7 $, and $ m = 128 $.
   - $ a $ is coprime with $ m $, ensuring the cipher is reversible.

## Objective:

Decrypt the ciphertext using the formula:

$$ x = a^{-1} \cdot (y - b) \mod m $$

- $ a^{-1} $ is $a$ inverse

Retrieve the plaintext and extract the flag in the format: `Alphabit{...}`.

## Deliverables:

Submit the decrypted flag as proof of completion.

Good luck, cryptographer!
