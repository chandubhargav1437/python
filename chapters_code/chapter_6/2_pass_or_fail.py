n = int(input("enter the number of subjects"))
marks = dict()
print(type(marks))
for i in range(n):
    # marks.update()
    subject = input("enter the subject name")
    mark = int(input(f"enter the marks of {subject}:"))
    marks[subject] = mark
print(marks.items())
individual_marks = marks.values()
isit = False
sum = 0
for mark in individual_marks:
    sum += mark
    if mark < 33:
        isit = True
        print("fail")
        break
if isit != True and sum/n >= 40:
    print("student is pass")
