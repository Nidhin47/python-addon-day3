def sq(x):
    z=[]
    e=abs(x)
    y=range(1,e+1)
    val=[i*i for i in y if (i%2==1)]
    if val not in z:
            z.append(val)
    return(z)

def sec(a):
   b=sq(a)
   print(b)
sec(input("enter a number:"))