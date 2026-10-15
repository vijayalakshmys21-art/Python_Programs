pass_count=fail_count=0
for values in marks:
    if values>=40:
        pass_count+=1
    else:
        fail_count+=1
print("passed students: ",pass_count)
print("failed students: ",fail_count)