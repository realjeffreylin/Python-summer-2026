# Exercises day 11 level 1 functions

def add_two_numbers(number_one,number_two):
    sum = number_one + number_two
    return sum

print(add_two_numbers(90,23))

def area_of_circle(radius):
    import math
    pi = 3,1416
    area = math.pi * radius * radius
    return area

print(area_of_circle(80))

def add_all_nums(*number):
    for digit in number:
        if not isinstance(digit, (float, int)):
            print('Type your number')

    return sum(number)

print(add_all_nums(2.5,4))
print(add_all_nums(5.9,10))

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*9/5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(10))
print(convert_celsius_to_fahrenheit(50))


def check_season(month):
    season = ['Autumn','Spring','Winter','Summer']
    i = -1
    if month in('September','October','November'):
        i = 0
        return season[0]
    elif month in ('March','April','Mai'):
        return season[1]
    elif month in ('December','January','Feburary',):
        return season[2]
    elif month in ('June','July','August'):
        return season[3]
    else:
        i=-1
    return season[i]
def check_season_2(month):
    season = ['Autumn','Spring','Winter','Summer']

    # Month_season_mapping = {
    #     'September':'Autumn',
    #     'October':'Autumn',
    #     'November':'Autumn',
    #     'March':'Spring',
    #     'April':'Spring',
    #     'Mai':'Spring',
    #     'December':'Winter',
    #     'January':'Winter',
    #     'Feburary':'Winter',
    #     'June':'Summer',
    #     'July':'Summer',
    #     'August':'Summer'}
    from Day_11_seasons_new import Month_season_mapping


    return  Month_season_mapping.get(month,'the month is not valid')


print(check_season('December'))
print(check_season('November'))
print(check_season('July'))

print(check_season_2('December'))
print(check_season_2('November'))

import math
def calculate_slope(A,B):
    x_1 = A[0]
    y_1 = A[1]

    x_2, y_2 = B
    Line_A = x_2 - x_1
    Line_B = y_2 - y_1
    slope = math.sqrt(Line_A**2 + Line_B**2)
    return slope

p1 = (4, 5)
p2 = (1,1)

print(calculate_slope(p1, p2))
print(calculate_slope((1, 5), (3, 8)))

import math

def solve_quadratic_equation(a, b, c):
    discriminant_value = (b) * (b) - 4 * (a) * (c)

 
    if discriminant_value > 0:
        sqrt_value = math.sqrt(discriminant_value)
        print('real and different root')
        print((-b + sqrt_value) / (2 * a))
        print((-b - sqrt_value) / (2 * a))
        return ((-b - sqrt_value) / (2 * a),
            (-b + sqrt_value) / (2 * a))
    elif discriminant_value == 0:
        print('The quadratic equation had only one solution')
        print(-b/(2*a))
    else:
        if discriminant_value < 0:
            print('The quadratic does not had any solution')
            return discriminant_value
        
# a, b, c = (int, input('Enter the values for a, b, and c separated by spaces:').split())
# print(solve_quadratic_equation(a=5,b=4,c=6))



def print_list(lst_1, lst_2):
    lst_3 = lst_1 + lst_2  
    return lst_3

print(print_list(lst_1=[1, 2, 3, 4, 5], lst_2=['A','B','C']))


def reverse_list(thelist):
    reverse_list=[]
    for item in thelist:
        reverse_list.insert(0,item)

    return reverse_list

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(['A','B','C']))



def add_item(lst,item):
    newlst = lst.copy()
    newlst.append(item)
    return newlst




# print(add_item(food_stuff='Meat'))

# def add_item2(number):
#     number = [2,3,7,9]
#     number.append(5)
#     return number

# print(add_item(number=5)) # I dont know how to merged two item and parameter at the same time

# def remove_item(food_stuff):
#     food_stuff=['Potato', 'Tomato', 'Mango', 'Milk']
#     food_stuff.remove('Mango')
#     return food_stuff

# print(remove_item(food_stuff='Mango'))

# def remove_item(number):
#     number= [2,3,7,9]
#     number.remove(3)
#     return number

# print(remove_item(number=3))


# def sum_of_numbers(sum):


# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
#  print(add_item(food_stuff, 'Meat')) 

#  print( food_stuff )

def remove_item(lst,item):
    new_lst = lst.copy()
    new_lst.remove(item)
    return new_lst

numbers =[2,3,7,9]
print(remove_item(numbers,3))

def sum_of_numbers(number):
    result = 0
    for a in range(1,number+1,1):
        result = result + a

    return result

print( sum_of_numbers(5))
print( sum_of_numbers(10))
print(sum_of_numbers(100))
    



