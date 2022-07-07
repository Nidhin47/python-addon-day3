def funcdup(path):
    file=open(path).read()
    w=[]
    x=file.split()
    for i in x:
        if i not in w:
            w.append(i)
    z=" ".join(w)
    return(z)

def second(a):
    b=funcdup(a)
    print(b)
second("/home/administrator/nidhin/python/day2/sample.txt")