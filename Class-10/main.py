# Short hand if-else statement / Ternary Operator

num1 = 40
num2 = 40

print("Num2") if num2 > num1 else (print("Num1") if num1 > num2  else print("Both are equal"))

if num2 > num1:
    print("Num2")
elif num1 > num2:
    print("Num1")
else:
    print("Both are equal")
