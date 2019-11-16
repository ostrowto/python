# read_text_from_file.py

# Read text from file

plik = open('numbers.txt', encoding = 'utf8')
tekst_1 = plik.read()

# Delete non-alpha letters and everything to lower

tekst_2 = ''.join(c for c in tekst_1 if c not in '-:.,?;!()[]{}"\'').lower()


# Counter

counter_Num = {}
for i in tekst_2.split():
    if (len(i)>2):
        if i not in counter_Num:
            counter_Num[i] = 1
        else:
            counter_Num[i] += 1


# List of top 6 characters
top_6=[]
while len(top_6)<6:
    for k,v in counter_Num.items():
        if v == max(counter_Num.values()):
            if k not in top_6:
                top_6.append(k)
                counter_Num[k] = 0


for i in range (6):
    print(str(i+1)+".",top_6[i])
