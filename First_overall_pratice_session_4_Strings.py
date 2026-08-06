letter = 'O'
print(letter)
print(len(letter))

text = 'I am very happy too see you man!'
print(text)
print(len(text))

message = '''This morning I felt really sloppy. But at least
I am able to get my focus back to work.'''
print(message)

message = """ Well obivously even I was trying to be a Nissan Altima driver in resseanler county. My car
broke down with a check engine light and 2 exploded tires."""
print(message)

#Creating a String

#String contentation
Nissan_Altima_drivers = 'Stupid on the road'
Speed_limit_for_them = 'No limit'
space = ''
Their_Stereotype = Nissan_Altima_drivers+Speed_limit_for_them+space
print(Their_Stereotype)

print(len(Nissan_Altima_drivers))
print(len(Speed_limit_for_them))
print(len(Nissan_Altima_drivers) < len(Speed_limit_for_them))


#Escape sequence In strings
print('This learning process takes a lot of pratice.\nAre you gonna pratice it')
print('Day\tPage\tExercises')
print('Day1\t6\t5')
print('Day 2 \t13\t20')
print('This is a back slash symbol(\\)')
print('This message is adressed to my best friend Charles "I am proud of you\"')


#String formatting
First_Day = 'Happy'
Last_Day = 'Sad'
Feeling = 'Neutral'
Formatted_String = 'The first day I am %s and the last day I am %s. I am feeling %s'%(First_Day,Last_Day,Feeling)
print(Formatted_String)

length = 23
width = 32
area = length*width
String_Formatting = 'The area of this rectangle is %d paired this the length which is %d'%(length,area)
print(String_Formatting)

#New style of the string in python introduce in python 3 
first_name = 'Jeffrey'
last_name = 'Lin'
home_town = 'Lasalle'
Formatted_String = 'I am {} {}. I live in {}.'.format(first_name,last_name,home_town)
print(Formatted_String)

#String interpolation examples start with f strings
t = 42
u = 31
print(f'{t}-{u} = {t-u}')
print(f'{t}+{u} = {t+u}')

#Python string as a sequence of Characters
word = 'Home' #Always start up from 0 with the first letter and finished at the end of the last letter
a,b,c,d = word
print(a)
print(b)
print(c)
print(d)

Country = 'Mongolia'
first_letter = Country[0]
print(first_letter)
second_letter = Country[1]
print(second_letter)
last_index = len(first_letter) -2
last_letter = Country[last_index]
print(last_letter)

Country = 'Canada'
first_letter = Country[-1]
print(first_letter)
last_letter = Country[-2]
print(last_letter)

Home = 'Expensive'
first_letter = Home[0:3]
print(first_letter)
second_letter = Home[3:6]
print(second_letter)
last_three = Home[6:9]
print(last_three)

#Reversing a string
text = 'I want to ban all Nissan Altima and Bmw drivers that cut into traffic what the hell'
print(text[::-1])

computer = 'Microsoft'
Micros = computer[0:6:2]
print(Micros)

Car = 'Nissan'
Niss = Car[0:3:1]
print(Niss)

#String method 
#first one being the captitalize
message = 'i love being a maniac one the road'
print(message.capitalize())

text = 'here i am being a fucking pussy if you know that'
print(text.capitalize())

#Second one being the count() function
Job = 'Working at mcdonald as a cashier'
print(Job.count('g'))
print(Job.count('g',14,16))
print(Job.count('as'))

#Third one is finished with endwith
Outpout = 'My name is Jeffrey and I am here to be an actual stupid guy on the street'
print(Outpout.endswith('eet'))
print(Outpout.endswith('pid'))

#Isalum, Alphanumeric number 
Outpout ='I dont had any friends to deal with right now'
print(Outpout.isalnum())

Outpout = 'I am very depressed right now'
print(Outpout.isalnum())

Outpout = '20daysofworks'
print(Outpout.isalnum())

#Checking if all the strings are in overall in decimal isdecimal
Outpout = '321'
print(Outpout.isdecimal())

Outpout = 'Thirty days of python'
print(Outpout.isdecimal())

#Checking if all the lowerstring all in lower case isslower
message ='20 days of working non stop would be like'
print(message.islower())

message ='I am kinda slow dude'
print(message.islower())

#The variables with startwith that specified what word to start with the string that we want to input inside
Variable ='I am learning python very hard to succeed my life and It is the first august gotta work harder next time'
print(Variable.startswith('I am learning'))

Variable ='Well here is my last phrase to learned with the day 4 course now on day 5 course'
print(Variable.startswith('Well here'))


