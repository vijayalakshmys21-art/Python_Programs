student_1={
    "name":"Pravin",
    "age":22,
    "mark":360,
    "departmet":"IT"
}
print(student_1)
print(student_1["name"])
print(student_1['mark'])
#print(student_1['city])
print(student_1.get("age"))
print(student_1.get("city","Not Availabe"))
student_1["mark"]=360
print(student_1)
student_1["city"]="Pondy"
print(student_1)
student_1.pop("age")
print(student_1)