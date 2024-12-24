# Algebraic Hill Cipher

**Author**: [Senhadji M Said](https://github.com/SenhadjiMSaid)

## Description

Your task is to decrypt a message encrypted using the Hill cipher with a 2x2 key matrix. You are given:

1. The ciphertext: `XM03IH)1{0$KC3@B>C *2<._1(;W`.
2. The flag is in the format `Alphabit{...}`.

The Hill cipher encryption is defined as:

$$ C = K \times P \pmod{m} $$

Where:

- $K$ is The encryption matrix:
  $$
  K = \begin{bmatrix}
  11 & 8 \\
  3 & 7
  \end{bmatrix}
  $$

## Files

- `ciphertext.txt`

## Hints

1. FFF

### Character Set

The encryption uses an extended character set:
`ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`

Use this python function to get mapping of the characters:

```python
def create_mapping():
    char_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/ "
    char_to_num = {char: idx for idx, char in enumerate(char_set)}
    num_to_char = {idx: char for idx, char in enumerate(char_set)}
    return char_to_num, num_to_char
```

Good luck!
