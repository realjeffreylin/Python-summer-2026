# Python exercises day 7 set level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Nvidia','Intel'])
print(it_companies)

it_companies.remove('Intel')
print(it_companies)

it_companies.discard('Twitter')
print(it_companies)

# Exercises level 2 
A.union(B)
print(B)

A.intersection(B)
print(A)

A.issubset(B)
print(A)

A.isdisjoint(B)
print(A)

A.union(B)
print(B)
B.union(A)
print(A)

A.symmetric_difference(B)
print(B)

A = {19, 22, 24, 20, 25, 26}
del A
print()

# Exercises level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
lst = set(age)
print(lst)
print(len(lst))
print(len(age))

# Difference between set , string , list and tuple 
# Set is a data type that is distinct that means that it doesnt allow 2 item into the same set and their are immutable that means they could not be modifty the way they are
# Tuple still a data type that is fixed size list and it allows 2 duplicate item inside of the list and you cannot modify insert or deleted litle by litle the items
# String is a data type that consist a series of setence or words after we declare a  variable
# List is a data type that you could make by modifying the changes and also you can put 2 members duplicate inside and you can put a series of other different data type inside

Str = 'I am a teacher and I love to inspire and teach people'
St = set(Str)
L = set(St)

print(St)
L = Str.split()
print(L)
