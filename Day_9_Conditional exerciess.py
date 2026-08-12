
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

    
