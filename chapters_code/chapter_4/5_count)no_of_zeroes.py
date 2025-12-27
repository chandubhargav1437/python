ls = [0, 1, 3, 4, 0, 0, 5, 0, 6, 0]
count = 0
for x in ls:
    if x == 0:
        count += 1
print(f"there are {count} zeroes in the list")
