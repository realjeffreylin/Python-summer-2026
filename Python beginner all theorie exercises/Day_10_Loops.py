# Day 10 loops theory exercises 
# Lets start of with the while statement loop
x = 0
while x < 5:
    print(x)
    x = x + 1

# if the statement of this expression is false we gotta use else to conclude the code executation
assign_variable = 12
while assign_variable < 24:
    print(assign_variable)
    assign_variable = assign_variable + 24
else:
    print(assign_variable) # We know that 12 is smaller than 24 so its gonna execute on the while condition because its true otherwise on else

# Example of using the break or the continue statement for the loop

Variable = 0
while Variable < 12:
    print(Variable)
    if Variable == 5:
        break
    Variable = Variable + 1

Another_condition = 3
while Another_condition < 12:
    print(Another_condition)
    if Another_condition == 5:
        break
    Another_condition = Another_condition + 2


# Using the continue statement for the loops

Condition = 30
while Condition < 40:
    print(Condition)
    if Condition == 30:
        Condition += 12
        continue
Condition += 12

Vrl = 40
while Vrl > 35:
    print(Vrl)
    if Vrl == 34:
        Vrl =+ 12
        continue
Vrl = Vrl + 2    

# For loop function 

# For condition of this loop its only use when we itirate from a sequence of list, tuples, dictionarries or set or string or even integers from a list 

numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

tpl = ('Sad','Happy','Intelligent')
for emotion in tpl:
    print(emotion)

# Using the keyword for into the sequence of the strings
# One example of using string in a for loop
# for itirator in string

country = 'Cananda'
for word in country:
    print(word)

Setence = 'I am feeling good today'
for word in Setence:
    print(word)

# Writing a tuple function with a loop
tpl = ('Y','X','Z')
for letter in tpl:
    print(letter)

# Executing a function with a set with for 
Houses = {'Condo','Appartement','Duplex'}
for resident in Houses:
    print(resident)

# break and continue part 2 
Value = (12,24,36,48)
for numbers in Value:
    print(numbers)
    if Value == 72:
        break

Letter = ('A','B','C','D')
for character in letter:
    print(character)
    if character < 4:
        continue


x = 23
while x < 10:
    print(x)
    x = x + 1