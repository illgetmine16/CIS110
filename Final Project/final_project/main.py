'''
Pseudocode

1. Get Variables
2. Describe Situation
3. First choice
    3(B). Nested Choice
4. Second Choice
    4.(B) Second Nested Choice
5. Ask to play again
'''

from LostMonkey import my_decisions

playGame = True

while playGame:
    monkeyName = input("What is the monkey's name?\n").title()
    userName = input("What is your name?\n").title()
    myCity = input("What city are you in?\n").title()
    favSubject = input("What is your favorite subject?\n").title()
    favNumber = int(input("What is your favorite number?\n"))

    print()

    print(f"This story is about a monkey named {monkeyName}. {monkeyName} gets loose and gets to explore {myCity}. While exploring, multiple decisions will need to be made that will affect the outcome. Let's play!\n")
    print(f"{monkeyName} is excited that they are able to explore the city. While wondering around, the monkey sees a huge sign with a bunch of animals.\nHe notices on the sign is a gorilla. He's never seen another monkey before,\nso he gets excited.\n")
    enter_zoo = input(f"Should {monkeyName} go into the zoo?('Yes' or 'No')\n").lower()

    if enter_zoo == 'yes':

        if my_decisions.zoo_choice1(monkeyName, favNumber):
            print(f"While running through the streets, {monkeyName} sees a group of teenagers carrying books walking into a building. The monkeys decide to follow the kids into a building. The building is a science building for the local University\n")
            print(f"After entering the building, the monkeys start to follow the kids. {monkeyName} notices a green glow coming from a different door and is curious, but hears the student's talking about {favSubject} in a classroom and doesn't know which direction to go.\n")
            print()
            go_to_class = input(f"Should {monkeyName} go investigate the green light? ('yes' or 'no')\n")
            print()
            my_decisions.school_choice(go_to_class, monkeyName, userName)
    elif enter_zoo == 'no':
        print(f"{monkeyName} decides not to go into the zoo. Instead he sees a group of teenagers wearing backpacks and carrying books. {monkeyName} loves books and decides to follow them.\n")
        print(f"Once {monkeyName} is inside, they see the kids enter a classroom. They also notice a green glowing light coming from behind another door. Should {monkeyName} go investigate the light? ('yes' or 'no')\n")
        investigate_light = input().lower()

        if investigate_light == 'yes' or investigate_light == 'no':
            my_decisions.solo_investigate(investigate_light, monkeyName, userName)
        else:
            print("I don't know what that means\n")
    else:
        print("I'm not sure what you mean...\n")



    playAgain = input("Would you like to play again? ('Yes' or 'No')\n").lower()

    if playAgain == 'no':
        playGame = False

        




