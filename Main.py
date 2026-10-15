   mark=int(input())
result="Even" 
if num%2==0 
else "Odd":
print(result)


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

   



 






# num=int(input())
# digits=0
# temp=num
# temp1=num 
# while num!=0:
#     rem=num%10
#     digits+=1
#     num=num//10
# sums=0
# while temp!=0:
#     rem=temp!=0:
#     sums=sums+rem**digitstemp=temp//10
# if sums==temp1:
#     print("Amstrong Number")
# else:
#     print ("Not Amstrong Number")

# for i in range(1,21):
#     if i==16:
#         break
#     print(i,end=" ")

# for i in range (1,6):
#     if i==3:
#         continue
#     print(i,end=" ")


# numbers=[10,20,30,40,50]
# names=["Rahul","Pravin","Kumar","Jagan"]
# mixed=[10,2.3,6,"K","Pravin"]
# print(numbers)
# # print(names)
# print(mixed)
# print(numbers[0])
# print(numbers[2])
# print(numbers[1])
# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-5])
# numbers[2]=300
# print(numbers)

# num=[]
# n=int(input())
# for i in range(n):
#     value=int(input())
#     num.append(value)
# print(num)


# arr=[1,2,3,4,5]
# for value in arr:
#     print(value,end=" ")

# print()

# i=0
# while i<len(arr):
#       print(arr[i],end=" ")
#       i+=1

# numbers=[11,12,13,14]
# print(numbers)
# numbers.append(15)
# numbers.append(16)
# print(numbers)
# numbers.insert(0,100)
# print(numbers)
# nums=[10,20,10,10]
# nums.remove(10)  #remove first matching element
# print(nums)
# nums.pop() #remove last element
# print(nums)
# nums.append(60)
# nums.append(70)
# nums.append(80)
# print(nums)
# nums.clear()
# print(nums)

#list slicing
# arr=[10,20,30,40,50,60,]    #list[start:stop:step]
# print(arr[1:5])
# print(arr[:3])
# print(arr[3:])
# print(arr[::2])

# arr1=[10,20,30,20,50]
# print(30 in arr1)
# print(90 in arr1)
# print(arr1.index(20))
# print(arr1.count(20))
# print(arr1.count(90))

#sort
# arr2=[10,20,30,200,40]
# arr2.sort()
# print(arr2)
# arr2.sort(reverse=True)
# print(arr2)

# arr3=[10,30,50,200,40]
# arr3.reverse()
# print(arr3)

# arr4=[10,30,50,200,40]
# print(len(arr4))
# print(sum(arr4))
# print(min(arr4))
# print(max(arr4))

# nums=[]
# pos=neg=zero=0
# n=int(input())
# for i in range(n):
#     value=int(input())
#     nums.append(value)
# for value in nums:
#     if value < 0:
#         neg+=1
#     elif value > 0:
#         pos+=1
#     else:
#         zero+=1
# print("list value: ",nums)
# print("Pos count: ",pos)
# print("Neg count: ",neg)
# print("Zeros count: ",zero)

#tuple ordered , immutable allow duplcates
# numbers=(10,20,30,40)
# print(numbers)
# print(type(numbers))
# arr=(5,)
# print(type(arr))
# print(numbers[2])
# print(numbers[-1])
# print(numbers[1:4])

# for values in numbers:
#     print(values,end=" ")
# print()
# arr2=(10,20,30,20)
# print(arr2.count(20))
# print(arr2.index(30))
# print(len(arr2))
# print(sum(arr2))
# print(min(arr2))
# print(max(arr2))

# marks=(85,35,60,28,90,40)
# pass_count=fail_count=0
# for values in marks:
#     if values>=40:
#         pass_count+=1
#     else:
#         fail_count+=1
# print("passed students: ",pass_count)
# print("failed students: ",fail_count)


#unordered
# numbers={45,67,89,90}
# print(numbers)
# names={"rahul","pravin","kumar"}
# print(names)
# empty_set=set()
# empty_set={4,5,6}
# print(empty_set)
# nums={10,20,30,20,30,10}
# print(nums)
# print(len(nums))

# list_1=[10,20,30,20,30,50,10]
# unique_set=set(list_1)
# print(unique_set)

# nums_1={10,20,30}
# nums_1.add(40)
# print(nums_1)
# num_1.update([50,60,70])
# print(nums_1)
# nums_1.remove(50)
# print(nums_1)
# #nums_1.remove(150)
# #print(nums_1)

# a={1,2,3}
# b={3,4,5}
# print()
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# a={10,20}
# b={10,20,30,40}
# c={50,60}
# print()
# print(a.issubset(b))
# print(a.issuperset(a))
# print(a.isdisjoint(b))
# print(a.isdisjoint(c))

# student_1={
#     "name":"Pravin",
#     "age":22,
#     "mark":360,
#     "departmet":"IT"
# }
# print(student_1)
# print(student_1["name"])
# print(student_1['mark'])
# #print(student_1['city])
# print(student_1.get("age"))
# print(student_1.get("city","Not Availabe"))
# student_1["mark"]=360
# print(student_1)
# student_1["city"]="Pondy"
# print(student_1)
# student_1.pop("age")
# print(student_1)

