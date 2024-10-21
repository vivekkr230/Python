def fun_fac(n):
    if(n==0):
        return 1
    else:
        return (n)*fun_fac(n-1)


print(fun_fac(2))