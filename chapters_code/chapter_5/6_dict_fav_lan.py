my_dic = dict()
print(type(my_dic))
for i in range(4):
    name = input(f"enter the name of {i+1} student")
    lan = input(f"enter the favourite language of {name} ")
    my_dic[name] = lan
for x in my_dic:
    print(f"the fav language of {x} is {my_dic[x]}")
