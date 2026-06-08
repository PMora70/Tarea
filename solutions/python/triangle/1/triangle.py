def equilateral(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b < c or a + c < b or b + c < a:
        return False

    if a == b == c:
        return True
    else: 
        return False

    

def isosceles(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b < c or a + c < b or b + c < a:
        return False

    if a == b or b == c or c == a:
        return True
    else:
        return False
    


def scalene(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b < c or a + c < b or b + c < a:
        return False

    if a != b and b != c and a != c:
        return True
    else:
        return False
