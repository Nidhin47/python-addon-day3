def square(x):
    y=[i*i for i in x if i>3 if i<8]
    print(y)
square(input("enter a list:"))