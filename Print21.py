num=int(input())
digits=0
temp=num
temp1=num 
while num!=0:
    rem=num%10
    digits+=1
    num=num//10
sums=0
while temp!=0:
    rem=temp!=0
    sums=sums+rem**digitstemp=temp//10
if sums==temp1:
    print("Amstrong Number")
else:
    print ("Not Amstrong Number")

for i in range(1,21):
    if i==16:
        break
    print(i,end=" ")

for i in range (1,6):
    if i==3:
        continue
    print(i,end=" ")