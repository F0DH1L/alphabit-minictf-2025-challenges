# Find the Function

**Author**: [Senhadji M Said](https://github.com/SenhadjiMSaid)

## Description

We want to encrypted a secret flag using a mathematical function $ f $. But we have forgot the function 
Can you help us find the function $f(x)$ and encrypt my message?

- Wen kow the format of the function $f$:
  
$$ f(x) = (ax^3 + bx^2 + cx + d) \  \text{mod} \ 256 $$

  So you need to find a, b, c and d

- We represent the alphabet as folow:

| A   | B   | c   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   | O   | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  | 26  |

**you need to:**

1. Deduce $f(x)$ usingthe provided plain-ciphertext pairs
2. Encrypt the message `ESI` using the function $f(x)$

- Plaintext-Ciphertext pairs for analysis:

```makefile
Plaintext: ALPHA
Ciphertext: [9, 157, 37, 21, 9]
```

- message to encrypt is `ESI`

## flags:

the flag is in format :
`Alphabit{E1_E2_E3}`
where `E1`, `E2` and `E3` are the encryption of `S`, `B` and `A`
Good luck!
