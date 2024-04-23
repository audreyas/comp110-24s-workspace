"""Functions that implement sorting algorithms."""

__author__ = "730387535"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    for i in range(1, len(x)):
        temp = x[i]
        j = i - 1
        while j >= 0 and temp < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = temp
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    i = 0
    while i < len(x):
        min_i = i
        j = i + 1
        while j < len(x):
            if x[j] < x[min_i]:
                min_i = j
            j += 1
        if min_i != i:
            temp = x[min_i]
            x[min_i] = x[i]
            x[i] = temp
        i += 1
    return None
    