s=raw_input("enter a string:")
count=0
a=raw_input("enter an alphabet:")
for i in s:
    if i in a:
        count=count+1
        print(count)
    else:
        break
print("alphabet not found")
