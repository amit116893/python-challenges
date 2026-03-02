item1_name = input("Enter name of item 1: ")
item1_price = float(input("Enter price of item 1: "))

item2_name = input("Enter name of item 2: ")
item2_price = float(input("Enter price of item 2: "))

item3_name = input("Enter name of item 3: ")
item3_price = float(input("Enter price of item 3: "))

total = item1_price + item2_price + item3_price

print("\n------ RECEIPT ------")
print(f"{item1_name:<15} ${item1_price:>7.2f}")
print(f"{item2_name:<15} ${item2_price:>7.2f}")
print(f"{item3_name:<15} ${item3_price:>7.2f}")
print("---------------------")
print(f"{'Total':<15} ${total:>7.2f}")
