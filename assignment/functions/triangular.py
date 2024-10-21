import math

def triangular(n):
    m=1+(8*n)
    s=math.sqrt(m)
    if s*s == m:
        
        z=(-1+s)/2
        if z>0:
            print(n,"is a triangular number")
        else :
            print(z,"is less than zero so it can not be a triangular number")

    else:
        print(s,"is not a perfect square so it can not be a triangular number")


def main():
    while 1==1:
        x=int(input("Enter the value: "))
        if x == -1:
            break
        else:
            triangular(x)  
main()