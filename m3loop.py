n=input("enter a number:")
y=range(1,n+1)
z=[(i,j,h) for i in y for j in y for h in y if i!=j if i!=h if j!=h]
print(z)