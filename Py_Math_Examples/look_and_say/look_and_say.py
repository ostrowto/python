def next_look_and_say(number):
    wynik = ''
 
    powtorz = number[0]
    number = number[1:] + ' '
    times = 1
 
    for actual in number:
        if actual != powtorz:
            wynik += str(times) + powtorz
            times = 1
            powtorz = actual
        else:
            times += 1
 
    return wynik
 
num = '1'
 
for i in range(10):
    print (num)
    num = next_look_and_say(num)
