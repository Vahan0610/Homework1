"""FUNCTIONS"""

from random import randint

# 1. We'll say that an element in an array is "alone" if there are values before and after it, and those values are
# different from it. Return a version of the given array where every instance of the given value which is alone is
# replaced by whichever value to its left or right is larger.


print('-' * 100)
print('Ex.1')


def not_alone(ls: list) -> list:
    for i in range(1, len(ls) - 1):
        right = ls[i + 1]
        left = ls[i + -1]
        if ls[i] != left and ls[i] != right:
            ls[i] = left if left > right else right

    return ls

ls = [4, 4, 1, 3, 3, 2, 2, 1, 5, 5, 6, 7]

assert not_alone(ls) == [4, 4, 4, 3, 3, 2, 2, 5, 5, 5, 7, 7], 'Somethin\'s wrong'





# 2. Write a function to create and print a list where the values are square of numbers between 1 and 30
# (both included).


print('-' * 100)
print('Ex.2')


def lt(sq: range) -> list:
    lst = []
    for element in sq:
        element **= 2
        lst.append(element)
    return lst

print(lt(range(1, 31)))




# 3. Write a function which will take one argument n. Return a list of size n, that will contain random numbers
# from (-100, 400).

print('-' * 100)
print('Ex.3')


def x(n: int) -> list:
    lst = []
    for _ in range(n):
        lst.append(randint(-100, 400))
    return lst

print(x(3))




# 4. Write a function, that will take a list as an argument and return all the words in the list that start with a
# vowel.
print('-' * 100)
print('Ex.4')

poem = '''All that is gold does not glitter,
Not all those who wander are lost;
The old that is strong does not wither,
Deep roots are not reached by the frost.

From the ashes a fire shall be woken,
A light from the shadows shall spring;
Renewed shall be blade that was broken,
The crownless again shall be king.'''




poem = poem.replace('.', '').replace(',', '').replace(';', '')


def x(n: list) -> list:
    new = []
    vowel = 'aeiou'
    for i in (n):
       if i[0].lower() in vowel:
            new.append(i)
    return new

print(x(poem.split()))





# 5. We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Write a function to return the number of small bars to use, assuming we always use big bars before small bars. Return
# -1 if it can't be done.

print('-' * 100)
print('Ex.5')

goal = 7
small = 3
big = 2

def mc(small, big, goal):
    if goal >= big * 5:
        rem = goal - big * 5
    else:
        rem = goal % 5

    if rem <= small:
        return rem

    return -1

print(mc(3, 1, 9))



# 6. Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other
# is "far", differing from both other values by 2 or more.


print('-' * 100)
print('Ex.6')


def x(a: int, b: int, c: int) -> bool:
    if (abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2) or\
            (abs(a - b) >= 2 and abs(a - c) <= 1 and abs(b - c) >= 2):
        return True
    return False

print(x(2, 3, 10))




# 7. Write a function that gets a numerical list as an argument. Find the sum of the elements. If a certain element is
# 13 stop the count and return whatever was the sum before that.

print('-' * 100)
print('Ex.7')

example_list = [4, 1, 2253, 32, 13, 64, 1, 90]


def f(x: list) -> int:
    total = 0
    for e in x:
        if e == 13:
            break
        total += e

    return total

print(f(example_list))





# 8. Write down the following functions in a lambda form

print('-' * 100)
print('Ex.8')



def square(x):
    return x ** 2

sq = lambda x: x ** 2



def circle_area(r, pi=3.14):
    return pi * r ** 2

ca = lambda r, pi=3.14: pi * r ** 2




def sum_to_power(x, y, p):
    return (x + y) ** p

stp = lambda x, y, p: (x + y) ** 2




# 9. Create a list from 1-100. Using the filter function, return a new list containing only the numbers ending with 7.

print('-' * 100)
print('Ex.9')


lst = [i for i in range(1, 101)]

not_sevan = list(filter(lambda x: x % 10 == 7, lst))

print(not_sevan)


# 10. Create a function that will take a string as an argument. Return a new string which is the original string with
# each letter doubled. For example 'cat' will become 'ccaatt'


print('-' * 100)
print('Ex.10')

str1 = 'cat'
lst1 = list(map(lambda x: x * 2, str1))
str2 = ''.join(lst1)
print(str2)

def dc(s: str) -> str:
    str2 = ''
    for char in s:
        str2 += 2 * char

    return str2

str1 = 'cat'
print(dc(str1))
