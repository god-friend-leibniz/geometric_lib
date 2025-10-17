import math

def area(side: float) -> float:
    '''
    Given the side of a square, calculates area
    '''
    return math.pow(side, 2)


def perimeter(side: float) -> float:
    '''
    Given the side of a square, calculates perimeter
    '''
    return 4 * side
