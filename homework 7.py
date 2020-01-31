text = input()
text = text.lstrip("$")
text = text.replace(",", "")
stuff = len(text)
money = 0
if text.find(".") == 1:
    for x in range(0, stuff):
        num = ord(text[x]) - 48
        if x > (stuff-3):
            money += num / 10**(x-(stuff-3))
        elif x < (stuff-3):
            money += num * 10**(-x+(stuff-4))
else:
    for x in range(0, stuff):
        money += (ord(text[x]) - 48) * 10**(-x +(stuff-1))
#print(round(money, 2))
print(money)
