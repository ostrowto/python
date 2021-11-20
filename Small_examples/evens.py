#evens.py

list_evens = []
list_not_evens = []

evens = [i for i in range(20) if i%2==0]
list_evens.append(evens)
print("Evens numbers: ", list_evens)

notevens = [i for i in range(20) if i%2!=0]
list_not_evens.append(notevens)
print("Not evens numbers: ", list_not_evens)

