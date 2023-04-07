# 3. Write a Python program to check whether a number is divisible by 5 and 50 or not.

num = int(input())

if num % 5 == 0 and num % 50 == 0:
    print("Divisible by 5 and 50")
else:
    print("Not Divisible by 5 and 50")
