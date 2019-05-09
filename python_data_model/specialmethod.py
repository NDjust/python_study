from math import hypot

class Vector:
    '''
    by using special method express euclidean vector 
    '''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
        

if __name__ == "__main__":
    v1 = Vector(2, 3)
    v2 = Vector(3, 5)
    print(v1) # Vector(2, 3)
    print(v1+v2) # Vector(5, 8)
    print(v1 * 3) # Vector(6, 9)
    print(abs(v2)) # 5.83095....
    print(bool(v1)) # True
    