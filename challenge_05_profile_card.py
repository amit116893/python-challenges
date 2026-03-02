name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))
favouritenumber = int(input("Enter your favourite number: "))

height_cm = int(height_m * 100)

print("\n================================")

print("        YOUR PROFILE CARD")

print("================================")

print(f" Name:              {name}")
print(f" Age:               {age} years")
print(f" Height:            {height_m:.2f}m ({height_cm}cm)")
print(f" Favourite Number:  {favourite_number}")
