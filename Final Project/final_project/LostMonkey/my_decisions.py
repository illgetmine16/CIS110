def zoo_choice1(monkeyName, favNumber ):
    print()
    print(f"{monkeyName} has entered the zoo, and quickly finds the gorilla enclosure.\nUpon arrival, he notices that there is something going on.\nEveryone is standing up and staring into the enclosure.\nIt seems a child has fallen over the barrier and is now inside the gorilla exhibit.\n")
    my_decision = input("Should he rush to help the child before the gorillas get to him? ('yes' or 'no')\n ").lower()
    if my_decision == 'yes':
        print(f"\n{monkeyName} rushes into the enclosure, racing past all of the gorillas. Before reaching the child, a loud 'BANG!' is heard. {monkeyName} was shot and now shall be known as Harambe in honor of a gorilla who had moved to a new zoo only hours earlier.")
        return False
    elif my_decision == 'no':
        print(f"\n{monkeyName} sits back and watches the situation unfold. A gorilla approaches the child and attempts to pick him up. Once getting near the child, a loud gunshot rang out. Once the commotion dies down, {monkeyName} is consumed by rage at watching his fellow monkey die. Now it's time to go and free {favNumber} other monkeys to help get revenge! The new army storms out of the zoo into the streets.\n")
        return True
    else:
        print("I don't understand")



def school_choice(answer, monkeyName, userName):
    if answer == 'no':
        print(f"{monkeyName} decides to go into the classroom. Able to sneak into the back, they just sit and listen to all of the talk between the professor and students. {monkeyName} is very curious and wants to ask questions, but is also shy. Should they ask anyways? ('yes' or 'no')")
        ask_question = input()
        if ask_question:
            print(f"\n{monkeyName} starts asking questions. The more they learn, the more questions they want to ask. A friend of {userName} is a student and recognizes {monkeyName} and takes them home. Everyone now refers to {monkeyName} as 'Curious George'.")
        else:
            print(f"\n{monkeyName} is too afraid to ask questions, but is listening intensely. A student who knows {userName} recognizes the monkey. They come and pick up {monkeyName} to return them to {userName}")
    elif answer == 'yes':
        print(f"The monkeys decide to go into the room with the glowing green light. Once they enter the room, they can't believe what they see. It is a huge machine that resembles a gian gun. It is shooting a green laser down into a mysterious rock that is also green. {monkeyName} being so curious, decides to get closer and reaches for the rock. Once it is touched, there is huge flash of green light and a blast that knocks all of the lights out. Once the monkeys wake up, they realize they are now larger and exponentially more intelligent. This is the beginning of 'Planet of the Apes'!\n")
    else:
        print("I have no idea what that means")



def solo_investigate(answer, monkeysName, usersName):
    if answer == 'no':
        print(f"{monkeysName} decides to go into the classroom. Able to sneak into the back, they just sit and listen to all of the talk between the professor and students. {monkeysName} is very curious and wants to ask questions, but is also shy. Should they ask anyways? ('yes' or 'no')\n")
        ask_question = input()
        if ask_question:
            print(f"\n{monkeysName} starts asking questions. The more they learn, the more questions they want to ask. A friend of {usersName} is a student and recognizes {monkeysName} and takes them home. Everyone now refers to {monkeysName} as 'Curious George'.\n")
        else:
            print(f"\n{monkeysName} is too afraid to ask questions, but is listening intensely. A student who knows {usersName} recognizes the monkey. They come and pick up {monkeysName} to return them to {usersName}.\n")
    
    elif answer == 'yes':
        print()
        print(f"{monkeysName} slowly approaches the door. After a second thought, they carefully push it open.")
        print(f"What {monkeysName} see completely amazes them. A large machine that is shaped like a gun, shooting a green laser into a glowing green stone.")
        print(f"Overwhelmed by curiousity, {monkeysName} decides to go and touch the stone. Immediately upon touching it, all of the radiation floods into the monkeys body, causing them to black out.")
        print(f"Moments later {monkeysName} wakes up to the sound of fire alarms and screaming kids. The monkey is now the size of a large house. The monkey is also angry that people keep screaming and shouting and wants to run away to New York.")
        print(f"The monkey decides to run away and visit the Empire State building. He would later be known as King Kong.\n")
    else:
        print("what are you trying to tell me right now?\n")