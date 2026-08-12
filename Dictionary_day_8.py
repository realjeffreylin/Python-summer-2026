# Day 8 dictiony exercises practice exercises
dog = dict()
print(dog)

dog = {'name':'Daisy','breed':'Poodle','legs':'short','age':8}
print(dog)

student = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(student))

print(student.get('skills'))
student['skills'] = 'Intel'
print(student)

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
val = dct.values()
print(val)
keys = dct.keys()
print(keys)

tpl = dct.items()
print(tpl)

del dct


# Day 8 dictionary understanding pratice 
# How to create a dictionnary
#Example
dic = dict()
print(dic)

variable_expression = dict()
print(variable_expression)

# Example of a dictionary that is always assign to a key:value that still consider as one category item
dct = {'Name':'Jeffrey','City':'Montreal','Age':17}
print(dct)

# Checking an item inside of a dictionary by using the in keywords 
dct = {}








