# b=int(input("Enter the binary digit: "))
# l1=[]
# l2=[]
# while b!=0:
#     rem=b%2
#     b=b/2
#     l1.append(rem)
# print(l1)

# # for i in range(len(l1)-1,0):
# #     l2.append(l1[i])

# for i in range(len(l1) - 1, -1, -1):
#     l2.append(l1[i])

# print(l2)

# l3=",".join(l2)
# print(l3)

b = int(input("Enter a decimal number: "))  # If binary input is needed, you can input it as a string and convert
l1 = []
l2 = []

# Converting decimal number to binary
while b != 0:
    rem = b % 2
    b = b // 2
    l1.append(rem)
print(l1)

# Reversing the binary digits
for i in range(len(l1) - 1, -1, -1):
    l2.append(l1[i])
print(l2)

# Convert each integer in l2 to a string before joining
l3 = "".join(map(str, l2))
result=int(l3)
print(result)
