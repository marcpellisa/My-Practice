def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a+b<=c or b+c<=a or a+c<=b:
        return False
    if a==0 or b==0 or c==0:
        return False
    if a == b == c:
        return True
    return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a+b<=c or b+c<=a or a+c<=b:
        return False
    if a==0 or b==0 or c==0:
        return False
    if len(set(sides))<=2:
        return True
    return False

def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a+b<=c or b+c<=a or a+c<=b:
        return False
    if a==0 or b==0 or c==0:
        return False
    if a!=b and b!=c and a!=c:
        return True
    return False