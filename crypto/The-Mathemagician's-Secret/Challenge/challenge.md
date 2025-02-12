# 📜 The Mathemagician's Secret

**Author**: [Senahadji M Said](https://github.com/SenhadjiMSaid)
**Category:** Cryptography  
**Difficulty:** Medium-Hard

## 🔹 Introduction

Welcome, young apprentice! You have stumbled upon an ancient **spellbook** filled with **mysterious numbers**.

Legends say that the **Mathemagician** himself encoded a **hidden message** within these numbers using the magic of **linear equations** and **modular arithmetic**.

Your task is to **reverse the spell** and uncover the true message.

## 🔢 The Challenge

Inside `spellbook.txt`, you will find **a list of encrypted numbers**.

The Mathemagician used a **linear transformation** to disguise the original text:

$$
ax + by ≡ c1 \pmod{2^{64}} \\
cx + dy ≡ c2 \pmod{2^{64}}
$$

But beware! The values of $a, b, c, d$ are **unknown**.  
Can you **discover the hidden equations** and solve for $x$ and $y$?

## 📂 Provided Files

📜 [spellbook.txt](https://drive.google.com/file/d/1JD7rnMc2i7nXBUte01umI7T8D4wLQtQm/view?usp=drive_link) → Contains the **ciphertext**.

## 💡 Hints

1️⃣ The Mathemagician has left behind a hidden clue in the ancient scrolls… but it’s not so obvious. Instead of directly revealing a, b, c, and d, he encoded them in a mysterious pattern: [hint.txt](Challenge\hint.txt.txt)
2️⃣ Before encryption, the flag was split into 4-character chunks and then transformed using a linear system of equations.

## 🚀 Goal

Your objective is to **decrypt the hidden message** and recover the flag.

Submit your answer in this format: `Alphabit{mathemagical_solution}`

_Good luck._
