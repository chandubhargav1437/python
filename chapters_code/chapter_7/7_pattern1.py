num = int(input("enter the number to print pattern"))
ans = ""
for i in range(1, num+1):
    curr = ""
    for j in range(1, i+i-1+1):
        curr += "*"
    # print(curr)
    toadd = ""
    for m in range(1, num-i+1):
        toadd += " "
    ans += toadd
    ans += curr
    ans += toadd
    print(ans)
    # print("\n")
    ans = ""
# num = int(input("Enter the number to print pattern: "))

# # Loop from 1 to num
# for i in range(1, num + 1):
#     # 1. Calculate spaces: (Total Height - Current Row)
#     spaces = " " * (num - i)

#     # 2. Calculate stars: (2 * Current Row - 1)
#     stars = "*" * (2 * i - 1)

#     # 3. Print combined string
#     print(spaces + stars)
