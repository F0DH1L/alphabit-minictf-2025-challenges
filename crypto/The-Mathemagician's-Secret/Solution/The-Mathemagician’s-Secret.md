# Write-Up: The Mathemagician’s Secret

**Author** : [Senahadji M Said](https://github.com/SenhadjiMSaid)

## Challenge Overview

In this challenge, we were given a set of linear equations that represent an encrypted flag. Our goal was to reverse the transformation, solve for the original numbers, and reconstruct the flag.

However, the values $a$, $b$, $c$, and $d$ used in the equations were not explicitly provided—they were hidden in a mysterious format:

```plaintext
| _ _ _ | , _ _ | _ _ , _ _ _ | | , | _ | | |
```

By deciphering this clue and solving the system of equations, we could recover the flag.

---

## Step 1: Extracting a, b, c, d

The first step was to decode the hidden values.

- The clue `| _ _ _ | , _ _ | _ _ , _ _ _ | | , | _ | | |` represents a pattern that maps to numeric values.
- From hints , we deduced:
  $$ a = 17, b = 4, c = 3 \ \text{and} \ d = 23
- the idea was simple:
  1. `|` is `1` and `_` is `0`
  2. the pattern is a binary number, so we convert it to decimal to get the values of a, b, c and d

Now, we had the transformation matrix:

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix} =
\begin{pmatrix}
17 & 4 \\
3 & 23
\end{pmatrix}
$$

## Step 2: Understanding the Equations

The challenge provided pairs of equations in the form:

$$
17x + 4y \equiv c_1 \mod{2^{64}} \\
3x + 23y \equiv c_2 \mod{2^{64}} \\
$$

Each pair represents one part of the flag, which was previously **split into 4-character chunks before encryption.**

Thus, solving for $(x, y)$ in each equation would reveal the **original 4-character chunks of the flag.**

## Step 3: Solving the System of Equations

For each pair of values $(c_1, c_2)$, we had to **solve for $x$ and $y$** using modular arithmetic.

1. Compute the determinant of the transformation matrix:
   $$ \text{det} = (a \cdot d - b \cdot c ) \mod{2^{64}} $$
2. Find the modular inverse of the determinant to invert the matrix:
3. Compute the inverse matrix $\mod{2^{64}}$:

   $$
   \begin{bmatrix}
    d & -b \\
    -c & a
   \end{bmatrix} \cdot det^{-1} \mod{2^{64}}
   $$

4. Multiply the inverse matrix by $(c_1, c_2)$ to solve for $(x, y)$
5. Convert the values back to characters using `long_to_bytes()`

## Solution Script

Here’s the Python script to decrypt the flag:

```python
from Crypto.Util.number import long_to_bytes

mod = 2**64

equations = [
    (17, 4, 25194994872, 3, 23, 40871185060),
    (17, 4, 42005481930, 3, 23, 45332464339),
    (17, 4, 36745152809, 3, 23, 50026341125),
    (17, 4, 39708733006, 3, 23, 44924205391),
    (17, 4, 39971525569, 3, 23, 47987695993),
    (17, 4, 39599077192, 3, 23, 42691308655),
    (17, 4, 39291744519, 3, 23, 50474244351),
    (17, 4, 467789, 3, 23, 82551),
]

flag = ""

for eq in equations:
    a, b, c1, c, d, c2 = eq

    det = (a * d - b * c) % mod
    det_inv = pow(det, -1, mod)

    x = (d * c1 - b * c2) * det_inv % mod
    y = (-c * c1 + a * c2) * det_inv % mod

    flag_part1 = long_to_bytes(x).decode("utf-8", errors="ignore")
    flag_part2 = long_to_bytes(y).decode("utf-8", errors="ignore")
    flag += flag_part1 + flag_part2

print(f"flag: {flag}")

```

## Final Flag

```plaintext
Alphabit{linear_equations_are_more_important_then_u_think}
```

## Lessons Learned

- Modular arithmetic is essential in cryptography.
- Linear transformations can obscure text but are reversible with math.
- Recognizing patterns in encoded values helps break cryptosystems.
- Breaking ciphers requires both cryptographic and mathematical thinking.
