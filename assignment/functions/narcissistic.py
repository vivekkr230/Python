def main():
    while 1==1:
        x=int(input("Enter the number: "))
        if x<0:
            break
        else:
            narcissist(x)


def narcissist(y):
    z=str(y)
    sum=0
    w=len(str(y))
    print("The count of digit is",w)
    for i in z:
        sum=sum+(int(i)**w)

    if sum == y:
        print(y,"is a narsissist")

    else:
        print(y,"is not a narsissit")

main()