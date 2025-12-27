marks = []
for i in range(6):
    mark = int(input(f"enter the marks of {i+1} student:"))
    marks.append(mark)
print("before sorting")
for s in marks:
    print(s)
print("\n")
print("after sorting")
marks.sort()
for s in marks:
    print(s)
