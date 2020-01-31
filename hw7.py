text = input()
text = list(text)
money = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
n = 0
while n < len(text):
    if text[n] == "$":
        text.pop()[n]
    elif text[n] == ".":
        continue
    else:
        num = money[text[n]]
        text.append[num]
    n += 1
print(text)
