path="/home/administrator/nidhin/python/day2/sample.txt"
file=open(path).read()
y=file.split()
z=[]
f=" ".join(y)
for i in y:
    if i not in z:
        z.append(i)
g=" ".join(z)
print(g)