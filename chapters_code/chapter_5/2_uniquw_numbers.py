li = []
for i in range(8):
    num = int(input(f"enter the  {i+1} number"))
    li.append(num)
for i in li:
    print(i)
ss = set(li)
print("the unique numbers are")
for i in ss:
    print(i)
