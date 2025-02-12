from Crypto.Util.number import bytes_to_long

flag = "Alphabit{linear_equations_are_more_important_then_u_think}"
chunk_size = 4  # Split flag into 4-character chunks

# Split flag into chunks
chunks = [flag[i : i + chunk_size] for i in range(0, len(flag), chunk_size)]

# Encode each chunk as a number
numbers = [bytes_to_long(chunk.encode()) for chunk in chunks]

# Use a large modulus (e.g., 2^64)
mod = 2**64

# Generate equations for each pair of chunks
equations = []
for i in range(0, len(numbers), 2):
    x = numbers[i]
    y = (
        numbers[i + 1] if i + 1 < len(numbers) else 0
    )  # Pad with 0 if odd number of chunks

    # Coefficients for the equations
    a, b = 17, 4
    c, d = 3, 23

    c1 = (a * x + b * y) % mod
    c2 = (c * x + d * y) % mod

    equations.append((a, b, c1, c, d, c2))

# Print the equations

for i, eq in enumerate(equations):
    a, b, c1, c, d, c2 = eq
    print(f"Equation {i+1}:")
    print(f"{a}x + {b}y ≡ {c1} (mod {mod})")
    print(f"{c}x + {d}y ≡ {c2} (mod {mod})")
    print()

with open("spellbook.txt", "w") as f:
    i = 0
    for eq in equations:
        i += 1
        a, b, c1, c, d, c2 = eq
        f.write(f"Ciphertext {i} : {c1}\n")
        i += 1
        f.write(f"Ciphertext {i} : {c2}\n")
