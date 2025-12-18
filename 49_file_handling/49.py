f = open("myfile.txt", "x")
print(f)

f = open("myfile.txt", "r")
print(f)

f = open("myfile.txt", "r")
text = f.read()
print(text)

f = open("myfile1.txt", "a")
f.write("\nhello i have addded a new content in here in second file")
f.close()

f = open("myfile1.txt", "r")
text = f.read()
print(text)

t = open("cumm.txt", "w")
t.write(text)
t.close()
t = open("cumm.txt", "r")
cumm_text = t.read()
print(cumm_text)
