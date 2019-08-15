# is_Palindrowme.py

input_first_Number = input('Input number: ')
number = int(input_first_Number)

def main():
	print( "Is Palindrome \"%s\" = %s" % ( number, is_Palindrome(number) ) )

def is_Palindrome(number):
    first_Number = number
    second_Number = 0

    while first_Number > 0:
        right_number = first_Number % 10
        second_Number = second_Number * 10 + right_number
        first_Number = first_Number / 10

    if number == second_Number:
        return True
    else:
        return False
main()