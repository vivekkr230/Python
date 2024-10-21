# n=int(input("Enter the the value of n: "))
# def print1ton(x=1):
#     global n
    
#     if x==n+1:
#         return
#     else:
#         print(f"{x}")
#         x=x+1
#         print1ton(x)

# print1ton()


n=int(input("Enter the the value of n: "))
x=1
def print1ton():
    global x
    
    if x==n:
        return
    else:
        print(f"{x}")
        x=x+1
        print1ton()

print1ton()