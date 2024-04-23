"""Writing A Recursive Function."""

__author__ = "730387535"


def f(n: int, k: int) -> int:
    """Recrusive function that finds the product of two integers."""
    if n == 0:  # base case
        return 0
    else:  # recursive rule
        return k + f(k, n - 1)