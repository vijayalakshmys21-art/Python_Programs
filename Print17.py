num=int(input())
fact=1
for i in range(num,0,-1):
    fact=fact*i
    print(i,end=" ")
    if i !=1:
        print("*",end=" ")
print("=",fact)