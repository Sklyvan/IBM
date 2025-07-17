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
    """
    Given an array of integers, this function calculates the maximum sum of two non-overlapping subarrays.
    The first subarray must end before the second subarray starts, and both subarrays must be non-empty.
    The function uses a two-pass approach to count unique elements in the left and right parts of the array.
    The maximum sum is calculated by combining the counts of unique elements from both parts.
    :param arr: list[int]: The input array of integers.
    :return: int: The maximum sum of unique elements from two non-overlapping subarrays.
    """
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
def getMinimumCost(visibilityScore):
    n, m = len(visibilityScore), len(visibilityScore[0])
    total_cost = 0

    for j in range(m):  # iterate columns
        for i in range(1, n):  # rows from second to last
            prev = visibilityScore[i - 1][j]
            curr = visibilityScore[i][j]
            if curr <= prev:
                required = prev + 1
                total_cost += required - curr
                visibilityScore[i][j] = required

    return total_cost
```
