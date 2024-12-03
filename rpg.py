import random

def game():
    print(" Welcome player")
    player_health = 50
    monster_health = 50

    while player_health > 0 and monster_health > 0:
        action=input("Choose 'attack' or 'heal'.\n")
        if action == "attack":
            damage_dealt = random.randint(5, 8)
            monster_health -= damage_dealt
            print(f"You attacked and dealt {damage_dealt} damage.")
        elif action == "heal":
            heal= random.randint(5, 12)
            player_health += heal
            print(f"You healed yourself for {heal} hp.")
        else:
            print("Invaild choice, Choose 'attack' or 'heal'.")

    

        if monster_health > 0:
            damage_dealt = random.randint(4, 11)
            player_health -= damage_dealt
            print(f"Monster attacked you and dealt {damage_dealt} damage")
            #health indicator after each attack 
            print(f"your health {player_health} | monster health {monster_health}")


    if player_health < 0:
        print("You lost")
    else:
        print("You won")




game()