num = int(input("enter the number tocheck the factoria"))


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)


def factt(n):
    sum = 1
    for i in range(1, n+1):
        if n == 0 or n == 1:
            sum = sum*1
        sum = sum*i
    return sum


print(fact(num))
print(factt(num))
