x="bad"
y={}
c=0
for i in x:
    if i not in y:
        c=1
        y[i]=c
    else:
        c=c+1
        y[i]=c
print(y)