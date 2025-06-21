str1=input("Enter first string")
str2=input("Enter second string")
concat = str1+" "+str2

print(f"Concatenated String : {concat}")

print("---- String Methods Applied ----")

print(f"Uppercase      : {concat.upper()}")
print(f"Lowercase      : {concat.lower()}")
print(f"Title Case     : {concat.title()}")
print(f"Swap Case      : {concat.swapcase()}")
print(f"Is Alpha Only  : {concat.isalpha()}")
print(f"Is Digit Only  : {concat.isdigit()}")
print(f"Starts with 'a': {concat.startswith('a')}")
print(f"Ends with 'z'  : {concat.endswith('z')}")
print(f"Count of 'a'   : {concat.count('a')}")
print(f"First index of 'a': {concat.find('a')}")
print(f"Reversed       : {concat[::-1]}")
a="RiyaG"
b="12345"
encode=concat.maketrans(a,b)
print(f"Encoding : {concat.translate(encode)}")
