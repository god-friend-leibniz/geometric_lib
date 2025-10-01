import math

def area(radius: float) -> float:
    '''
    Given the radius of a circle, calculates area
    '''
    return math.pi * math.pow(radius, 2)


def perimeter(radius: float) -> float:
    '''
    Given the radius of a circle, calculates perimeter
    '''
    return 2 * math.pi * radius

