#list.py

list1 = []
for i in range(10):
    list1.append(i*i)

print("List1: ", list1)

list2 = [i*i for i in range(10)]
print("List2: ", list2)
