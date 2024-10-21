n=int(input("Enter the value of n: "))
x=1
def printnto1():
    global n
    while n!=x-1:
        print(f"{n}")
        n=n-1
        printnto1()

printnto1()