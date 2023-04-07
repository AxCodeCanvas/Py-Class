"""
5.1234567





lst = [1, 2, 3, 4, 5]
lst2 = [10, 20, 30, 40, 50]

lst2.extend(lst)
print(lst2)

lst.extend(lst2)  # [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
print(lst)
"""

num1 = 85
num2 = 85 * 2
num3 = 85 * 3

print(id(num1))  # 1854405545296
print(id(num2))  # 1854405548496
print(id(num3))  # 1854406580496

print(num1 * 3 is num3) # False
print(num1 * 2 is num2) # True

print(num1 * 3 == num3)

lst = [10, 20, [30, 40]]

lst[2][0] = 50

print(lst)