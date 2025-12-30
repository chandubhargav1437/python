n = int(input("enter the number of marks to be stores"))
marks = []
for i in range(n):
    mark = int(input(f"enter the marks of {i+1} student:"))
    marks.append(mark)
marks.sort()
greatest_mark = marks[-1]
print(f"the gretest marks is {greatest_mark}")
