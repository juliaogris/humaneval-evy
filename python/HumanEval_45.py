#START:PROMPT


def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """

#END:PROMPT
#START:SOLUTION
    return a * h / 2.0

#END:SOLUTION
#START:TEST


METADATA = {}


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0


#END:TEST
#START:CHECK
check(triangle_area)
#END:CHECK