#cube.py

def cube(i):
    return i*i*i

cubes = [cube(i) for i in range(10)]
print("Cubes: ", cubes)