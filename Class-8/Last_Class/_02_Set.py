"""
Set:

1. Unordered
2. Unindexed
3. Duplicate not allow

Tuple :

1. Ordered
2. Unchangeable [Immutable]
3. Allow duplicate data

List:

1. Ordered
2. Changeable [Mutable]
3. Allow duplicate data
"""

# my_set = {}

my_set_2 = set("python")

# print(type(my_set))
print(type(my_set_2))
print(my_set_2)

a = {1, 2, 3, 4}
print(type(a))

my_set_2 = {1, 2, 3, 1, 2, 3}
print(my_set_2)

my_set_3 = set("1")
print(my_set_3)
