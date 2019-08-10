# Generate Pythagorean Triplets
print(
'''
Math theory:
A Pythagorean triplet is a set of three positive integers a, b and c
such that a2 + b2 = c2. 
Given a limit, generate all Pythagorean Triples
with values smaller than given limit.
--------------------------------------------------------------------
Solution: to generate these triplets smaller than given limit using three nested loop. 

Instruction:
1. Input max value.
2. Press enter.
3. A file: "Generated_Pythagorean_Triplets.txt" will be generated.
4. Remember - value greater than 200 will be long computed.

'''
'''
*******************************
*Generate Pythagorean Triplets*
*******************************
''')

import sys

input_max_value = int(input('Input max value: '))
r = range(1, input_max_value)

pitagoras_triangle = [(a, b, c) for a in r for b in r for c in r if ((a * a) + (b * b) == (c * c)) and (a < b)]
sys.stdout = open('Generated_Pythagorean_Triplets.txt', 'w')
print(pitagoras_triangle)


