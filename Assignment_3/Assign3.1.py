#Set
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
fruits.discard("banana")
# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)


# Dictionary
inventory = {
    "pen": (10, 100),
    "notebook": (40, 50),
    "eraser": (5, 200),
    "scale": (15, 80)
}

print("Inventory:")
for item, (price, qty) in inventory.items():
    print(f"{item.title()}: {price}, Quantity: {qty}")

# Calculate total value of stock
total_value = 0
for price, qty in inventory.values():
    total_value += price * qty

print(f"Total stock value: ₹{total_value}")

#Tuple
my_tuple = ("apple", "banana", "cherry")
print("Original tuple:", my_tuple)

print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])

# Looping through a tuple
print("Items in the tuple:")
for item in my_tuple:
    print(item)

print("Number of items:", len(my_tuple))
