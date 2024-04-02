"""EX04 - List Utility Functions."""

__author__ = "730387535"


def all(a: list[int], given: int) -> bool: 
    """Indicates whether or not all the ints in the list are the same as the given int."""
    if len(a) == 0:
        return False
    while a:
        elem = a.pop()
        if elem != given:
            return False
    return True 


def max(input: list[int]) -> int: 
    """Return the largest in the list."""
    if len(input) == 0: 
        raise ValueError("max () arg is an empty List") 
    max_number = input.pop(0)
    while input:
        next_number = input.pop()
        if next_number > max_number:
            max_number = next_number 
    return max_number


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Check if every element at every index is equal in both lists."""
    if len(list_one) != len(list_two):
        return False 
    while list_one: 
        element_one = list_one.pop()
        element_two = list_two.pop()
        if element_one != element_two:
            return False 
    return True


def extend(a: list[int], b: list[int]) -> None: 
    """Mutate the first list by appending the second list to the end of it."""
    while len(b) > 0:
        a.append(b.pop(0))