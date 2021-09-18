"""LOOPS"""

# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։


print('-' * 100)
print('Ex. 1')





# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

print('-' * 100)
print('Ex. 2')

lst = []

for i in range(0, 3):
  lst.append([])
  # print(f'iteration: {i}', 'list: ', lst)
  lst[i] = [j ** 2 for j in range(1, 10)]


print(lst)






# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։

print('-' * 100)
print('Ex. 4')

nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
count = 0
for i in nonsense:
    if i == "b":
        count += 1

print(count)




# 5. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։

print('-' * 100)
print('Ex. 5')

n = int(input("your number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)