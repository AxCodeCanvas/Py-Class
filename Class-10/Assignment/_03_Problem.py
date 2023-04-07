"""
A year may be a leap year if it is evenly divisible by 4. Years that are divisible by 100 (century years such as 1900 or 2000) cannot be leap years unless they are also divisible by 400.


"""

year = int(input())

if year % 400 == 0 or (year % 100 !=0  and year % 4 == 0): # Problem: []
    print("Leap Year")
else:
    print("Is not leap year.")