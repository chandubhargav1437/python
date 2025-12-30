li = list()
print(type(li))
n = int(input("enter the number of names:"))
for i in range(n):
    name = input(f"enter the {i+1}th name:")
    li.append(name)
for i in li:
    if (i[0] == 's'):
        print(f"hello {i}")
else:
    print("completed for every one")
