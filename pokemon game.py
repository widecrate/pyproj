import random

print("Welcome to the budgeted pokemon game")
name = input("What is your name: ")

while True:
    starter = int(input("\nChoose your starter \n 1. Charmander \n 2. Bulbasaur \n 3. Squirtle \n > "))
    confirmation = input("Are you sure (Y/N): ")
    if confirmation == "Y" :
        break
    else:
        False

if starter == 1:
    poke = "Charmander"
elif starter == 2:
    poke = "Bulbasaur"
else:
    poke = "Squirtle"
print(f"{name} has chosen {poke}\n")

route_1_list = ["Pidgey", "Ratata", "Oddish"]

route_1_poke = random.choice(route_1_list)

tall_grass = input("Do you want to walk into the grass? (Y/N): ")
if tall_grass == "Y":
    print(f"\nA WILD {route_1_poke} APPEARED!")
    poke_HP = 100
    route_1_poke_HP = 80
    #Loop to keep prompting to attack till one faints
    while poke_HP > 0 and route_1_poke_HP > 0:
        print(f"----------\n{poke} HP: {poke_HP}\n{route_1_poke} HP: {route_1_poke_HP}\n----------")
        move = int(input("Choose your move:\n1 - Tackle\n2 - Growl\n > "))
        if move == 1:
            poke_damage = random.randint(20,35)
            print(f"\n{poke} used tackle!\nIt dealt {poke_damage} damage!")
            route_1_poke_HP -= poke_damage
        elif move == 2:
            print(f"\n{poke} used growl!\nIt dealt 0 damage!")
        route_1_poke_damage = random.randint(10,15)
        poke_HP -= route_1_poke_damage
        print(f"\n{route_1_poke} used scratch\nIt dealt {route_1_poke_damage} damage!") 
    if route_1_poke_HP <=0 :
        print(f"\n{route_1_poke} fainted \nYou won the battle!")
    else:
        print(f"\n{poke} fainted \nYou lost the battle!")
else:
    print("You're safe")