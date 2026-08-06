#Creating a string on python
Variable = 'IDK'
print(Variable)
print(len(Variable))

#Mutliline string in python for single and double quote 
text = '''Yeahh I really hate to get yelled by my abusive parents.
Leave me alone man I need some peace okay.'''
print(text)

text ="""Yeahh leave me the hell alone i dont want to see my father anymore.
This is enough then figure the fuck out man im tired of this shit."""
print(text)

#Creating a string with mutliple variables
My_age = 'Young'
My_gender = 'male'
space = ''
Full_information = My_age + My_gender + space
print(Full_information)

#Another example
Boring = "Hell"
Father = "Anger issues"
space = ""
overall = Boring +Father+space
print(overall)

#Escape sequence in Python
print('How old are you man u must be in high school kid.\nWhat about you kid?.')
print('This is a double slash quote (\\)')
print('Days\tSubject\tIdk')
print('Day1\t2\t3')
print('The best that a parent can do is "Punishing their kids for no reason."')

#String formatting
Variable = 'Sleepy'
Variable_2 = 'Lazy'
Variable_3 = 'Boredom'
Format_string = 'I am very %s and %s.I also felt very %s.'%(Variable,Variable_2,Variable_3)
print(Format_string)

length = 30
width = 30
area = length*width
Format_string = 'The length of the square is %d. The area of the square is %d.'%(length,area)
print(Format_string)

#Python interpolation introduced in python 3 
First_name = 'Jeffrey'
Last_name = 'Forks'
House_type = 'Appartement'
Format_string = 'I am {} {}. I live in a {}.'.format(First_name,Last_name,House_type)
print(Format_string)

a= 10
b = 10
print(f'{a}+{b} = { a + b =}'.format(a,b,a+b))
print(f'{a}-{b} = {a-b =}'.format(a,b,a-b))

#Strings sequence in characters 
text = 'Yolo'
a,b,c,d = text
print(a)
print(b)
print(c)
print(d)

Word = 'Living'
first_letter = Word[0]
print(first_letter)
second_letter = Word[1]
print(second_letter)
last_letter = len(first_letter) -1
last_index = Word[last_letter]
print(last_letter)

Word = 'Poor'
first_letter = Word[-1]
print(first_letter)
second_letter = Word[-2]
print(second_letter)
last_letter = Word[0]
print(last_letter)

Country = 'United states'
first_letter = Country[0:3]
print(first_letter)
second_letter = Country[3:6]
print(second_letter)
last_letter = Country[6:9]
print(last_letter)

#Reversing a string
text = 'Well I am here to invest my time of working on python'
print(text[::-1])

Message = 'I happily came back from working out in this afternoon now its time to start the course five on python'
print(Message[:: - 2])

# Strings methods
Home = 'Street of sumbeam'
print(Home.capitalize()) #Capitalize method 

Variable = 'i am very fustrated that i am learning very slow on it'
print(Variable.capitalize())

String = 'This message does it really makes sense in my opinion because I gotta lock in when its the first Month of august'
print(String.startswith('This'))

String = 'This is my last session that I would like to interfers to this lessons gotta learn more consistent and understanding the knowledge'
print(String.endswith('and'))

Variable_2 = 'Another message to declare to this computer to work'
print(Variable_2.count('oh'))
print(Variable_2.count('uter'))

Variable_3 = 'This is the last message that I would like to print out'
print(Variable_3.rindex('This'))
print(Variable_3.expandtabs(10))
print(Variable_3.isalnum())

Variable = 'This source of code must had at least 10 characters'
print(Variable.isalnum())

