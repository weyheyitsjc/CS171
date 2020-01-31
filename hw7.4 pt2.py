import math

def bunnies(rabbits, foxes, years):
    A = 0.04
    B = 0.0005
    G = 0.2
    S = 0.00005

    if years <= 0:
        return [rabbits, foxes]
    else:
        nextRabbits = rabbits + math.floor(rabbits * (A - B * foxes));
        nextFoxes = foxes - math.floor(foxes * (G - S * rabbits));
        return bunnies(nextRabbits, nextFoxes, years - 1);

if __name__ == "__main__":
    print("Welcome to Predator-Prey Model.")
    initialRabbit = int(input("Enter Initial Rabbit Population:\n"))
    initialFox = int(input("Enter Initial Fox Population:\n"))
    years = int(input("Enter Number of Years to Simulate:\n"))
    
    info = bunnies(initialRabbit, initialFox, years)
    
    print("After", years, "years there will be", info[0], "rabbits.")
    print("After", years, "years there will be", info[1], "foxes.")