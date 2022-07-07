def square(x):
    y=[i*i for i in x if (i%2==1)]
    print(y)
square(input("enter a list:"))