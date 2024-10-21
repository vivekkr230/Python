def prime(x):
    for i in range(1,x+1):
        if i==1 or i==x:
            continue
        else:
            if x%i==0:
                print(x,"is not a prime number")
                break
            else:
                if i==x-1:
                    print(x,"is prime number")
                else:
                    continue

prime(7)    