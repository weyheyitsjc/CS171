import math
def hypotenuse(a,b):
    hyp = math.sqrt((a**2) + (b**2))
    return hyp

#You do not need to make changes below this line.
if __name__=="__main__":
    print("Hypotenus Example")
    a=int(input("Enter Side One:\n"))
    b=int(input("Enter Side Two:\n"))
    
    print("Hypotenuse is %0.4f"%(hypotenuse(a,b)))