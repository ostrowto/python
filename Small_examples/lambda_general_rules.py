# Lambda function general rules
input_x = (int(input('Please input x parameter: ')))
input_y = (int(input('Please input x parameter: ')))
input_z = (int(input('Please input x parameter: ')))

x = input_x
y = input_y
z = input_z

# Standard function in Python (add)
def my_Func(x, y, z):
    result = x + y + z
    return result
print('This is the result from standard function: ', my_Func(x, y, z))

# Lambda function (mul)

result_2 = lambda x, y, z : x * y * z

print('This is the result from Lambda function: ', result_2(x, y, z))
 
