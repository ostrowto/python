# scalar product of two vectors - vector multiplications

input_vecotr_1_x = int(input('Input vector 1 parametr x: '))
input_vecotr_1_y = int(input('Input vector 1 parametr y: '))
input_vecotr_1_z = int(input('Input vector 1 parametr z: '))
input_vecotr_2_x = int(input('Input vector 2 parametr x: '))
input_vecotr_2_y = int(input('Input vector 2 parametr y: '))
input_vecotr_2_z = int(input('Input vector 2 parametr z: '))


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
        return vec.x * self.x  + vec.y * self.y + vec.z * self.z

v_1 = Vector(input_vecotr_1_x, input_vecotr_1_y, input_vecotr_1_z)
v_2 = Vector(input_vecotr_2_x, input_vecotr_2_y, input_vecotr_2_z)

print('Scalar product of two vectors: ')
print(v_1 * v_2)
print('Add two vectors: ')
print(v_1 + v_2)
