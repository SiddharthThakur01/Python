#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to Tip Calculator\n")
bill = float(input("Enter Total Bill: "))
tip_percent = float(input("Enter Tip Percent: "))
total_person = int(input("Enter Total Person to split the bill in between: "))
total_bill_per_person = (
    (float(bill) + (float(bill) * (float(tip_percent) / 100)))
) / total_person
print(f"Each person should pay: {round(total_bill_per_person, 2)}")
