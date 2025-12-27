number = int(input("enter the number of fruits to store "))
fruits = []
for i in range(number):
    fr = input(f"enter the {i+1} th fruit name to add in the list")
    fruits.append(fr)
print(fruits)
print(type(fruits))
for x in fruits:
    print(x)
