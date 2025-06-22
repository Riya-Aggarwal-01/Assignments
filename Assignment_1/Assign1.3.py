num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
operator = input("Enter any one operator +,-,*,/,% ")
if operator=='+':
    res=num1+num2
elif operator=='-':
    res=num1-num2
elif operator=='*':
    res=num1*num2
elif operator=='/':
    if num2!=0:
        res = num1 / num2
    else:
        res="Error: Cannot divide by 0"
elif operator=='%':
    res=num1%num2
else:
    res="Enter any valid operator"


print(f"Result is : {res}")