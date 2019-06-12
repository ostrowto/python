
import itertools, collections, sys

print('This program is very simply,')
print('- iterate and print over Your sentence.')
print('As result You will become a file called your_result.txt,')
print('- included iterated result in any combination.')
print('WARNING! iteration is very complicated, more characters need more time to print result!')
print('If Your sentence is longer as 6 characters - please be patient...')
print('____________________________')
items_for_iterations = str(input("What do you want to iterate? "))
for p in itertools.permutations(items_for_iterations):
    print(p)

c = collections.Counter(items_for_iterations)
print(c)

sys.stdout = open('your_result.txt', 'w')
print(p)
print("___________________________")
print(c)
sys.stdout.close()
input()

