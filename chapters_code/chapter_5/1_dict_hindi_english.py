dic = {"nal": "tap", "more": "peacock", "kamal": "lotus"}
st = input("enter the hindi word to check the meaning in english")
answer = ""
for x in dic:
    if (x == st):
        # print("the meaning of ", st, "in english is ", dic[x])
        answer = dic[x]
        break
if answer != "":
    print("the meaning of ", st, "in english is ", answer)
else:
    print("the word is not found in the dictionary")
