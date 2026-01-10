num = int(input("enter the number to print pattern"))
temp = ""
for i in range(1, num+1):
    inn = 1
    last = num
    if i == inn or i == last:
        for j in range(1, num+1):
            # print("*")
            temp += "*"
        # print("\n")
    else:
        for j in range(1, num+1):
            if j == inn or j == last:
                # print("*")
                temp += "*"
            else:
                # print(" ")
                temp += " "
    # print("comp")
    print(temp)
    temp = ""
