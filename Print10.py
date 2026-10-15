amount=float(input("Enter purchase amount: "))
if amount<0:
    print("Invaild amount")
else:
    discount=0.0
if amount>=5000:
    discount=amount*20/100
elif amount<2000 and amount<5000:
    discount=amount*10/100
print("dicount Amount: ", discount)
print("final Amount: ", amount-discount)