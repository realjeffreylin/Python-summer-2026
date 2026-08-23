
def exercise_level_1_1():
    age = input("Enter your age: ")
    age = int(age)

    missing_year = 18 - age
    if age >= 18:
        print("You are old enough to learn to drive")
    else:
        print("You need {0} more years to learn to drive".format(missing_year))


def exercise_level_1_2():
    your_age = input('Enter your own age:')
    your_age=int(your_age)

    my_age = 17 
    diff = your_age - my_age

    if diff == 1:
        print('You have {} year difference in age'.format(diff))
    else:
        if diff>1:
            print('You have {} years difference in age'.format(diff))
        else:
            print('You are younger or equal')

#exercise_level_2()
def exercise_level_1_3():       
    a=input('Enter number one:')
    a =int(a)
    b=input('Enter number two:')
    b=int(b)

    if a > b:
        print('{} its greater than {}'.format(a,b))
    else:
        print('{} its greater than {}'.format(b,a))
        print(f'{b} its greater than {a}')

#exercise_level_1_3()
def exercises_level_2_1():

    score = input('Enter your score:')
    score = int(score)

    grade = ''
    if score>=90:
        grade = 'A'
    elif score>=80 and score<=89:
        grade = 'B'
    elif score >=70 and score<=79:
        grade = 'C'
    elif score >=60 and score<=69:
        grade = 'D'
    else:
        grade = 'F'
    print('Your grade is {}'.format(grade))

def exercises_level_2_2():
    month = input('Enter the month:')


    Spring = ['March','April','May']
    Summer = ['June','July','August']
    Autumn = ['September','October','November']
    Winter = ['December','January','Feburary']

    if month in Winter:
        Season = 'Winter'
    elif month in Spring:
        Season = 'Spring'
    elif month in Summer:
        Season = 'Summer'
    elif month in Autumn:
        Season = 'Autumn'
    else:
        Season = 'Nul' 
    print('The season of "{0}" is {1}:'.format(month, Season))

    Season = 'Winter' if month in Winter else 'Spring' if month in Spring else 'Summer' if month in Summer else 'Autumn' if month in Autumn else 'nul'
    print(Season)

def exercises_level_2_3():
    fruits = ['banana', 'orange', 'mango', 'lemon']
    new_fruit = input('Enter your fruit:')

    if new_fruit in fruits:
        print('The {} exist on the list'.format(new_fruit))
    else:
        if new_fruit not in fruits:
            print('The {} does not exist in the list. It will be added'.format(new_fruit))
            fruits.append(new_fruit)

    print(fruits)


#exercises_level_2_3()


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayehyy',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills = person["skills"]
    middle_skills = skills[1:-1]
    print('The middle skills are',middle_skills)
else:
    print('skill not availble')    

if 'Python' in skills:
    print('The skill python is in the list {}'.format(skills))
else:
    print('he doesnt had')    

Front_end_dev = ['JavaScript', 'React']
Back_end_dev =['Node', 'MongoDB', 'Python']
Full_stack_dev = [ 'React', 'Node', 'MongoDB']
Full_stack_super_dev = ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']

if skills == Front_end_dev:
    print('He is a front end developper')
elif skills == Back_end_dev:
    print('He is a backend developper')
elif skills == Full_stack_dev:
    print('He is a fullstack developper')
elif skills == Full_stack_super_dev:
    print('He is a superdevelopper')
else:
    print('unknow title')

if person ['is_married']==True and person['country']=='Finland':
    print('\033[91m{} {} \033[0m lives in \033[94m{}\033[0m. He is married.'.format(person['first_name'],person['last_name'],person['country']))


# Linux/Mac/Windows with modern terminals
print('\033[91m' + 'Red text' + '\033[0m')        # Red
print('\033[92m' + 'Green text' + '\033[0m')      # Green
print('\033[94m' + 'Blue text' + '\033[0m')       # Blue
print('\033[93m' + 'Yellow text' + '\033[0m')     # Yellow
print('\033[95m' + 'Magenta text' + '\033[0m')    # Magenta
print('\033[96m' + 'Cyan text' + '\033[0m')       # Cyan








    






    
