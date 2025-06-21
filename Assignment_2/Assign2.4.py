items = []

while True:
    print('''--- Billing Program ---
    1. Create New Bill 
    2. Add Items to Bill
    3. Display Item Prices and total bill amount
    4. Display Total
    5. Exit 
    ''')
    choice = int(input("Enter your choice : "))
    if choice==1:
        items.clear()
        print("New bill created. All previous items cleared.")

    elif choice==2:
        n=int(input("How many items do you want to add? "))
        for i in range(n):
            name=input(f"Enter the name of item {i+1} : ")
            price = float(input(f"Enter price of {name} : "))
            quantity = int(input(f"Enter quantity of {name} : "))
            items.append([name,price,quantity])
        print("Items added successfully")

    elif choice==3:
        if not items:
            print("No items in the bill")
        else:
            print("\n--- Bill Details ---")
            print(f"{'Item':15} {'Price':10} {'Qty':10} {'Subtotal':10}")
            total=0
            for item in items:
                name, price, qty = item
                subtotal = price*qty
                total+= subtotal
                print(f"{name:15} {price:<9} {qty:<10} {subtotal:<10}")
            print(f"\nTotal Bill Amount: {total}")
    elif choice==4:
        total = sum(price*qty for name,price,qty in items)
        print(f"\nTotal Bill Amount: {total}")
    elif choice==5:
        print("Thank you for using the billing system")
        break
    else:
        print("Invalid Choice.")





