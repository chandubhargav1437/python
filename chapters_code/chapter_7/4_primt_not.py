number = int(input("enter the number to check primality"))
i = 1
li = list()
while i < number:
    if ((number / i - number//i) == 0):
        li.append(i)
    i += 1
if (len(li) == 1):
    print(f"the {number} is a prime number")
else:
    print(f"the {number} is not a prime number")
