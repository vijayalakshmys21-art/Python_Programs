temp=float(input("Enter temperature: "))
if temp<20:
    print("Cold")
elif temp>=20 and temp<30:
   print("Pleasant")
elif temp>=30 and temp<40:
    print("Hot")
elif temp>=40:
    print("Very hot")