"""
General geometry-related functions

Syntax:

area = circle_area(diameter)
area = rectangle_area(length, width)
area = square_area(side)
"""
import math   # load math.py

PI = math.pi

def circle_area(diameter):
    """
    Compute the area of a circle from a given diameter

    :param diameter: Diameter of circle
    :return: Area of circle
    """
    radius = diameter / 2
    return PI * (radius ** 2)

def rectangle_area(length, width):
    """
    Compute the area of a rectangle.

    :param length:  length of longer side
    :param width:   length of shorter side
    :return: Area of rectangle
    """
    return length * width

def square_area(side):
    """
    Compute area of a square.

    :param side: Length of one side
    :return: Area of square
    """
    return side ** 2

print(f"{__name__ = }")


if __name__ == "__main__":  # if this file is run directly, not imported
    # only run if called as a script:
    AREA1 = square_area(15)
    print(f"area1: {AREA1}")

    AREA2 = circle_area(22)
    print(f"area2: {AREA2}")

    AREA3 = rectangle_area(9, 13)
    print(f"area3: {AREA3}")
