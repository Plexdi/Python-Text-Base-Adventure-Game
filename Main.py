import os
import time

def lost_text(item):
    for c in item:
        print(c, end='', flush=True)

def type_text_letterbyLetter(items):
    for index in items:
        print(index, end='', flush=True)
        time.sleep(0.05)

def type_text_one_text():
    text_one = "With the torch illuminating the cave, you discover two paths ahead. Each path seems to lead deeper into the cave. Your choices are:"
    for c in text_one:
        print(c, end='', flush=True)
        time.sleep(0.05)

def type_ordered_list(items):
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}", end='', flush=True)
        time.sleep(0.40)
        print()

def goodbyeMessage():
    FinalMessage ="Thank you for experiencing my interactive text-based adventure game. While I take pride in crafting this immersive narrative, I'd like to acknowledge that the story was AI-generated, and I handled the game development personally."
    type_text_letterbyLetter(FinalMessage)

    print()

    promotion_text = "If you wish to show your support, it would be greatly appreciated. Feel free to explore my social platforms and engage in conversations with me. Everyone is welcome to join the community. 😊"
    type_text_letterbyLetter(promotion_text)

    print()

    socials = ['Twitch: https://www.twitch.tv/plexdiiii', 'Discord: https://discord.gg/eVVnBf2gjk']

    for index, item in enumerate(socials, start=1):
        print(f'{index}: {item}', flush=True)
        time.sleep(0.05)

