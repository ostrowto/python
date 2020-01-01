# rev_data.py

def rev_data(data):
    for index in range(len(data) -1, -1, -1):
        yield data[index]

def main():
    rev = rev_data('Any text 1234')
    for x in rev:
        print(x)

    data = 'Any text 12345'
    print(list(data[i] for i in range(len(data) -1, -1, -1)))

if __name__ == '__main__':
    main()