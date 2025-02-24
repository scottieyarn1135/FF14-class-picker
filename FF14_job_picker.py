# This imports the random liberay 
import random
import sys

# creates a list of the current jobs in the game

tank = ["Warrior","Paladin","Dark Knight","Gunbreaker"]
heal = ["White Mage","Scholar","Astrologian","Sage"]
dps = ["Monk","Dragoon","Ninja","Samurai","Bard","Machinist","dancer","Black-mage","Summoner","Red-Mage","Reaper","Viper","Pictomancer"]
# This is for all the jobs in the game
every_class = tank+dps+heal

print("Thank you for using the FF14 Job picker")
print("Before we can show you a class to level first you should see the following\n 1.)Tanks\n 2.)DPS\n 3.)Healer\n 4.)All the classes.")

# if else funtion based on the user choice it will pick a random class from the list chosen.
def picker(option = int(input("Please Select which made you want: "))):
    try:
        if option == 1:
            print(random.choice(tank))
        elif option == 2:
            print(random.choice(dps))
        elif option == 3:
            print(random.choice(heal))
        elif option == 4:
            print(random.choice(every_class))
    except:
        if option >= 5:
            print("This is not an option")
            sys.exit(1)
picker()
