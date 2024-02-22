import random
w = random.randint(1,100)
n = int(input("guess a number between 1 to 100 : "))
game_over = True
i = 1 
while  game_over:
    if w == n :
        print(f"you won, you gussed this number in {i} times")
        game_over = False
    elif w < n :
        print("too high")
        i += 1
        n = int(input("again guess a number between 1 to 100 : "))
    elif w > n :
        print("too low")
        i += 1
        n = int(input("again guess a number between 1 to 100 : "))