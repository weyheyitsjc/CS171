print("Fractal Generator")

def fractal(length, spaces):
    if length == 1:
        print(spaces * " " + "*")
    else:
        return fractal(length // 2, spaces), print(" " * spaces + "*" * length), fractal(length // 2, spaces + (length//2))
        

while True:
    try:
        number = int(input("Enter an integer > 0:\n"))
        if number > 0:
            fractal(number, 0)
            break
        else:
            continue
    except:
        continue
