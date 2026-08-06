#Practice day for doing the list course on Python
lst = list()
empty_list = list()
print(len(empty_list))

lst2 = list()


lower_list = []
print(lower_list)

#Listing example for counting the number of item 
listing = ['Banana','Green apple','Strawberry','Watermelon']
print(len(listing))
print('number of fruits:',len(listing))
print('Listing:',listing)

#Accessing the item from a positive index from a list 
Grocery_listing = ['Banana','Strawberry','Carrots','Meat']
first_listing = Grocery_listing[0]
print(first_listing)
Second_listing = Grocery_listing[1]
print(Second_listing)
third_listing = Grocery_listing[2]
print(third_listing)
last_index = len(Grocery_listing) -1
last_fruits = Grocery_listing[last_index]

#Accessing negative index comes into the list 
list_1 = ['Cheese','Screwdrivers','Meat','Gas']
first_listing = list_1[-1]
print(first_listing)
Second_listing = list_1[-2]
print(Second_listing)
third_listing = list_1[-3]
print(third_listing)
last_index = len(list_1) -1
last_list = list_1[last_index]

# Accessing positive and negatif range of item that were found into the list
listing = ['Pencils','Range','Ragebait','Backpack']
first_listing = listing [0:1]
print(first_listing)
Second_listing = listing [1:2]
print(Second_listing)
third_listing = listing [2::]
print(third_listing)

Vegetable = ['Carrots','Cheese','Cabbage','Celery']
first_listing = Vegetable[::-1]
print(first_listing)
Second_listing = Vegetable[-2:-4]
print(Second_listing)
third_listing = Vegetable[::-3]
print(third_listing)

#Modifying the list_1 
list_1 = ['Wallet','Money','Cash','yo']
list_1[0] = 'Shark'
print(list_1)
list_1[1] = 'I dont know'
print(list_1)
last_index =len(list_1) -1

# Cheking item in a list 
list_1 = [12,23,45,56]
does_exist = 12 in list_1
print(does_exist)
does_exist = 44 in list_1 
print(does_exist)

# Removing a list from an item using pop
list_1 = ['I dont know','Pop','Ice cream']
list_1.pop()
print(list_1)

#Removing list_1 using remove 
list_1 = ['Sorry','Sadly','Mouse','I dont know']
list_1.remove('Sorry')
print(list_1)

#Using the remove list_1 by del
list_1 = ['Too bad','Too tired','Too sad','Too weak']
del list_1[0]
print(list_1)
del list_1[1]
print(list_1)
del list_1[2:3]
print(list_1)

#Copying a list_1 
list_1 = ['Banana','Guava','Mango','lemon']
copy_list = list_1.copy()
print(copy_list)

#Joining a operator
list_1 = [1,2,3,4,5,6,7]
zero = [0]
negative = [-1,-2,-3,-4,-5,-6,-7]
total = list_1 + negative 
print(total)

list6 = ['Join','Have fun dude','Had fun']
IDk = ['Sad','Depressed','Lonely']
list6.extend(IDk)
print(list_1)

# Pratice warmup about 10 minutes of python day 5
Variable = []
print(len(Variable))

# How to find the number of item that were in the list
Big = ['Chunky','Old','Tall']
print(len(Big))
print('number of item in this list:',len(Big))

#Finding the index of every list we could fin in the positive way
Small = ['Room','Tight','Affordable']
first_item = Small[0]
print(first_item)
second_item = Small[1]
print(second_item)
third_item = Small[last_index]
print(third_item)