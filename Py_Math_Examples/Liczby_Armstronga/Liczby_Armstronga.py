# Liczby Armstronga



start_num = int(input("Podaj dolną granice zakresu badania: "))
end_num = int(input("Podaj gorna granice zakresu badania: "))

for search_num in range(start_num, end_num + 1):

    numbers = len(str(search_num))
    sum = 0
    compute = search_num
    while compute > 0:
       number_2  = compute % 10
       sum += number_2 ** numbers
       compute //= 10
    if search_num == sum:
       print('Liczba armstronga to: ', search_num)
