num1 = float(input("Type first number: "))
num2 = float(input("Type second number: "))

operation = input("Please, choose operation:\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Modulo division\n6. All operations together\n")

print("You`re number 1 (num1)= ", num1)
print("You`re number 2 (num2)= ", num2)
print("You`re choose was: ", operation)

if operation == "1":
    print("Result Addition: ", num1 + num2)
elif operation == "2":
    print("Result Substraction num1-num2: ", num1 - num2)
elif operation == "3":
    print("Result Multiplication: ", num1 * num2)
elif operation == "4":
    print("Result Division num1/num2: ", num1 / num2)
elif operation == "5":
    print("Result Modulo division num1%num2: ", num1 % num2)
elif operation == "6":
    print("\nResult Addition: ", num1 + num2, "\nResult Substraction: ", num1 - num2, "\nResult Multiplication: ", num1 * num2, "\nResult Division: ", num1 / num2, "\nResult Modulo division: ", num1 % num2)
