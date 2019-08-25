import math

input_point_1_A = int(input('Input for point A parameter 1: '))
input_point_2_A = int(input('Input for point A parameter 2: '))
input_point_3_A = int(input('Input for point A parameter 3: '))

input_point_1_B = int(input('Input for point B parameter 1: '))
input_point_2_B = int(input('Input for point B parameter 2: '))
input_point_3_B = int(input('Input for point B parameter 3: '))

input_point_1_C = int(input('Input for point B parameter 1: '))
input_point_2_C = int(input('Input for point B parameter 2: '))
input_point_3_C = int(input('Input for point B parameter 3: '))


class Vector:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return '[%.2f, %.2f, %.2f]' % (self.x, self.y, self.z)

    def __add__(self, vec):
        "suma: self + vec"
        return Vector(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __iadd__(self, vec):
        "suma: self += vec"
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z
        return self

    def __eq__(self, vec):
        return self.x == vec.x and self.y == vec.y and self.z == vec.z

    def __ne__(self, vec):
        return not self == vec
        
    def __mul__(self, vec):
        "iloczyn: self * vec"
        return self.x*vec.x + self.y*vec.y + self.z*vec.z
        
    def norm(self):
        "norma wektora: self"
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

class Point:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return '(%.2f, %.2f, %.2f)' % (self.x, self.y, self.z)

    def __sub__(self, poi):
        return Vector(self.x - poi.x, self.y - poi.y, self.z - poi.z)

    def __add__(self, vec):
        return Point(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __iadd__(self, vec):
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z
        return self

class Triangle:
  def __init__(self, A, B, C):
    self.A = A
    self.B = B
    self.C = C
    
  def __repr__(self):
    return 'Triangle: %s, %s, %s' % (self.A, self.B, self.C)
    
  def perimeter(self):
    a = self.B - self.C
    b = self.A - self.C
    c = self.A - self.B
    print('Perimeter: ')
    return a.norm() + b.norm() + c.norm()
    
  def area(self):
    v = self.B - self.C
    a = v.norm()
    
    v = self.A - self.C
    b = v.norm()
    
    v = self.A - self.B
    c = v.norm()
    
    p = self.perimeter()/2
    
    P = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print('Area: ')
    return P


A = Point(input_point_1_A, input_point_2_A, input_point_3_A)
B = Point(input_point_1_B, input_point_2_B, input_point_3_B)
C = Point(input_point_1_C, input_point_2_C, input_point_3_C)
t = Triangle(A, B, C)


print(t)
print(t.perimeter())
print(t.area())