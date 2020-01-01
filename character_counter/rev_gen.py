# rev_gen.py

class rev_gen:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def main():
    rev = rev_gen('any text 123')
    for x in rev:
        print(x)

if __name__ == '__main__':
    main()