nums = input("Enter numbers separated by space: ").split()
numbers = []
for i in nums:
    numbers.append(int(i))

smallest = second_smallest=float("inf")
greatest=second_greatest=float("-inf")

for i in numbers:
    if i < smallest:
        second_smallest=smallest
        smallest=i
    elif smallest<i<second_smallest:
        second_smallest=i

    if i>greatest:
        second_greatest=greatest
        greatest=i
    elif greatest > i > second_greatest:
        second_greatest=i


print("\nResults:")
print("Smallest number:", smallest)
print("Second smallest number:", second_smallest if second_smallest != float('inf') else "Not found")
print("Greatest number:", greatest)
print("Second greatest number:", second_greatest if second_greatest != float('-inf') else "Not found")

