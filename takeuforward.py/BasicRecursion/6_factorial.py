n=int(input("Enter the value of n: "))
# fact=1
# def factorial(x):
#     # fact=1
#     global fact
#     if x==1:
#         return 
#     elif x==0:
#         fact=1
#     else:
#         fact=fact*x
#         factorial(x-1)
    # print(fact)
# factorial(n)
# print(fact)


def factorial2(n):
    if n==0 or n==1:
        return 1;
    else:
        return n*factorial2(n-1)


print(factorial2(n))