# itertools: permutations, combinations, groupby, cycle

from itertools import permutations
from itertools import combinations
from itertools import groupby

my_list = [1,2,6]
perm = permutations(my_list,3)
print('Permutations',*perm)

comb = combinations(my_list,2)
print('Combinations',*comb)

# function for key attribute for groupby function
def smaller_than_3(x):
    return x < 3

group_obj = groupby(my_list,key=smaller_than_3)
# group_obj = groupby(my_list,key=lambda x: x<3) # using lambda function for key attribute
for key, value in group_obj:
    print(key, *value)

# another example for groupby function
persons = [{'name':'Tim', 'age': 25},{'name': 'Dan', 'age': 25},
           {'name':'Lisa', 'age':23},{'name':'Claire','age':28}]
groupObj = groupby(persons, key=lambda key: key['age'])
for age, values in groupObj:
    print(age , " -> ", [attributes['name'] for attributes in values])
    # for attributes in values:
    #     print(attributes['name'],end=', ')
    # print()

from itertools import cycle
import time

words = {'start':1,'ready':2,'go':0.5}
for word in cycle(words):
    print(word)
    time.sleep(words[word])    