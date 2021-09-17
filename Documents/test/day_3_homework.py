"""IF, ELIF, ELSE"""

# 1. Enter your name, then find the sum of the ASCII values of the letters in your name. If that number is larger than
# 500, print "I've got a great name!", and "I've got a fancy name!" otherwise.
# Ներմուծեք ձեր անունը և գտեք անվան տառերի ASCII արժեքների գումարը։ Եթե թիվը մեծ է 500-ից, տպել "I've got a great
# name!", իսկ հակառակ դեպքում՝ "I've got a fancy name!"։

print('Ex. 1')
print("-" * 100)

name = input('Your Name: ')
sum_ascii = 0
for i in name:
    sum_ascii += ord(i)
if sum_ascii > 500:
    print(f'I\'ve got a great name! ({sum_ascii})')
else:
    print(f'I\'ve got a fancy name!({sum_ascii})')





# 2. Ask the user for a movie title. If the title starts with a capital letter, print "Great title!", otherwise print
# "Titles start with capital letters...". If the input starts with a special character [!, @, #, $, %, ^, &], print "I
# doubt that this is a title.".
# Պահանջել ներմուծել ֆիլմի վերնագիր։ Եթե վերնագիրը սկսվում է մեծատառով, տպել "Great title!", հակառակ դեպքում տպել
# "Titles start with capital letters..."։ Եթե ներմուծվածը սկսվում է [!, @, #, $, %, ^, &] նշաններով, տպել "I doubt that
# this is a title."․

print('Ex. 2')
print("-" * 100)

import re
mt = input(str('Movie title: '))

sc = re.compile('!, @, #, $, %, ^, &')
if  64 < ord(mt[0]) < 91:
    print('Great title!')
elif (sc.search(mt) != None):
    print('I doubt that this is a title.')
else:
    print('Title doesn\'t start with capital letters...')

print ('-' * 10 + '>' + '   ' + 'CODE DOESN\'T WORK AS EXPECTED' + '   ' + '<' + '-' * 10)





# 3. Ask the user to input his/her age. If the user is older than 18, than tell them they're eligible to vote. If they
# are younger than 18, tell them how many years do they have to wait.
# Հարցրեք օգտատիրոջ տարիքը։ Եթե նա 18 տարեկանից մեծ է, նրան տեղյակ պահեք, որ կարող է քվեարկել։ Հակառակ դեպքում ասեք, թե
# քանի տարուց նա կկարողանա դա անել։


print('Ex. 3')
print("-" * 100)

age = int(input('Your age: '))
if age > 18:
    print('You\'re eligible to vote')
else:
    print(f'You will be able to vote after {18 - age} years.')





# 4. Write a program that will tell us whether a given year is a leap year or not.
# Գրել ծրագիր, որը կտեղեկացնի, թե տրված տարին նահանջ է, թե ոչ։


print('Ex. 4')
print("-" * 100)

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
    print('This is a leap year.')
else:
    print('This isn\'t a leap year.')





# 5. Using 'random' module, generate a random number between -1000 and 1000. If the number is positive, print positive.
# If it's negative, print negative along with the absolute value of the number.
# Օգտագործելով random գրադարանը, գեներացնել [-1000,1000]-ը տիրույթում պատահական թիվ։ Եթե թիվը դրական է, տպել positive.
# Հակառակ դեպքում տպել negative և այդ թվի բացարձակ արժեքը։


print('Ex. 5')
print("-" * 100)

import random

randnum = random.randint(-1000, 1000)
print(randnum)
if randnum > 0:
    print('Positive')
elif randnum == 0:
    print('the number is 0')
else:
    print(f'Negative {abs(randnum)}')