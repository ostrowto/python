# enumerate_iterator_1.py

my_value = int(input('Your value for iterator: '))

class my_Increment_Iterator:

    def __init__(self, my_number):
        self.my_number = my_number
        self.my_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.my_number == self.my_item:
            raise StopIteration

        self.my_item += 1
        return self.my_item

for my_item, num in enumerate(my_Increment_Iterator(my_value)):
    print(my_item, num)