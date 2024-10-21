def divisor(x):
    l1=[]
    for i in range(1,x+1):
        if x%i == 0:
            l1.append(i)
        else:
            continue

    print(l1)





def main():
    
    while 1==1:
        y=int(input("Enter the number: "))
        if y == -1:
            break
        else:
            divisor(y)
    # divisor(y)
main()