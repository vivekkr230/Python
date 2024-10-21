# n1=int(input("Enter the first digit: "))
# n2=int(input("Enter the second digit: "))

# def hcfofgivennumber(x1,x2):
#     hcf=0
#     for i in range(1,min(x1,x2)+1):
#         if x1%i==0 and x2%i==0:
#             hcf=i


#     return hcf


# print(hcfofgivennumber(n1,n2))
# equilateral algorithm

n1=int(input("Enter the first digit: "))
n2=int(input("Enter the second digit: "))
while n1!=0 or n2!=0:
    x1=max(n1,n2)%min(n1,n2)
    x2=min(n1,n2)
    n1=x1
    n2=x2
    if min(n1,n2)==0:
        print(f"{max(n1,n2)} is gcd")
        break
    else:
        print(n1)
        print(n2)