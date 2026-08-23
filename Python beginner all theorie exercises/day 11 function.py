# Day 11 about the function code

# Defining a function means that its a reusable block of codes that could perform a certain task. 
# We use the def keyword to defined the function only if its only invoked

# lets do some example for the def functions

def get_sum_total_number(*args):
    total = 0
    for number in args:
        total+= number
    return total

print(get_sum_total_number(*range(1,5)))
print(get_sum_total_number(*[1,2,3,4,5]))

def greet(name, location):
    print("Hi there",name,'How is the weather in',location)
    return None
greet(name='Alice',location='Montreal')

s_dict = {'name':'Alice','location':'New york'}
s_dict = {'location':'New york','name':'Eric'}
greet(**s_dict)

def arbitrary_named_args(**args):
        print("I received an arbitrary number of arguments, totaling", len(args))
        print("They are provided as a dictionary in my function:", type(args))
        print("Let's print them:")
        for k,v in args.items():
             print("*keys:",k,'*value:',v)


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
s_dict = {'location':'New york'}
arbitrary_named_args(Doctor="Smith", Professor="Johnson", Engineer="Brown")
arbitrary_named_args(**s_dict)
arbitrary_named_args(**person)


def add_two_numbers(number_1,number_2):
    sum = number_1 + number_2
    print(sum)
    return sum

print(add_two_numbers(50,20))     

import math
def Area_of_circle(radius):
     pi = 3.14
     area = math.pi*radius*radius
     return area

print(Area_of_circle(20))
