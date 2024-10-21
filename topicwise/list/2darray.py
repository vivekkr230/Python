l1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(len(l1))
for row in l1:
    print(row)

print(l1[1][2])

l1[2][1]=100


print("Updated Matrix is:")
for row in l1:
    print(row)