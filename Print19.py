num=int(input())
digits=0
total=0
while num!=0:
    rem=num%10
    digits+=1
    total+=rem
    num=num//10
print("No of digits: ",digits)
print("Sum of digits: ",total)