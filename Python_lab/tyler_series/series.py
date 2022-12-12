import factf
n= int(input("Enter n value"))
s=1
x= int(input("input x value"))
for i in range(1,n+1):
    r1,r2=factf.fact(i,x)
    s=s+(r1/r2)
print("sum is",s)