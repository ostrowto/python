# nested_exception_handling.py

try_Again = True
while try_Again:
    try:
        my_Value = int(input('Please, type a whole number: '))
    except ValueError:
        print('Please be sure to input a whole number only! ')
        try:
            do_Over = input('Try again Yes or No? ')
        except:
            print('Thank You very much! Bye!')
            try_Again = False
        else:
            if (str.upper(do_Over) == 'N'):
                try_Again = False
    except KeyboardInterrupt:
        print('You`ve pressed CTRL+C! ')
        print('Have a nice day! ')
        try_Again = False
    else:
        print(my_Value)
        try_Again = False