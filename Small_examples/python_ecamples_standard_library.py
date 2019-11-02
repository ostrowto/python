# Some examples from standard library

from collections import namedtuple

# NamedTuple

Features = namedtuple('Features', ['age', 'gender', 'name'])
row = Features(age = 22, gender = 'male', name = 'Alex')

print(row.age)

# Counter

from collections import Counter
ages = [22, 22, 25, 25, 30, 24, 26, 24, 35, 45, 52, 22, 22, 22, 25, 16, 11, 15, 40, 30]
value_counts = Counter(ages)
print(value_counts.most_common())

#DefaultDict

from collections import defaultdict

my_default_dict = defaultdict(int)
for letter in 'The red fox ran as fast as it could':
    my_default_dict[letter] += 1
print(my_default_dict)