#import of random
import random

def run():
    menu = """
    
    Welcome to the GUESS NUMBER GAME (GNG)

    Please select the level of dificult
    1. Easy
    2. Medium
    3. Hard
    4. Impossible

    Level: """
    level_selected = int(input(menu))
    lifes = 0
    
    if(level_selected == 1):
        lifes=10
    elif(level_selected == 2):
        lifes=7
    elif(level_selected == 3):
        lifes=3
    else:
        lifes=1

    chossen_num = int(input("Choose a number between 1 and 100: "))
    random_num = random.randint(1,100)
    i=1

    while i <= lifes:
        if(chossen_num>random_num and i < lifes):
            chossen_num = int(input("Choose a smaller number, you still have "+ str(lifes-i) +" chances: "))
            i += 1
        elif (chossen_num<random_num and i < lifes):
            chossen_num = int(input("Choose a larger number, you still have "+ str(lifes-i) +" chances: "))
            i += 1
        elif (chossen_num==random_num and i < lifes):
            print("You win")
            break
        else:
            print("Nice try, but you lose")
            break
    
if __name__ == '__main__':
    run()