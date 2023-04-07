# "" / ''
language = "Python"
language2 = 'Java'

# Data type Check
print(type(language))  # <class 'str'>
print(type(language2))  # <class 'str'>

num = "10"
print(type(num))  # <class 'str'>

# Value Access || Intial Index -> 0
# "0->P 1->y 2->t 3->h 4->o 5->n"

print(language[0])  # P
print(language[4])  # o
# print(language[10]) # IndexError: string index out of range
print(language[-1])  # n
print(language[-3])  # h
print(language[2:4])  # [start : end-1] # th
print(language[2:8])  # [start : end-1] # thon
print(language[2:])  # thon
print(language[:6])  # Python
print(language[-5:-2])  # yth # [-5 : -2-1] # [-5 : -3]
print(language[-0])
