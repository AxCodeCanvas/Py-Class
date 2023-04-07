"""
List:

1. Ordered
2. Element access by Index
3. Mutable type data structure
4. Various type data - integer / float / list / others
"""

# Declare - empty

lst = []

print(type(lst))  # <class 'list'>

lst_2 = list()
print(type(lst_2))  # <class 'list'>

# Declare - value

lst_3 = [1, 2, 5.6, "Python", [1, 2, "Java"]]

print(type(lst_3))  # <class 'list'>
print(lst_3)

# Access Element

print(lst_3[4])

print(lst_3[-2])

print(lst_3[1:3])

print(lst_3[4][2])

print(lst_3[2:])

print(lst_3[:4])

# Length

print(len(lst_3))

# Adding

lst_3.append(10)

print(lst_3)

lst_3.insert(0, "C++")
print(lst_3)

lst_4 = [1, 2, 3, 4]

lst_3.extend(lst_4)

print(lst_3)

lst_3.reverse()

print(lst_3)

# Value Update - Mutable

lst_3[0] = "JavaScript"

print(lst_3)

# Remove

lst_3.remove(1)

print(lst_3)

lst_3.pop()
print(lst_3)

# lst_3.remove(1000) # ValueError: list.remove(x): x not in list
# print(lst_3)

lst_3.pop(2)
print(lst_3)

lst_3.pop(0)
# lst_3.pop(100) # IndexError: pop index out of range
print(lst_3)
