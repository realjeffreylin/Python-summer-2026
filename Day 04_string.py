s = 'Coding for all persons'
l = s.split()
r = ''
for x in l:
    r+= x[0]

# r.upper()
print(f'The acronym of "{s}" is: {r.upper()}')

S_2 = 'You cannot end a sentence with because because because is a conjunction'


end= S_2.rfind('because')+len('because')
start=S_2.find('because')
print(S_2[start:end])



s= 'I am enjoying this challenge.\nI just wonder what is next.'
s = '''Name\t\tAge\tCountry\tCity
Asabeneh\t250\tFinland\tHelsinki'''
print(s)

a=8
b=6

print(f'{a}+{b} ={a+b}') # 
print(f'{a}*{b} ={a*b}')


print('{2}//{2} ={0}'.format(a,b,(a//b)))

''' 
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''