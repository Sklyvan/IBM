# IBM Software Engineer Challenge

This repository contains solutions to two algorithmic problems presented in a IBM Software Engineer Challenge.

---

## 📌 Question 1: Maximum Distinct Sum After Split

### 🧩 Problem Statement

Given an array `arr` of size `n`, split it at index `i` into two **non-empty subarrays**:

- Left: `arr[0..i-1]`
- Right: `arr[i..n-1]`

The goal is to **maximize the sum** of the number of **distinct elements** in each subarray.

Return the **maximum possible sum** of distinct counts among all valid splits.

### 🧠 Strategy

- Iterate from left to right to compute the number of distinct elements up to each index.
- Then, from right to left to do the same in reverse.
- At each valid split point `i`, compute `left[i-1] + right[i]`.
- Keep track of the **maximum** sum found.

### ✅ Python Solution

```python
def getMaxSum(arr: list[int]) -> int:
    n = len(arr)
    leftCounter, rightCounter = [0] * n, [0] * n

    seen = set()
    for i in range(n):
        seen.add(arr[i])
        leftCounter[i] = len(seen)

    seen = set()
    for i in reversed(range(n)):
        seen.add(arr[i])
        rightCounter[i] = len(seen)

    return max(leftCounter[i - 1] + rightCounter[i] for i in range(1, n))
```
---

## 📌 Question 2: Minimum Cost to Adjust Grid Visibility

### 🧩 Problem Statement

You are given a 2D grid `visibilityScore[n][m]`.
Each value represents the visibility of an element in a column-based layout.
You must **increase values (at a cost of 1 per unit)** such that:

> For every column, all elements **below** a given row must have a **strictly higher** visibility score than the one above.

Return the **minimum total cost** to make the grid satisfy this rule.

### 🧠 Strategy

* Iterate **column by column** (not row-wise).
* For each cell from top to bottom:

  * If the current value is not strictly greater than the one above it, increment it to the required value (`above + 1`).
  * Track the total cost based on how much was increased.

### ✅ Python Solution

```python
def getMinimumCost(visibilityScore: list[list[int]]) -> int:
    n, m = len(visibilityScore), len(visibilityScore[0])
    totalCost = 0

    for j in range(m):
        for i in range(1, n):
            prev, curr = visibilityScore[i - 1][j], visibilityScore[i][j]
            if curr <= prev:
                required = prev + 1
                totalCost += required - curr
                visibilityScore[i][j] = required

    return totalCost
```
