import time

def text_print(text):
    for words in text:
        print(words, end='', flush=True)
        time.sleep(0.01)
    print()

while True:
    text_print("\n Welcome to 'Nakshatra' The Adventurous Island' Text Based Adventure Game.")
    text_print("""\n On a fateful night,\n under the full moon's shimmering light,\n you found yourself on a boat to find the treasure.
    \n Dark clouds began to gather on the horizon.\n Suddenly,a colossal wave crashed over the boat,\n and you tumbled into the icy depths below.""")
    text_print("\n you find your leg stuck in the anchor's chain and \n you shrink down and deep into the sea.")


    remove_chain=input("\n Do you want to remove chain? (yes/no) > ")


    if remove_chain == 'no':
        print("\n GAME OVER, you sink into the sea")

    else:
        text_print("""\n The frigid waters enveloped you, and darkness swallowed you whole.\n Next morning When you regain consciousness,\n you find yourself lying on a sandy shore.\n As you stand up and survey your surroundings, you see A Old Man, the Forest, the Dark Cave """)

        magical_sword = False
        magical_shield = False

        #choice
        while True:
            text_print("\n Where would you like to go?")
            text_print(" 1. Talk to the Old Man")
            text_print(" 2. Go into the Forest")
            text_print(" 3. Explore the Dark cave")

            choice = input("\n Enter your choice (1/2/3) > ")

            #oldman
            if choice == '1':

                if magical_sword:
                    text_print("\n The old man doesn't look here.")
                    text_print(" Old man gave me 'Magical sword', I think it will help me")
                    text_print(" I remember what he said,'Old man : I think you may go near the river and then... go into the dark cave.'")

                else:
                    #you and old man
                    text_print("\n You walked to the old man. ")
                    text_print("\n You: hello, I accidentally came here what is the name of this island?")
                    text_print(" Old man: Nakshatra, and I know you start your journey searching for treasure.")
                    text_print(" You: how do you know!!!!")
                    text_print(" Old man: I'm a wizard and know everything...")
                    text_print("\n Old man gives you some food and the magical sword.\n I think you may go near the river and then... go into the dark cave.")
                    text_print("\n you: 'Magical sword' looks so shiny ,ohh!!! where does old man go? ")
                    magical_sword = True

            #river
            elif choice == '2':
                text_print("\n You go into the forest,")
                if magical_shield:
                    text_print(" Angle doesn't look here.")
                    text_print(" but Angle gave me a 'Magical shield', I think it will help me.")
                else:
                    text_print(" and see an angle stuck into the marshy land you help angle.")
                    text_print(" \n angle: thanks for the help, let me give you a magical shield it will help you.")
                    text_print(" You: Thank you for 'magical shield' looks powerful, Ohh!! where does angle go?")
                    magical_shield = True

           #cave
            elif choice == '3':
                text_print("\n You enter the dark cave after walking some distance in the cave\n you see a Marvelous treasure guarded by a very big and dangerous red dragon.\n Suddenly, dragon senses you and attacks you with his fire breath.")
                if magical_sword and magical_shield:

                    #end of game
                    text_print("\n you block the dragon's fire breath with a magical shield and\n attack the dragon with a magical sword in one strike\n dragon's head is off and the dragon is dead.")
                    text_print(" then you go to the beach with the treasure and start to create a boat to go home with the treasure.")
                    text_print("\n GAME OVER")
                    text_print("\n Congratulations!\n You found the treasure and completed your quest!")
                    text_print("\n Credit \n Created by > Saurabh Jadhao \n For part-2 commentor message linked id > linkedin.com/in/saurabh-jadhao-8325482ab ")
                else:
                    #failed of game
                    text_print("\n You block it by jumping the big stone's backside.")
                    text_print(" You feel ill-prepared to fight with the dragon.")
                    text_print(" You decide to return to the Island and prepare yourself for the fight.")

            #return choise list
            choice_again = input("\n Do you want to go somewhere else?\n [#If you found treasure select 'no'] (yes/no) > ")
            if choice_again == 'no':
                text_print("\n Thank you for palying the adventure Game!!!")
                break

    #game play game
    game_again = input("\n Do you want to play game again? (yes/no) > ")
    if game_again == 'no':
        text_print("\n Thank you for playing, Good Day")
        break





