"""EX06 - Testing Dictionary Utility Functions."""

__author__ = "730387535"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_use_case() -> None: 
    """Test basic use case for the invert function."""
    t: dict[str, str] = {'orange': 'dog', 'yellow': 'fish', 'purple': 'hamster'}
    ret_value: str = invert(t)
    assert ret_value == {'dog': 'orange', 'fish': 'yellow', 'hamster': 'purple'}


def test_invert_use_case_error() -> None: 
    """Test basic use case for the invert function."""
    t: dict[str, str] = {'a': 'z'}
    result = invert(t)
    assert result == {'z': 'a'}


def test_invert_edge_case_empty() -> None:
    """Test basic edge case for an empty dictionary for the invert function."""
    t: dict[str, str] = {}
    result = invert(t)
    assert result == {}


def test_favroite_color_use_case() -> None: 
    """Test basic use case for favorite color function."""
    a: dict[str, str] = {'Mark': 'yellow', 'Audrey': 'yellow'}
    assert favorite_color(a) == 'yellow'


def test_favorite_color_seconduse_case() -> None:
    """Test use case for favorite color function."""
    a: dict[str, str] = {'Mark': 'yellow', 'Audrey': 'yellow', 'Emma': 'blue', 'Erik': 'blue'}
    assert favorite_color(a) == 'yellow'


def test_favorite_color_edge_case() -> None: 
    """Test basic edge case for empty dictionary for favorite color function."""
    a: dict[str, str] = {}
    assert favorite_color(a) is None


def test_count_use_case() -> None: 
    """Test basic use case for the count function."""
    assert count(["cat", "dog", "cat"]) == {"cat": 2, "dog": 1}


def test_count_use_case_empty() -> None: 
    """Test use case for empty count function."""
    assert count([]) == {}


def test_count_edge_case() -> None:
    """Test edge use for count function."""
    assert count([1, 2, 3, 1, 2, 1, 1]) == {1: 4, 2: 2, 3: 1}


def test_alphabatizer_use_case() -> None:
    """Test basic use case for the alphabetizer function."""
    assert alphabetizer(['ant', 'bee', 'cat', 'duck']) == {'a': ['ant'], 'b': ['bee'], 'c': ['cat'], 'd': ['duck']}


def test_alphabatizer_use_case_empty() -> None:
    """Test use case for the alphabetizer function with empty list."""
    assert alphabetizer([]) == {}


def test_alphabatizer_edge_case() -> None: 
    """Test edge case for the alphabetizer function with special character inputs."""
    assert alphabetizer(['!ant', '$bee', '12dog']) == {'!': ['!ant'], '$': ['$bee'], '1': ['12dog']}


def test_update_attendance_use_case() -> None: 
    """Test basic use case for the update attendance function."""
    t: dict[str, list[str]] = {"Monday": ["Audrey", "Sarah"]}
    update_attendance(t, "Monday", "Rebecca") 
    assert t == {'Monday': ['Audrey', 'Sarah', 'Rebecca']}


def test_update_attendance_use_case_empty() -> None: 
    """Test edge case for the update attendance function with an empty attendance log."""
    t: dict[str, list[str]] = {}
    update_attendance(t, 'Thursday', 'Audrey')
    assert t == {'Thursday': ['Audrey']}


def test_update_attendance_edge_case() -> None: 
    """Test use case for eht update attendance function."""
    t: dict[str, list[str]] = {"Monday": ["Audrey", "Sarah"]}
    day = "Monday"
    update_attendance(t, day, "Amber") 
    update_attendance(t, day, "Emma") 
    assert t == {'Monday': ['Audrey', 'Sarah', 'Amber', 'Emma']}