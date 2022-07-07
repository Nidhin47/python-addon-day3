path="/home/administrator/nidhin/python/day2/sample.txt"
file=open(path).read()
print(file)
y=file.split()
count=0
a=raw_input("enter a word:")
for i in y:
    if i in a:
        count=count+1
print(count)



