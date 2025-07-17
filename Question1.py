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
