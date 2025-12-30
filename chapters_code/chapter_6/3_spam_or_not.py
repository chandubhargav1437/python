keywords = ["make more money", "click this", "subscribe now", "buy now"]
message = input("enter the message:")
is_spam = False
message = message.lower()
print(message)
for word in keywords:
    word = word.lower()
    if word in message:
        is_spam = True
        break
if is_spam:
    print("yes this message is a spam")
else:
    print("no this message is not a spam")
