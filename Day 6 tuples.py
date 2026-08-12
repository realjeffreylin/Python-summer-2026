# Day 6 tuples warmup
# How to create a tuple 
Create_tpl = ()
print(Create_tpl)
Tpl = tuple()
print(Tpl)

# Example of using a tuple 
Tpl = ('First_list','Second_list','Third_list')
print(Tpl)

Planets = ('Saturn','Jupiter','Mars','Venus','Earth')
print(Planets)

#Finding the length of alphabet
Variable = ('I dont know','Somehow','Maybe later')
print(Variable)
len(Variable)


#Finding the index of each tuple positive and negatif but no range
Alphabet = ('a','b','c','d','e')
first_aplphabet = Alphabet[0]
print(first_aplphabet)
second_aplahabet = Alphabet[1]
print(second_aplahabet) 
third_alphabet = Alphabet[-2]
print(third_alphabet)
last_index = len(Alphabet) -1
print(last_index)

# Finding the range of the tuple positif and negatif
Cheap_cars = ('Pontiac Sunfire','Hyundai venue','Dodge caravan','Kia soul','Nissan versa','Infinity g35')
Range = Cheap_cars[0:2]
print(Range)
Second_Range = Cheap_cars[-5::]
print(Second_Range)
Last_range = len(Cheap_cars) -1
print(Last_range)

#Finding the boolean on the tuple list
Tpl = ('Strawberry','Blueberry','Pineapple')
print('Character' in Tpl)
print('Strawberry' in Tpl)
print('Superhero' in Tpl)

# Extending the tuple to another tuple together
Hero = ('Kind','Brave','Show that their are capable','Fearless')
Villan = ('Mean','Troublemaker','Destroying the city')
Extension = Hero + Villan
print(Extension)

#Changing from a tuple to a list
Tppl = ('Terminal','Bollean','Python shell','Visual studio code')
lst = list(Tppl)
print(lst)
Tpl = tuple(lst)
print(Tpl)

#Deleting a tuple using the fonction del
Example = ('Science','Math','Geography','French')
del Example

#Exercise to Rewire to our brain
Empty_tpl = ()
print(Empty_tpl)

Bro = ('Jeffrey','Jason')
Sis = ('Madison','Jamie')
Siblings = Bro + Sis
print(Siblings)
print(len(Siblings))
Family_members = Siblings+ ('Mrs.Jones','Mr.Daniel')
print(Family_members)