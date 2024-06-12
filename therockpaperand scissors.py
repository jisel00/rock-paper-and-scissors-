import math
import random
def play():
    user = input("Time to choose! 'r' for Rock, 'p' for Paper and finally 's' for Scissors ")
    user = user.lower()

    computer = random.choice(['r','p','s'])

    if user == computer:
        return (0,user, computer)
    
    if is_win(user, computer):
        return (1, user, computer)
    return (-1, user, computer)
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    return False

def play_best_of(n):

    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        if result == 0:
            print("It's a tie you both chose {}. \n". format(user))
        elif result ==1:
            player_wins += 1
            print("You chose {} while the computer chose {} You won]\n" .formar(user, computer))
        else:
            computer += 1
            print("You chose {} while the computer chose {} You lose]\n" .formar(user, computer))

    if player_wins > computer_wins:
        print("Yeyyyy, YOU JUST WON THE GAME BEST OF {}".format(n))
    else:
        print(" You LOSE IN BEST OUT OF {} GAME.".format(n))
    

if __name__ == '_main_':
    play_best_of(3)




