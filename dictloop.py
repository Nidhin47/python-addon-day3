x=input("enter a list:")
y={}
for i in x:
    if i%2==0:
        y[i]="even"
    else:
        y[i]="odd"
print(y)
