# Day 9 learning condiotional theorie and exercises at the end
a = int(input("Enter a number: " ) or 2)

a =int(a)
if a == 3:
    print('{0} is equal to 3'.format(a))
elif a > 3:
    print('{0} is greater than 3'.format(a))
else:
    print('{0} is less than 3'.format(a))

print('You passed the exam' if a >= 60 else 'You failed the exam')

# ...existing code...
def check_adult(age):
    if age >= 18:
        return True
    else:
        return False

if check_adult(a):
    print('{0} is an adult.'.format(a))
else:
    print('{0} is not an adult.'.format(a))

a = 82
grade = "A" if a >= 90 else "B" if a >= 75 else "C" if a >= 60 else "F"

if a >= 90:
    grade = "A" 
elif a >= 75:
    grade = "B"
elif a >= 60:
    grade = "C"
else:
    grade = "F"
print(grade)

a = 0
if a > 0 and a % 2 == 0:
    print('{0} is a positive and even number.'.format(a))
elif a > 0 and a % 2 != 0:
    print('{0} is a positive and odd number.'.format(a))
else:
    print('{0} is not a positive number.'.format(a))    
