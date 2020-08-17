import random 
from time import sleep
from os import system

dif_easy = 10
dif_mid = 30
dif_hard = 60
dif_superH = 100
dif_ultSuperH = 1000

def ran_num(dif):
    global numa 
    global numb
    numa = random.randint(1,dif)
    numb = random.randint(1,dif)

def maingame(dif):
    while True:
        system("cls")
        ran_num(dif)
        print("what is "+ str(numa) + " * " + str(numb))
        sum = numa * numb
        ans = input(">> ")
        if ans == str(sum):
            system("cls")
            print("nice correct")
            sleep(2)
        else:
            system("cls")
            print("wrong it was " + str(sum))
            sleep(2)

def main():
    print("""
    enter the difficulty
    easy 
    meddium 
    hard
    superHard
    ultraSuperHard(impossible)
    """)
    inp = input(">> ") 
    if inp == "easy":
        maingame(dif_easy)
    elif inp == "middium":
        maingame(dif_mid)
    elif inp == "hard":
        maingame(dif_hard)
    elif inp == "superHard":
        maingame(dif_superH)
    elif inp == "ultraSuperHard":
        maingame(dif_ultSuperH)


if __name__ == "__main__":
    main()