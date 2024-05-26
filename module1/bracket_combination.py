def BracketCombinations(num):
    """
    Calculates the number of valid combinations of n pairs of parentheses.

    Args:
        num (int): The number of pairs of parentheses.

    Returns:
        int: The number of valid combinations.
    """
    if num == 0:
        return 1

    total = 0
    for i in range(num):
        total += BracketCombinations(i) * BracketCombinations(num - i - 1)

    return total
print(BracketCombinations(3))