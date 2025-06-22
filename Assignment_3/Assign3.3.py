num = int(input("Enter a number to check if it is palindrome : "))
str_num = str(num)

if str_num==str_num[::-1]:
    print(f"{num} is palindrome")
else:
    print(F"{num} is not palindrome")