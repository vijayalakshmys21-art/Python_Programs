nums=[]
pos=neg=zero=0
n=int(input())
for i in range(n):
    value=int(input())
    nums.append(value)
for value in nums:
    if value < 0:
        neg+=1
    elif value > 0:
        pos+=1
    else:
        zero+=1
print("list value: ",nums)
print("Pos count: ",pos)
print("Neg count: ",neg)
print("Zeros count: ",zero)