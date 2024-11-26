# 0x08. Making Change

## Algorithm | Python

### Objective

This project tackles the classic coin change problem, a cornerstone of dynamic programming and greedy algorithms. The goal is to determine the **minimum number of coins** required to achieve a specific total using a given set of coin denominations.

This project challenges your ability to:

- Apply algorithmic thinking.
- Optimize for efficiency and correctness.
- Understand the trade-offs between different algorithmic strategies.

---

## Concepts Needed

### 1. Greedy Algorithms

- **Understanding**:
  - How greedy algorithms make locally optimal choices to build a global solution.
  - When greedy approaches might fail to provide the optimal solution.
- **Example**: Determining if a greedy approach works with your coin denominations.

### 2. Dynamic Programming (DP)

- **Principles**:
  - Using DP to solve optimization problems by breaking them into sub-problems.
  - Recognizing overlapping subproblems and optimal substructure.
- **Example**: Building a DP table for minimum coins to make change for each amount.

### 3. Algorithmic Complexity

- Analyzing and improving **time** and **space complexity**.
- Balancing between readability and performance.

### 4. Problem-Solving Strategies

- Breaking the problem into manageable steps.
- Exploring iterative vs recursive approaches.

### 5. Python Programming

- List manipulations, comprehensions, and conditional logic.
- Writing efficient and readable functions.

---

## Resources

### Documentation

- [Python Official Documentation](https://docs.python.org/3/tutorial/controlflow.html): Control flow tools (`for`, `if`, etc.).

### Tutorials

- **GeeksforGeeks**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm for Minimum Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube**:
  - Dynamic Programming - Coin Change Problem (Step-by-step explanation).

---

## Requirements

### General

- **Editors**: `vi`, `vim`, `emacs`.
- **Environment**: Ubuntu 20.04 LTS, Python 3.4.3.
- **Code Style**: PEP 8 (version 1.7.x).
- Files should:
  - End with a new line.
  - Begin with `#!/usr/bin/python3`.
  - Be executable.
- A `README.md` file is mandatory at the root of the project.

---

## Tasks

### 0. Change comes from within

**Mandatory**  

Write a function `makeChange(coins, total)` that determines the **fewest number of coins** needed to meet a given `total`.  

Happy Coding! 🚀
