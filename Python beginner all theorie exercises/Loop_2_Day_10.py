def exercises_18_01():
    x = 1
    while x <= 100:
        x = x + 1 

        if x in [50,60,70,80,90,100]:
            continue

        print(x)

    else:
        print('end the value of x is {}'.format(x))


numbers = [0, 1, 2, 3, 4, 5]
for x in numbers:
    print(x)


language = 'Python'
for letter in language:
    print(letter)

for I in range(0,len(language) -1):
    print(I,language[I])

numbers = (0,1,2,3,4,5)
for y in numbers:
    print(y)

person = {
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

for key in person:
    print(key)

for v in person.values():
    print(v)

for k,v in person.items():
    print(k,':****',v)

numbers = (1,2,3,4,5)
for I in numbers:
    print(I)
    if I == 3:
        continue
    print('The next number should be',I + 1) 


# Finding the range function 

lst = list(range(10))
print(lst)
tpl = tuple(range(32))
print(tpl)
st = set(range(10))
print(st) 

lst= list(range(23,0,-12))
print(lst)

tpl = tuple(range(3,1,+ 2))
print(tpl)

for I in range(9):
    print(I)

# Nested condition in loop
# We can write loop inside of a loop

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == 'address':
        for address in person['address']:
            print(address)


# Lets do another nested loop by our own
Dct = {'Car':'Ford','Engine':'Coyote V8','Model':'Mustang Darkhorse','Horsepower': 480}

for I in Dct:
    if Dct == 'Car':
        for I in Dct['Car']:
            print(I)


# For loop else 
for x in range(11):
    print(x)
else:
    print('the loop of this number finished at',x)

for g in range(4):
    print(g)
else:
    print('This range of this number finished at',g)

# The pass function 
for x in range(423):
    pass



for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print('The skill of the person is {}'.format(skill))


number = 99
for number in range(1,24,5):
    pass
    #print(number)
#else:
print('This loop of number end with {}'.format(number))


for number in range(10,0):
    print(number)

I = 48
while I>=35:
    print(I)
    I = I - 2

for i in range(1,8):
    print('#'*i)

for x in range(1,9):
    for y in range(1,9):
        print('#',end=' ')
    print('',end='|\n')

for t in range(0,11):
   #for u in range(0,11):
#    p = t*t
   print('{} * {} = {}'.format(t,t,t*t))


lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skills in lst:
    print(skills)

for number in range(0,101,2):
    print(number)

for digit in range(1,101,2):
    print(digit)


# Exercises level 2 day 10 loops 
total_sum = 0
for number in range(0,101):
    total_sum += number

print('The sum of all number is {}'.format(total_sum))

total_sum_even = 0
total_sum_odd = 0

for u in range(0,101,2):
    total_sum_even +=u

for x in range(1,101,2):
    total_sum_odd +=x

print('The sum of all number even is {}. And the sum of all odds is {}.'.format(total_sum_even, total_sum_odd))

# Exercises level 3 loops

from  countries import countries
land = list()
for c in countries:
    if 'land' in c:
        land.append(c)

print(land)

fruits = ['banana', 'orange', 'mango', 'lemon','Pear']
fruits_reverse=list()
l=len(fruits)
for I in range(l-1,-1,-1):
#for I in range( -1, -1*l-1,-1):
   
    print( 'The value I== {}, fruits[I]=={}'.format(I,  fruits[I]))
    #fruits_reverse.append(I)
    fruits_reverse.append(fruits[I])

print(fruits_reverse)

import json
f=open(r"C:\30dayPython\Python-summer-2026\Python beginner all theorie exercises\countries-data.py", "r", encoding="utf-8")
countries=json.load(f)
f.close()


langs = ['Norwegian', 'Norwegian Bokmål', 'Norwegian Nynorsk']




print(countries[0])
print(countries[-1])


total_languages = 0
for c in countries:
    print(c['name'],  c['languages'],len(c['languages']))
    total_languages = total_languages + len(c['languages'])
print(total_languages)  

languages_count = dict()  



def fc( t:tuple):
        return t[1]


for c in countries:
    for l in c['languages']:
        if l in languages_count:
            languages_count[l] = languages_count[l] + 1
        else:
            languages_count[l] = 1
#s = {k:v for k,v in sorted(languages_count.items(), key=lambda x: x[1],reverse=True)}
s = {k:v for k,v in sorted(languages_count.items(), key=fc,reverse=True)}
print(s)

for i, item in enumerate( s):
    if i<=10:
        print('No {} language {} are spoken by {}'.format(i+1,item, s[item]))