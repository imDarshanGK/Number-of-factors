n=int(input("Enter a number:"))
c=0
print('factors are')
for i in range(1,n+1):
    if n%i==0:
        print(i)
        c=c+1
print("Number of factors=",c)
