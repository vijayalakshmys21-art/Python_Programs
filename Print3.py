intial_balance=float(input("enter intial balance: "))
deposit_amount=float(input("enter deposit amount: "))
intial_balance+=deposit_amount
expense_amount=float(input("enter expense amount: "))
intial_balance-=expense_amount
print("final balance: ",intial_balance)