"""DATA STRUCTURES"""

# 1. Write a program to multiply all the items in a list.
# Գրել ծրագիր, որը կբազմապատկի լիստի բոլոր թվերը։

print('-' * 100)
print('Ex.1')

lst = [2, 4, 6]
lst_1 = []
for i in lst:
    i *= 2
    lst_1.append(i)

print(lst_1)

lst = [i * 2 for i in lst]
print(lst)




# 2. Write a program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings.
# Գրել ծրագիր, որը կհաշվի լիստում եղած 2 կամ ավել երկարություն ունեցող լիստերի քանակը, որոնց առաջին և վերջին տառերը
# նույնն են։

print('-' * 100)
print('Ex.2')

lst_s = ['hello', 'adfFSf', 'bob', 'AnnA', 'k', '23453', 'opppo','KKlado', 'hh']
count = 0

for i in lst_s:
    if len(i) > 1 and i[0] == i[-1]:
        count += 1
print(count)




# 3. Write a program that will remove duplicates from a list. DO NOT use set() method directly on the list.
# Գրել ծրագիր, որը կջնջի դուպլիկատները լիստից։ ՉՕԳՏԱԳՈՐԾԵԼ set() մեթոդը։


print('-' * 100)
print('Ex.3')

### Solution 1:

lst_d = ['hello', 'adfFSf', 'bob', 'AnnA', 'hello', 'k', '23453', 'k', 'hh', 'opppo', 'KKlado', 'hh']
lst_f = []
for i in lst_d:
    if i not in lst_f:
        lst_f.append(i)

print(lst_f)

### Solution 2:

lst_d = ['hello', 'adfFSf', 'bob', 'AnnA', 'hello', 'k', '23453', 'k', 'hh', 'opppo', 'KKlado', 'hh']
lst_f = []

[lst_f.append(i) for i in lst_d if i not in lst_f]
print(lst_f)





# 4. Create a list from 5 user inputs.
# Ստեղծել լիստ 5 ներմուծված թվերից


print('-' * 100)
print('Ex.4')


inp = []

for _ in range(0, 5):
    val = int(input('next value:'))
    inp.append(val)

print(inp)




# 5. Write a program to print the given list after removing the 2nd, 4th and 5th elements.
# Գրել ծրագիր, որը կջնջի տրված լիստի 2-րդ, 4-րդ և 5-րդ էլեմենտները։

print('-' * 100)
print('Ex.5')

lst = ['Rock', 'Pop', 'Metal','Hip-Hop', 'Rap']

### Solution 1:

for i, j in enumerate(lst.copy()):
    if i == 1 or i == 3 or i == 4:
        lst.remove(j)
print(lst)

### Solution 2:

lst = ['Rock', 'Pop', 'Metal','Hip-Hop', 'Rap']

lst.pop(4)
lst.pop(3)
lst.pop(1)
print(lst)



# 6. Given a list of ints, print True if the array contains a 2 next to a 2 somewhere.
# Գրել ծրագիր, որը կտպի True, եթե տրված լիստում ինչ-որ տեղ 2 թվին 2 է հաջորդում։

print('-' * 100)
print('Ex.6')


a = [12, 2, 2, 243422, 56, 2, 6, 5, 19, 1, 1]

### Solution 1:


for i in range(len(a)- 1):
    if a[i:i+2]  == [2, 2]:
        print(True)
        break


### Solution 2:


a = [12, 2, 5, 243422, 56, 2, 2, 5, 19, 1, 1]
for i, _ in enumerate(a):
    if i < len(a) - 1 and a[i] == a[i + 1] == 2:
        print(True)





# 7. Given a list of ints, print True if every element is a 1 or a 4, and False otherwise.
# Գրել ծրագիր, որը կտպի True, եթե լիստի բոլոր էլեմենտները 1 կամ 4 են։ Հակառակ դեպքում տպել False:

print('-' * 100)
print('Ex.7')


b = [4, 1, 4, 4, 1, 1, 4, 1, 4, ]

bs = set(b)

for i in bs:
    if bs == {1, 4}:
        print(True)
        break
    else:
        print(False)



# b = [4, 2, 4, 4, 2, 2, 4, 2, 4]
# check = [2, 4]
# bl = []
#
# for i in b:
#     if i  not in bl:
#         bl.append(i)
#
#
# bl.sort()
# check.sort()
#  if bl = check
#     print(True)




# 8. Ask for user input and add that input as a key into the dictionary. If the key exists, warn the user about it and
# do nothing. Assign some arbitrary value to it.
# Պահանջել ներմուծել բանալի և ավելացնել այդ բանալին dictionary-ի։ Եթե այն արդեն գոյություն ունի, տպել, որ բանալին արդեն
# կա և ոչինչ չանել։ Որպես արժեք տեղադրել պատահական օբյեկտ

print('-' * 100)
print('Ex.8')









# 9. Loop through the values of a dictionary and add them to a new list.
# Ցիկլի միջոցով ավելացնել dictionary—ի արժեքները նոր լիստի մեջ։

print('-' * 100)
print('Ex.9')

dictx = {i: i ** 2 for i in range(1, 16)}
lstx = [i for i in dictx.values()]
print(lstx)

### OR

lstx = []
for i in dictx.values():
    lstx.append(i)
print(lstx)


# 10. Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# Գրել ծրագիր, որը կստեղծի և կտպի dictionary, որի բանալիները [1,15] թվերն են, իսկ արժեքները դրանց քառակուսիները։

print('-' * 100)
print('Ex.10')



dict1 = {i: i ** 2 for i in range(1,16)}
print(dict1)

### OR

dict_2 = {}

for i in range(1, 16):
    dict_2[i] = i ** 2
print(dict_2)
