def Calc(numheads,numlegs):
    rabbits = (numlegs - 2* numheads) // 2

    chickens = numheads - rabbits
    return chickens, rabbits

numheads = (int(input("enter number of heads: ")))
numlegs =(int(input("enter number of heads: ")))
chickens , rabbits = Calc(numheads, numlegs)


print(f"chikens: {chickens},Rabbits: {rabbits}")