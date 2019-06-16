# The program is used to enumerate numbers.
# First, we define the range of numbers,
# then the step of progress of enumeration.
# Please use only a whole numbers.
# The result will be printed in a "enum_result.txt" file.

print(''' 
The program is used to enumerate numbers.
Firs, we define the range of numbers,
then the step of progress od enumeration.
Please use onlu a whole numbers.
The result will be prontef in a "enum_result.txt" file.
''')



import sys

start_enum = int(input('Please input a number as startpoint: '))
end_enum_input = int(input('Please input a number as endpoint: '))
end_enum = end_enum_input+1
step_enum = int(input('Please input a number as incrementation step: '))
print('Please wait...')

sys.stdout = open('enum_result.txt', 'w')

for x in range(start_enum, end_enum, step_enum):
    print(x)

sys.stdout.close()