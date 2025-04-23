"""Snake,Water and Gun game project."""

import random


def play_again():
    """Ask the user whether they want to play again."""


    while True:
        user_choice = input("\nDo you want to play again.\nEnter 'yes' or 'no':\n").lower()


        if user_choice == 'yes':
            play()
            break

        elif user_choice == 'no':
            print('OK! Play Next Time.')
            break

        else:
            print("Please enter 'yes' or 'no'")
            

def play():
    """User can choose any one option and play game with computer."""
    options = ['Snake', 'Water', 'Gun']
    comp = random.choice(options)
    print("You can play snake, water and gun game with computer")
    user_input = input("For\nSnake (press 's')\nWater (press 'w')\nGun (press 'g')\n").lower()
    input_map = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
    user_choice = input_map.get(user_input)


    if not user_choice:
        print("Invalid input. Please choose 's', 'w', or 'g'.")
        return 
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {comp}")

    if comp == user_choice:
        print("🤝 It's a tie!")

    else:


        if comp == 'Snake':


            if user_choice =='Water':
                print("😢 You Lose.")

            elif user_choice =='Gun':
                print("🎉 You Win!")


        elif comp == 'Water':


            if user_choice =='Snake':
                print("🎉 You Win!")

            elif user_choice =='Gun':
                print("😢 You Lose.")
             

        elif comp == 'Gun':


            if user_choice =='Water':
                print("🎉 You Win!")    
                
            elif user_choice =='Snake':
                print("😢 You Lose.")


    play_again()   
if __name__ == '__main__':
    play()  
