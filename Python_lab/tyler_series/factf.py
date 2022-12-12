def fact(n,x):
    f1=1
    fact1=1
    for i in range(1,n+1):
        f1=f1*x
        fact1=fact1*i
    return f1,fact1