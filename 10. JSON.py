import json
# converting python dictionary to json format
# in json
'''

Python              JSON

dict                object
list, tuple         array
str                 string
int, long, float    number
True                true
False               false
None                null

'''

person = {
    "name" : "Arunchandra",
    "age" : 22,
    "city" : "new york",
    "hasChildren" : False,
    "titles" : ['Engineer','Programmer']
}

# dumps and loads are used for string formats or python_obj_formats
# dump and load are used for file formats of json type
personJSON = json.dumps(person, indent=4, sort_keys=True, separators=(","," -> "))
print(personJSON,end='\n')

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4, sort_keys=True)

with open('person.json', 'r') as f:
    person_python_obj = json.load(f)
    print(person_python_obj)

# json.loads(personJSON)