# for key,value in student_1.items():
#     print(key," : ",value)

# student_1={
#     "name":"keyboard",
#     "price":500,
#     "stock":10
# }
# print(student_1)
# print(student_1["name"])
# print(student_1['price'])
# #print(student_1["brand"])
# print(student_1.get("age"))
# print(student_1.get("brand :","Not Availabe"))
# student_1["price"]=500+150
# print(student_1)
# student_1["brand"]="Logitech"
# print(student_1)
# student_1.pop("stock")
# print(student_1)

# for key,value in student_1.items():
#     print(key," : ",value)

 #immutable collection of chara
# name="Arun" 
# course='python'
# print(name)
# print(course)
# print(type(name))
# print(type(course))
# print(course[0])
# print(course[1])
# print(course[-1])
# print(course[0:3])
# print(course[2:])
# print(course[0:4])
# print(course[::-1])

# text="Python"
# text="J"+text[1:]
# print(text)

# print(len(text))

# for value in text:
#     print(value,end=" ")
# print()
# text_1="Hello Python"
# print(text_1.upper())
# print(text_1.lower())
# print(text_1.replace("Python","Java"))
# print(text_1)
# print(text_1.count('O'))
# print(text_1.find("Python"))
# print(text_1.find("Java"))
# print(text_1.startswith("Hello"))
# print(text_1.endswith("Python"))

# text_2="                    Mogana Pravin                  "
# print(text_2.strip())

# text_3="C C++ Jave Python"
# print(text_3)
# courses=text_3.split()
# print(courses)

# text_4=["C","C++ ","Jave", "Python"]
# text_5=",".join(text_4)
# print(text_5)

# word=input("Enter th word: ").lower()
# if word=word[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# def greet():
#     print("Grest morning pravin")

# def addition(a,b):
#     print(a+b)

# def multiplication(a,b):
#     return a*b

# greet()
# greet()

# addition(3,4)
# addition(10,20)
# result=multiplication(8,9)
# print(result)

# def greet():
#     print("Good morning pravin")

# def addition(a,b):
#     print(a+b)

# def square(a):
#     return a*6

# greet()
# greet()

# addition(10,20)
# result=square(6)
# print(result)

# def show():
#     message="Hello"
#     print(message)
# show

# text="Pravin"
# def greet():
#     print("Hello ",text)

# greet()
# print("hi ",text)

#Lambda function - A lambda function is a small anonymous function contiaing
# a single expression
#syntax lambda arguments:expression


# square=lambda n:n*n 
# n=int(input())
# result=square(n)
# print(result)

# addition=lambda a,b:a+b
# total=addition(4,5)
# print(total)

# def factorial(num):
#     if num==1:
#         return 1
#     return num*factorial(num-1)

# num=int(input("Enter a number: "))
# result=factorial(num)
# print(result)


#polymorphism many forms
#method overriding
# class Phone:
#     def camera (self):
#         print ("taking a normal photo")
# class smartphone(Phone):
#     def camera(self):
#         print("taking a portrait photo")
# mi=smartphone()
# mi.camera()
# nokia=Phone()
# nokia.camera()


# #encapsulation
# class Phone:
#     __battery="30%"
#     def printbattery(self):
#         print(self.__battery)
# iphone15=Phone()
# iphone15.printbattery()


#Time and space complexity 
#Time complexity describes how the number of operatrions an algorithm
#perfoms grows as its input size increases
#it measures growth rather than the exact running time un second
names=["Pravin","kumar","arun","sethu"]
print(names[2])
print(names[3])
#linera time - O (n)
n=100
for i in range (n):


#Spce comlexity describes how the memory required by an algorithm grows
#as its input size increases.
# #input
# #o(1) -constant spce 
# listone=[4,6,7,83,9,0,3,5,6]
# total=0
# for value in listone:
#     total+=value
# print(total)#linera spce -O(n)
# listtwo=[1,2,3,4]
# temp=[]
# for values in listtwo:
#     temp=[]
# for values in listtwi:
#     temp.append(values*values)
# print(temp)


# n=int(input())
# listone=[]
# for i in range (n):
#     data=int(input())
#     listone.append(data)
# left=0
# right=len(listone)-1
# while leftorright:
#     temp=listone[left]
#     listobe[left]=lestone[right]
#     listone[right]=temp
# ]   left+=1
#     right-=1
# print(listone)

# a=10
# b=20
# print(a,"",b)
# c=a
# a=b
# b=c
# print(a,"",b)
# #without using third varibale
# c=10
# d=20
# print(c,"",d)
# c=c+d
# d=c-d
# c=c-d
# print(c,"",d)


#sorting algo and searching algo
#bubble sort
# listone=[5,1,4,2,8]
# for i in range(len(listone)-1)
#     for j in range(len(listone)-1-i)
#         if listone[j]>listone[j+1]:
#             temp=listone[j]
#             listone[j]=listone[j+1]
#             listone[j+1]=temp
# print(listone)

#linera search
listtwo=[5,1,4,2,8]
find=2
found=False
for i in range(len(listtwo)):
    if listtwo[i]==find:
        break
if found:
    print ("Found")
else:
    print("Not Found")