def main():
    os.system('cls')

    text = "You find yourself standing at the entrance of a mysterious cave deep in the heart of an uncharted jungle. The legends speak of a hidden treasure buried within the cave's depths. Will you embark on this perilous adventure to claim the lost treasure, or will you turn back?"

    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)

    print("\n\n\n")

    print("""
   _____ _                 _              __ 
  / ____| |               | |            /_ |
 | |    | |__   __ _ _ __ | |_ ___ _ __   | |
 | |    | '_ \ / _` | '_ \| __/ _ \ '__|  | |
 | |____| | | | (_| | |_) | ||  __/ |     | |
  \_____|_| |_|\__,_| .__/ \__\___|_|     |_|
                    | |                      
                    |_|
    """)

    texttwo = "As you step into the cave, the entrance closes behind you, leaving you in complete darkness. Your journey begins here. You have a few options:"

    for char1 in texttwo:
        print(char1, end='', flush=True)
        time.sleep(0.05)

    print()

    list_items = [
        "Light a torch to illuminate the cave.",
        "Feel your way through the darkness.",
        "Call out for help."
    ]

    type_ordered_list(list_items)

    while True:
        user_choice = input('\nType in the number of your decision: ')
        try:
            number = int(user_choice)
            if number == 1:
                script = "You light a torch, and the cave comes to life with the flickering light. You continue deeper into the cave with newfound confidence."
                for c in script:
                    print(c, end='', flush=True)
                    time.sleep(0.05)
                time.sleep(2.00)
                os.system('cls')
                break
            elif number == 2:
                scripttwo = 'You slowly and cautiously make your way through the darkness, stumbling over rocks and uneven terrain. You light a torch, and the cave comes to life with the flickering light. You continue deeper into the cave with newfound confidence.'
                for c2 in scripttwo:
                    print(c2, end='', flush=True)
                    time.sleep(0.05)
                break
            elif number == 3:
                scriptthree = 'Your voice echoes in the cave, but no one responds. You are alone.'
                for c3 in scriptthree:
                    print(c3, end='', flush=True)
                    continue
            else:
                error_text = 'Please enter in a value from 1 - 3'
                for c4 in error_text:
                    print(c4, end='', flush=True)
                    time.sleep(0.05)
                continue
        except ValueError:
            error_text_2 = 'Please enter in a value from 1 - 3.'
            for c5 in error_text_2:
                print(c5, end='', flush=True)
                time.sleep(0.05)
                continue

    os.system('cls')

    print("""
        _____ _                 _              ___  
        / ____| |               | |            |__ \ 
        | |    | |__   __ _ _ __ | |_ ___ _ __     ) |
        | |    | '_ \ / _` | '_ \| __/ _ \ '__|   / / 
        | |____| | | | (_| | |_) | ||  __/ |     / /_ 
        \_____|_| |_|\__,_| .__/ \__\___|_|    |____|
                            | |                        
                            |_|
    """)

    script2 = "With the torch illuminating the cave, you discover two paths ahead. Each path seems to lead deeper into the cave. Your choices are:"
    type_text_letterbyLetter(script2)
    print()
    options = ["Take the left path.", "Take the right path."]
    type_ordered_list(options)
    while True:
        print()
        second_stage = input('Enter in a number from 1 - 2: ')
        try:
            secondNumber = int(second_stage)
            if secondNumber == 1:
                second_text = "You follow the left path, hoping it will lead you to the treasure. It's a narrow passage"
                type_text_letterbyLetter(second_text)
                time.sleep(2)
                break

            elif secondNumber == 2:
                text2 = 'You choose the right path, which is wider and illuminated by faint, natural light.'
                type_text_letterbyLetter(text2)
                print() #preventing next line of code to run on the same line as "text2"
                print("You died.")
                while True:
                    retry_text = "Would you like to retry the game?"
                    type_text_letterbyLetter(retry_text)
                    print()
                    retry = input()
                    if retry.lower() == 'yes' or retry.lower() == 'yeah' or retry.lower() == 'yah':
                        os.system('cls')
                        main()
                    else:
                        confirmation_text = 'are you sure you would like to quit?'
                        type_text_letterbyLetter(confirmation_text)
                        confirmation = input()
                        if confirmation.lower() == 'yes' or confirmation.lower() == 'yeah' or confirmation.lower() == 'yah':
                            continue
                        else:
                            quit_text = "Thank you for playing my game have a nice day :D"
                            type_text_letterbyLetter(quit_text)
                            quit()                

        except:
            error = "Enter a Number"
            for u in error:
                print(u, end='', flush=True)
                continue
    

    os.system('cls')

    print("""
          
   _____ _                 _              ____  
  / ____| |               | |            |___ \ 
 | |    | |__   __ _ _ __ | |_ ___ _ __    __) |
 | |    | '_ \ / _` | '_ \| __/ _ \ '__|  |__ < 
 | |____| | | | (_| | |_) | ||  __/ |     ___) |
  \_____|_| |_|\__,_| .__/ \__\___|_|    |____/ 
                    | |                         
                    |_|                         
          """)
    
    situation_3_text = "You follow the left path, which eventually leads you to a mysterious room filled with treasures, artifacts, and ancient writings. You notice a locked chest in the corner. What will you do?"
    type_text_letterbyLetter(situation_3_text)
    time.sleep(2)

    options3 = ["Examine the artifacts and decipher the ancient writings.", "Try to open the locked chest.", "Leave the room and continue exploring the cave."]
    print()

    type_ordered_list(options3)
    print()
    while True:
        print()
        user_decision = input("Enter the number of your decisions: ")
        try:
            numbers = int(user_decision)
            if numbers == 1:
                implication = "You study the artifacts and decipher the writings, gaining insights into the cave's history and potential dangers."
                type_text_letterbyLetter(implication)
                time.sleep(3.00)
                break

            elif numbers == 2:
                implications = "As you try to open the chest, you trigger a trap, and the room begins to fill with poisonous gas. You died"
                type_text_letterbyLetter(implications)
                print()
                while True:
                    question = "Would you like to retry the game?"

                    type_text_letterbyLetter(question)
                    print()
                    retry = input()
                    if retry.lower() == 'yes' or retry.lower() == 'yeah' or retry.lower() == 'yah':
                        os.system('cls')
                        main()
                    else:
                        confirmation_text = 'are you sure you would like to quit?'
                        type_text_letterbyLetter(confirmation_text)
                        confirmation = input()
                        if confirmation.lower() == 'yes' or confirmation.lower() == 'yeah' or confirmation.lower() == 'yah':
                            main()
                        else:
                            quit_text = "Thank you for playing my game have a nice day :D"
                            type_text_letterbyLetter(quit_text)
                            quit()  

            elif numbers == 3:
                implication = "You decide not to disturb the room's contents and leave to explore further."
                type_text_letterbyLetter(implication)
                time.sleep(3.00)
                break
            else:
                print('Invalid option try again.')
                continue
                

        
        except ValueError:
            error = "Enter a Number"
            type_text_letterbyLetter(error)
            continue

    os.system('cls')

    print("""         
  _____ _                 _              _  _   
  / ____| |               | |            | || |  
 | |    | |__   __ _ _ __ | |_ ___ _ __  | || |_ 
 | |    | '_ \ / _` | '_ \| __/ _ \ '__| |__   _|
 | |____| | | | (_| | |_) | ||  __/ |       | |  
  \_____|_| |_|\__,_| .__/ \__\___|_|       |_|  
                    | |                          
                    |_|                          
                     
          """)
    
    situation_4_text = "While examining the artifacts, you suddenly hear a noise behind you. You turn to find a mysterious figure approaching. It's an old explorer who warns you about the curse guarding the treasure. Your choices are:"
    type_text_letterbyLetter(situation_4_text)

    print()

    situation_4_options = ["Listen to the old explorer's warning and leave the cave.", "Disregard the warning and continue your quest."]
    type_ordered_list(situation_4_options)

    print()
    while True:
        situation_4_decision = input()
        try:
            num = int(situation_4_decision)
            if num == 1:
                textnum_1 = "You heed the explorer's warning and choose to leave the cave, avoiding potential disaster. But no solutions."
                type_text_letterbyLetter(textnum_1)
                print()
                retry = input('would you like to play again? ')
                if retry == retry.lower() == 'yes' or retry.lower() == 'retry' or retry.lower() == 'yah':
                    os.system('cls')
                    main()
                else:
                    goodbyeMessage()
                    quit("This game has concluded")
                


            elif num == 2:
                textnum_2 = "You choose to continue, believing in your luck and determination. The explorer watches you disappear into the depths of the cave, concern in their eyes."
                type_text_letterbyLetter(textnum_2)
                break
            else:
                print('Invalid option try again')
                continue
        except ValueError:
            error = "Invalid Number"
            type_text_letterbyLetter(error)
            continue
            
    os.system('cls')

    print("""         

  ______ _             _       _____ _                 _                  _____ 
 |  ____(_)           | |     / ____| |               | |           _    | ____|
 | |__   _ _ __   __ _| |    | |    | |__   __ _ _ __ | |_ ___ _ __(_)   | |__  
 |  __| | | '_ \ / _` | |    | |    | '_ \ / _` | '_ \| __/ _ \ '__|     |___ \ 
 | |    | | | | | (_| | |    | |____| | | | (_| | |_) | ||  __/ |   _     ___) |
 |_|    |_|_| |_|\__,_|_|     \_____|_| |_|\__,_| .__/ \__\___|_|  (_)   |____/ 
                                                | |                             
                                                |_|                             
                   
                     
          """)
    
    chapter_5_text = "If you chose to continue, you eventually reach a chamber where you discover the hidden treasure. It gleams with gold, jewels, and ancient relics. You've found the lost treasure! What will you do now?"
    type_text_letterbyLetter(chapter_5_text)

    print()

    chapter_5_options = ["Claim the treasure as your own.", "Leave the treasure untouched and exit the cave."]
    type_ordered_list(chapter_5_options)


    print()
    while True:
        chapter_5_decision = input()
        try: 
            num5 = int(chapter_5_decision)
            if num5 == 1:
                implication5 = "You decide to claim the treasure, but as you reach for it, you trigger a final trap, sealing your fate within the cave forever. You loose"
                type_text_letterbyLetter(implication5)
                print()
                retryQuestion = 'Would you like to try again?'
                type_text_letterbyLetter(retryQuestion)
                print()
                retry5 = input()
                if retry5.lower() == 'yes' or retry5.lower() == 'yeah' or retry5.lower() == 'yah':
                    os.system('clear')
                    main()
                else:
                    break
            elif num5 == 2:
                implication5 = "You resist the temptation of the treasure, choosing to exit the cave safely. The legend of the lost treasure lives on, but you've survived."
                type_text_letterbyLetter(implication5)
                break
            else:
                print("Invalid option. Try again")
                continue
        except ValueError:
            error = "Invalid Number"
            type_text_letterbyLetter(error)
            continue

    goodbyeMessage()
    quit("This game has concluded")
main()