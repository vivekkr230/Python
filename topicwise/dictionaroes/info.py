vivek={
    "name":"Vivek",
    "attendence":[True,True,True,True,True],
    "grade":[100,80,87,76,95]
}
# for v in vivek:
#     print("key",v)

# for key,value in vivek:
#     print(key,value)  wrong statement

v=vivek.items()
for key,value in v:
    print(key,":",value)


suku={
    "name":"Suku",
    "attendence":[True,False,True,False,False],
    "grade":[100,80,87,76,95]
}

satyam={
    "name":"Satyam",
    "attendence":[True,True,True,False,True],
    "grade":[100,80,87,76,95]
}


students={"1":vivek,"2":suku,"3":satyam}

#print the number of total students

print(len(students))

#print all the key values

print(students.keys())

#get the attendece of vivek

vivek=students['1']

print(vivek['attendence'])


#get the grade of suku
suku=students.get('2')

print(suku.get('grade'))


#iterate through dictionaries

for k in students:
    print("key",k)


#average of all grades
#1st calculate satyam average
l1=[]
s=satyam.items()
for key,value in s:
    print(f"{key}:{value}")
    if key == "grade":
        for i in value:
            l1.append(i)

#     for g in k['grade']:
#         l1.append(g)
print(l1)
print(f"Average of satyam ")
# Print all keys and values
for key, value in vivek.items():
    print(f"{key}: {value}")

# Calculate the average of grades
grades = vivek["grade"]
average_grade = sum(grades) / len(grades)
print(f"Average grade: {average_grade}")


grades=[]
items=students.items()
for key,val in items:
    print(key,val)
    for g in val['grade']:
        grades.append(g)

print(grades)