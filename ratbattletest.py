import time, random, sys

hp = 10
rathp = 5

def rcattack(): #Character attack when fighting rat
    global rathp
    playerdmg = random.randrange(10)
    print(player_name, "strikes the creature with", playerdmg,"damage.")
    rathp -= playerdmg
    time.sleep(1)
    print("Rat HP -", rathp)
    time.sleep(2)



def ratattack():
    global hp
    ratdmg = random.randrange(6)
    print("The rat strikes you with", ratdmg, "damage.")
    hp -= ratdmg
    time.sleep(1)
    print("Your HP -", hp)
    time.sleep(2)


def battletext(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def ratbattle():
    battletext("""
----------------------------
--------BATTLE START--------
----------------------------
    """)
    time.sleep(3)
    print("Rolling for initiative")
    time.sleep(3)
    initiative = random.randrange(2)
    if initiative == 0:
        print(player_name, "attacks first!")
        time.sleep(1)
        while True:
            rcattack()
            if rathp <= 0:
                print("You have defeated the rat!")
                time.sleep(4)
                break
            ratattack()
            if hp <= 0:
                print("The rat killed you!")
                time.sleep(4)
                gameover()
                exit()



    else:
        print("The rat attacks first!")
        time.sleep(1)
        while True:
            ratattack()
            if hp <= 0:
                print("The rat killed you!")
                time.sleep(4)
                gameover()
                exit()
            rcattack()
            if rathp <= 0:
                print("You have defeated the rat!")
                input()
                break
def gameover():
    print()
    print()
    print()
    time.sleep(1)
    print("   _____              __  __   ______      ____   __      __  ______   _____  ")
    print("  / ____|     /\     |  \/  | |  ____|    / __ \  \ \    / / |  ____| |  __ \ ")
    time.sleep(0.5)
    print(" | |  __     /  \    | \  / | | |__      | |  | |  \ \  / /  | |__    | |__) |")
    print(" | | |_ |   / /\ \   | |\/| | |  __|     | |  | |   \ \/ /   |  __|   |  _  / ")
    time.sleep(0.5)
    print(" | |__| |  / ____ \  | |  | | | |____    | |__| |    \  /    | |____  | | \ \ ")
    print("  \_____| /_/    \_\ |_|  |_| |______|    \____/      \/     |______| |_|  \_\ ")
    print()
    input("Press ENTER to exit")
    exit()
player_name = input("Enter your name: ")
input("Press enter to begin the battle")
ratbattle()

battletext("""
----------------------------
---------BATTLE END---------
----------------------------
    """)
input()
