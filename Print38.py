for key,value in student_1.items():
    print(key," : ",value)

student_1={
    "name":"keyboard",
    "price":500,
    "stock":10
}
print(student_1)
print(student_1["name"])
print(student_1['price'])
#print(student_1["brand"])
print(student_1.get("age"))
print(student_1.get("brand :","Not Availabe"))
student_1["price"]=500+150
print(student_1)
student_1["brand"]="Logitech"
print(student_1)
student_1.pop("stock")
print(student_1)