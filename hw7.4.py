import math

def bunnies(rabbits, foxes, years):
    a = 0.04
    b = 0.0005
    g = 0.2
    s = 0.00005
    
    allRabbits = [rabbits]
    allFoxes = [foxes]

    for i in range(1, years + 1):
        buns = allRabbits[i - 1] + math.floor(allRabbits[i - 1] * (a - b * allFoxes[i - 1]))
        allRabbits.append(buns)
        
        fox = allFoxes[i - 1] - math.floor(allFoxes[i - 1] * (g - s * allRabbits[i - 1]))
        allFoxes.append(fox)
        
        endRabbits = allRabbits[-1]
        endFoxes = allFoxes[-1]
    return endRabbits, endFoxes

if __name__ == "__main__":
    print("Welcome to Predator-Prey Model.")
    initialRabbit = int(input("Enter Initial Rabbit Population:\n"))
    initialFox = int(input("Enter Initial Fox Population:\n"))
    years = int(input("Enter Number of Years to Simulate:\n"))
    
    info = bunnies(initialRabbit, initialFox, years)
    print("After", years, "years there will be", info[0], "rabbits.")
    print("After", years, "years there will be", info[1], "foxes.")
    

