n=input("enter a number:")
y=range(1,n+1)
z=[(i,j) for i in y for j in y if i>j]
print(z)