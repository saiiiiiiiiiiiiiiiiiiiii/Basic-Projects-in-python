# Interactive Text-Based Adventure Game
# Developed an interactive text-based adventure game in Python where players make choices to navigate through various scenarios such as a jungle, a dead city, or a desert. The game uses user input to determine the path and outcome, offering survival-based choices and providing immediate feedback on the player’s decisions. Features include time delays for dramatic effect, handling of invalid inputs, and branching storylines based on player choices.


print("**********************Welcome To The World Globe Throat**************************")
asking_for_How_you_feeling = input("Are You Excited for this (yes/no): ").lower()

if asking_for_How_you_feeling == 'yes':
    print('''It's an adventurous travel game
    called "WGT"''')
else:
    print("No worries, come later!")
    quit()

starting = input("Are You Ready to play the game (yes/no): ").lower()

if starting == 'yes':
    name = input("Enter Your Name: ")
    print(f'''Welcome To The Game "{name}" 
    Now Let's Begin''')
else:
    print('''Better Luck Next time!''')
    print('''Thank you!!''')
    quit()

import time

time.sleep(3)
print('''But Remember!''')
time.sleep(3)
print('''Your Main Aim is Survival!''')
time.sleep(3)
print('''Survival in the Journey!''')
time.sleep(3)

print("Are You Ready :)")
asking = input('(yes/no): ').lower()

if asking == 'yes':
    chose_between_Jungle_Dead_city_Desert = input('''Choose between these 3
    1) Jungle
    2) Dead City
    3) Desert

    What would you like to choose: ''').lower()

    if chose_between_Jungle_Dead_city_Desert == 'jungle':
        chose_Dense_or_Grass = input('''There are Two Kinds Of Jungle 
        1) Dense Forest
        2) Grassland Forest
        
        What would you like to choose: ''').lower()

        if chose_Dense_or_Grass == 'dense forest':
            chose_river_inside_jungle = input('''In this forest you have two choices:
            Either go by river or from inside the jungle
            
            What will you choose: ''').lower()

            if chose_river_inside_jungle == 'go by river':
                print('''Then You will Survive!!
                Good Choice''')
            elif chose_river_inside_jungle == 'inside the jungle':
                print('''You will be Dead.
                You'd better have chosen the 
                go by river option!''')
                print('Better Luck Next time!')
                quit()
            else:
                print("Invalid choice. The game is ending.")
                quit()

        elif chose_Dense_or_Grass == 'grassland forest':
            print('''You chose Grassland Forest.
            You will find it easier to navigate but be cautious of the wildlife!''')
        else:
            print("Invalid choice. The game is ending.")
            quit()

    elif chose_between_Jungle_Dead_city_Desert == 'dead city':
        chose_beween_streets = input('''You have to choose between 
        Zombie Street or Wolf Street: 
                                     What will you choose:-''').lower()

        if chose_beween_streets == 'zombie street':
            print('''You will Survive
            Because when they come up to you 
            you have to act like them 
            and thus you will escape''')
        elif chose_beween_streets == 'wolf street':
            print('''You will be Dead because they will
            smell you''')
            print('Better Luck Next time!')
            quit()
        else:
            print("Invalid choice. The game is ending.")
            quit()

    elif chose_between_Jungle_Dead_city_Desert == 'desert':
        print('''You are in the desert. You need to find water to survive!''')
        water_source = input('''Do you want to look for an oasis or try to find shelter first?
        1) Oasis
        2) Shelter
        What will you choose?''').lower()

        if water_source == 'oasis':
            print('''You found the oasis and can now survive in the desert!''')
        elif water_source == 'shelter':
            print('''You found shelter but will need to find water soon to survive!''')
        else:
            print("Invalid choice. The game is ending.")
            quit()
    else:
        print("Invalid choice. The game is ending.")
        quit()
else:
    print("You chose not to play. Better luck next time!")
