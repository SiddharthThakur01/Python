number_people = int(input("Enter number of people in group?\n"))
price = 0
all_price = 0  # Initialize all_price outside the loop
for i in range(number_people):
    age = int(input(f"Enter your age for {i+1}?\n"))
    if age <= 12:
        price = int(12)
        print("Kids tickets at $12")
    elif age <= 18:
        price = int(18)
        print("Teens tickets at $18")
    else:
        price = int(24)
        print("Adult tickets at $24")

    total_price = price
    photo = input("Do you want photo taken (y/n)?\n")
    final_price = int(total_price) + 3 if photo == 'y' else int(total_price)

    all_price += final_price  # Accumulate total price for all members

print(f"Your total bill is = {all_price}")