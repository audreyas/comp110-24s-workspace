"""CQ08: Intro To Object Oriented Programming."""

from __future__ import annotations 

__author__ = "730387535"


class Point: 
    """Class that has an x and a y attribute that acts as a representation of a point on a coordinate graph."""
    # attributes
    x: float 
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor that assigns inital values for the attributes x and y."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None: 
        """Updates the x and y attribute so that x = x * factor and y = y * factor."""
        self.x *= factor 
        self.y *= factor
    
    def scale(self, factor: int) -> Point: 
        """Return a new Point with x and y attributes equal to self.x * factor and self.y * factor."""
        return (self.x * factor, self.y * factor)
