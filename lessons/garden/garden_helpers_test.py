"""Test my garden functions."""

__author__ = "730387535"


from lessons.garden.garden_helpers import add_by_kind

def test_add_empty_plantby() -> None:
    """Ensures add by kind does not add an empty string to the dictionary."""
    by_kind = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    new_plant_kind = "vegetable"
    new_plant = "peas"
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert add_by_kind(by_kind, "vegetable", "peas") == {"flower": ["marigold", "zinnia"], "vegetable": ["carrots", "peas"]}
