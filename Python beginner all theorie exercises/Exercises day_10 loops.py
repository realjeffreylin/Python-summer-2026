
# Exercises day 10 loops

#Exercises level 1
numbers = [0,1,2,3,4,5,6,7,8,9,10]
for digit in numbers:
    print(digit)

number = 0
while number <= 10:
    print(number)
    number+=1

numbers = [10,9,8,7,6,5,4,3,2,1,0]
for number in numbers:
    print(number)

number = 10
while number >=11:
    print(number)
    i-= 1 

print("#")
print("##")
print("###")
print('####')
print('#####')
print('######')
print('#######')

# Nested loop for the hashtag

for u in range(8):
    for u in range(8):
        print("#", end="")
        print()



print('0x0=0')
print('1x1=1')
print('2x2=4')
print('3x3=9')
print('4x4=16')
print('5x5=25')
print('6x6=36')
print('7x7=49')
print('8x8=64')
print('9x9=81')
print('10x10=100')


lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in lst:
    print(language)

for number in range(0,100,2):
    print(number)

for number in range(1,101):
    if number % 2 !=0:
        print(number)


# Exercises level 2 in python 
num = input('Enter your number')
total_sum_of_number = 0

for numb in range('num + 1'):
    print('The total sum from all number is {}'.format(numb))


