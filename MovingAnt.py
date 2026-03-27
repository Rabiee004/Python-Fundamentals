import random


def main():
    counter = 0 
    ant = (0,0)
    food = (-3, 7)
    while counter < 5000:
        ant = move(ant)
        if ant == food:
            print(f"it took {counter} steps")
            break
        else: 
            counter += 1

    
def move(ant):
    new = random.choice([1,-1])
    index = random.choice([0,1])
    ant = list(ant)
    ant[index] += new
    return tuple(ant)

main()