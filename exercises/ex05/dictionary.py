"""EX05 - Dictionary Utility Functions."""

__author__ = "730387535"


def invert(user_input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    keys = list(user_input.keys())
    values = list(user_input.values())
    inverted_dict = {}
    for i in range(len(keys)):
        if values[i] in inverted_dict:
            raise KeyError("Duplicate value found when inverting the dictionary.")
        inverted_dict[values[i]] = keys[i]
        
    return inverted_dict


def favorite_color(user_colors: dict[str, str]) -> str:
    """Return highest frequency color."""
    values = list(user_colors.values())
    counter = 0
    color = values[0]
    for i in values:
        curr_frequency = values.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            color = i
    return color


def count(values: list[str]) -> dict[str, int]:
    """Count the occurances of a given value."""
    counter: dict[str, int] = {}
    for element in values:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1
    return counter


def alphabetizer(user_words: list[str]) -> dict[str, list[str]]:
    """Sort words by first letter."""
    sorted_words: dict[str, list[str]] = {}
    for element in user_words:
        first_letter = element[0].lower()
        if first_letter not in sorted_words:
            sorted_words[first_letter] = []
            sorted_words[first_letter].append(element)
        else:
            sorted_words[first_letter].append(element)
    return sorted_words


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the attendance sheet for students."""
    if day in attendance_log and student not in attendance_log[day]:
        attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]