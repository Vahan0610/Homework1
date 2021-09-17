#
# # total = 0
# # for i in range(0, 10000):
# #     total += i
# #
# # print(total)
#
#
# # print('-' * 100)
# #
# # i = 0
# # while i < 10000:
# #     i += 1
# #
# # print(i)
#
# # import random
# # randnum = random.randint(0, 10)
# # print(randnum)
# # guessed = False
# #
# #
# # while not guesse d:
# #     guessed_num = input()
# #     if int(guessed_num) == randnum:
# #         print('cool')
# #         guessed == True
#
#
#
# #LIST
#
# # lst_1 = [1, 3, 6]
# # lst_2 = [5, 7, 9]
# #
# # lst_1.extend(lst_2)
# # print(lst_1)
#
#
# # lst_1 = [1, 3, 6]
# # lst_2 = [5, 7, 9]
# #
# # lst_3 = lst_1 + lst_2
# # print(lst_3)
#
#
#
# print('-' * 100)
#
#
#
# # nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
# # count = 0
# # for i in nonsense:
# #     if i == "b":
# #         count += 1
# #
# # print(count)
#
#
#
# print('-' * 100)
#
#
# # n = int(input("your number: "))
# # fact = 1
# # for i in range(1, n + 1):
# #     fact *= i
# # print(fact)
# #
#
#
#
#
#
# # print('-' * 100)
# #
# # import timeit
# # print(timeit.timeit(stmt = '[i for i in range(1, 100)]'))
#
#
# foods = {'Milk': 'Calcium, Lactose', 'Nutella': 'Calcium',
#          'Cheese': 'Calcium', 'Yoghurt': 'Calcium, Lactose',
#          'Spinach': 'Calcium', 'Fish': 'Calcium'}
#
#
# for i in foods.values():
#     if 'Lactose' in i:
#         print(f'I can\'t consume that {foods.keys()}')
#     else:
#         print(f' {foods.keys()}')
#
#
#
#
#
#
# grades = {'Maths': 7,
#           'Physics': 11,
#           'Geography': 10,
#           'History': 8,
#           'Geometry': 19}
#
# grade = 0
# for i in grades:
#     if i is int:
#         grade += i
#         print(grade)
#


# import re
# mt = input(str('Movie title: '))
# print(type(mt))
# sc = re.compile('!, @, #, $, %, ^, &')
# if  64 < ord(mt[0]) < 91:
#     print('Great title!')
#
# elif (sc.search(mt) != None):
#     print('I doubt that this is a title.')
#
# else:
#     print('Title doesn\'t start with capital letters...')
#
# print('Ex. 3')
# print("-" * 100)
#
# age = int(input('Your age: '))
# if age > 18:
#     print('You\'re eligible to vote')
# else:
#     print(f'You will be able to vote after {18 - age} years.')

#
#
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
#     print('This is a leap year.')
# else:
#     print('This isn\'t a leap year.')


import random

randnum = random.randint(-1000, 1000)
print(randnum)
if randnum > 0:
    print('Positive')
elif randnum == 0:
    print('the number is 0')
else:
    print(f'Negative {abs(randnum)}')
