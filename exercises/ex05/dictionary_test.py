"""EX06 - Testing Dictionary Utility Functions."""

__author__ = "730387535"

import pytest
from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

def test_invert_use_case() -> None: 
    """Test basic use case for the invert function."""
    t: dict[str, str] = {'orange': 'dog', 'yellow': 'fish', 'purple': 'hamster'}
    #ret_value: dict[str, str] = invert(t)
    invert(t)
    assert t == {'dog': 'orange', 'fish': 'yellow', 'hamster': 'purple'}


def test_invert_use_case_error() -> None: 
    """Test basic use case for the invert function."""
    t: dict[str, str] = {'a': 'z'}
    #inverted_dict = invert(t)
    invert(t)
    assert t == {'z': 'a'}


def test_invert_edge_case_empty() -> None:
    """Test basic edge case for an empty dictionary for the invert function."""
    t: dict[str, str] = {}
    #inverted_dict = invert(t)
    invert(t)
    assert t == {}


def test_favorite_color_use_case() -> None:
    """Test basic use case for the favorite color function."""
    t: dict[str, str] = {"Audrey": "purple", "Sarah": "purple", "Jessica": "red"}
    most_frequent_color = favorite_color(t)
    assert most_frequent_color == "purple"


def test_favorite_color_use_case_tie() -> None:
    """Test basic use case for the favorite color function when there is a tie."""
    t: dict[str, str] = {"Audrey": "purple", "Sarah": "purple", "Jessica": "red", "Erin": "red"}
    most_frequent_color = favorite_color(t)
    assert most_frequent_color == "purple"


def test_favorite_color_edge_case() -> None:
    """Test edge case for the favorite color function."""
    t: dict[str, str] = {}
    most_frequent_color = favorite_color(t)
    assert most_frequent_color == ""


def test_count_use_case() -> None: 
    """Test basic use case for the count function."""
    t: list[str] = ["cat", "dog", "cat"]
    result = count(t)
    assert result == {'cat': 2, 'dog': 1}


def test_count_use_case_empty() -> None: 
    """Test use case for empty count function."""
    t: list[str] = []
    result = count(t)
    assert result == {}


def test_count_edge_case() -> None:
    """Test edge use for count function."""
    t: list[str] = [1, 2, 3, 1, 2, 1, 1]
    result = count(t)
    assert result == {'1': 4, '2': 2, '3': 1}


def test_alphabatizer_use_case() -> None:
    """Test basic use case for the alphabetizer function."""
    t: list[str] = ['ant', 'bee', 'cat', 'duck']
    result = alphabetizer(t)
    alphabetizer(t)
    assert result == {'a': ['ant'], 'b': ['bee'], 'c': ['cat'], 'd': ['duck']}


def test_alphabatizer_use_case_empty() -> None:
    """Test use case for the alphabetizer function with empty list."""
    t: list[str] = []
    result = alphabetizer(t)
    assert result == {}


def test_alphabatizer_edge_case() -> None: 
    """Test edge case for the alphabetizer function with special character inputs."""
    t: list[str] = (['!ant', '$bee', '12dog'])
    result = alphabetizer(t)
    assert result == {'!': ['!ant'], '$': ['$bee'], '1': ['12dog']}


def test_update_attendance_use_case() -> None: 
    """Test basic use case for the update attendance function."""
    t: dict[str, list[str]] = {"Monday": ["Audrey", "Sarah"]}
    day = "Monday"
    student = "Rebecca"
    update_attendance(t, day, student) 
    assert t == {'Monday': ['Audrey', 'Sarah', 'Rebecca']}


def test_update_attendance_use_case_empty() -> None: 
    """Test edge case for the update attendance function with an empty attendance log."""
    t: dict[str, list[str]] = {}
    day = 'Thursday'
    student = 'Audrey'
    update_attendance(t, day, student)
    assert t == {'Thursday': ['Audrey']}


def test_update_attendance_edge_case() -> None: 
    """Test use case for eht update attendance function."""
    t: dict[str, list[str]] = {"Monday": ["Audrey", "Sarah"]}
    day = "Monday"
    student = ["Amber", "Emma", "Zack"]
    update_attendance(t, day, student) 
    assert t == {'Monday': ['Audrey', 'Sarah', 'Amber', 'Emma', 'Zack']}