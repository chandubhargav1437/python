number = int(input("enter the number to check primality"))
i = 1
li = 0
while i < number:
    if ((number / i - number//i) == 0):
        li += 1
    i += 1
    if li > 1:
        break
if (li == 1):
    print(f"the {number} is a prime number")
else:
    print(f"the {number} is not a prime number")
