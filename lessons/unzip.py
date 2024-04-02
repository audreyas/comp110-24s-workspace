"""Splitting a dictionary into two lists."""

__author__ = "730387535"


def get_keys(dict_input: dict[str, int]) -> list[str]:
    """Produce a list of all the keys in the input dictionary."""
    user_list = []
    for key in dict_input: 
        user_list.append(key)
    return user_list


def get_values(dict_input2: dict[str, int]) -> list[int]:
    """Produce a list of all the values in the input dictionary."""
    user_list = []
    for key in dict_input2: 
        user_list.append(dict_input2[key])
    return user_list