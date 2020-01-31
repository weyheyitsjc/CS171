item1 = float(input("Cost of first item:"))
item2 = float(input("Cost of second item:"))
user_pay = float(input("Please enter payment:"))

total = item1 + item2

if user_pay < total:
    print("You didn't pay enough. You still owe: $", round(total - user_pay, 2))
else:
    print("Thank you, your change is: $", round(user_pay - total, 2))