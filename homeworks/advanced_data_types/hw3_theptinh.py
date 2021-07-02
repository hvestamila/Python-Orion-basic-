# 1. Define the id of next variables:
from typing import Dict

int_a = 55
print("# 1: ", id(int_a))

str_b = 'cursor'
print("# 1: ", id(str_b))

set_c = {1, 2, 3}
print("# 1: ", id(set_c))

lst_d = [1, 2, 3]
print("# 1: ", id(lst_d))

dict_e = {'a': 1, 'b': 2, 'c': 3}
print("# 1: ", id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print('# 2: ', id(lst_d))  # same id (mutable)

# 3. Define the type of each object from step 1.
print('# 3: ', type(int_a))
print('# 3: ', type(str_b))
print('# 3: ', type(set_c))
print('# 3: ', type(lst_d))
print('# 3: ', type(dict_e))

# 4*. Check the type of the objects by using isinstance.
print('# 4: ', isinstance(int_a, int))
print('# 4: ', isinstance(str_b, str))
print('# 4: ', isinstance(set_c, set))
print('# 4: ', isinstance(lst_d, list))
print('# 4: ', isinstance(dict_e, dict))

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
#
# 5. With .format and curly braces {}
print("# 5: Anna has {} apples and {} peaches.".format(4, 5))

# 6. By passing index numbers into the curly braces.
print("# 6: Anna has {1} apples and {0} peaches.".format(5, 4))

# 7. By using keyword arguments into the curly braces.
print("# 7: Anna has {apples_num} apples and {peaches_num} peaches.".format(apples_num=4, peaches_num=5))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("# 8: Anna has {1:5} apples and {0:3} peaches.".format(5, 4))

# 9. With f-strings and variables
apples_num = 4
peaches_num = 5
print(f"# 9: Anna has {apples_num} apples and {peaches_num} peaches.")

# 10. With % operator
print("# 10: Anna has %s apples and %s peaches." % (apples_num, peaches_num))

# 11*. With variable substitutions by name (hint: by using dict)
dict_fruits = {
    "apples": 4,
    "peaches": 5
}
print(f"# 11: Anna has {dict_fruits['apples']} apples and {dict_fruits['peaches']} peaches.")

# Comprehensions:
# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

# (2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

# 12. Convert (1) to list comprehension
loop_to_lst_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
# Check if it has the same result as loop
print('# 12: ', loop_to_lst_comp)

# 13. Convert (2) to regular for with if-else
list_comp_to_loop = []
for num in range(10):
    if num % 2 == 0:
        list_comp_to_loop.append(num // 2)
    else:
        list_comp_to_loop.append(num * 10)

print('# 13: ', list_comp_to_loop)

# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

# (5)
dict_comprehension = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}

# (6)
dict_comprehension = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}

# 14. Convert (3) to dict comprehension.
dict_comp = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print('# 14: ', dict_comp)

# 15*. Convert (4) to dict comprehension.
dict_comp_cond = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print('# 15: ', dict_comp_cond)

# 16. Convert (5) to regular for with if.
dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3

print(dict_comprehension)

# 17*. Convert (6) to regular for with if-else.
dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
    else:
        dict_comprehension[x] = x

print('# 17: ', dict_comprehension)


# Lambda:
#
# (7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y
#
# (8)
foo = lambda x, y, z: z if y < x and x > z else y
#
# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
print(foo(3, 4))

# 19*. Convert (8) to regular function
def foo(x, y, z):
    if y < x and x > z:
        return x
    else:
        return y

print(foo(3, 4, 5))

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
print(sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2


