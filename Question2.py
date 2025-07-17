def getMinimumCost(visibilityScore: list[list[int]]) -> int:
    """
    Given a 2D list of visibility scores, this function calculates the minimum cost to ensure that each element in the
    second row is greater than the element directly above it in the first row. The cost is defined as the difference
    needed to increase the visibility score of an element in the second row to be greater than the element above it.
    The function iterates through each column and adjusts the visibility scores as necessary, accumulating the total cost.
    :param visibilityScore: list[list[int]]: A 2D list where each element represents the visibility score of a cell.
    :return: int: The total cost to adjust the visibility scores.
    """
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
