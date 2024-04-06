
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

user_cards = []
computer_cards = []
import random


def deal_card(li):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if sum(li)>=10 :
        cards.remove(11)
        cards.append(1)
        return random.choice(cards)
    else:
        return random.choice(cards)



def play_again():
    aga=input("Type 'y' if you want to play again, press anything to exit : ")
    if aga=='y':
        print(logo)
        user_cards.clear()
        computer_cards.clear()
        append()
        blackjack()
    else:
        print()
        print("Thanks for playing.")
        print()
        exit()


def append():
    for _ in range(2):
        user_cards.append(deal_card(user_cards))
        computer_cards.append(deal_card(computer_cards))
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    if sum(user_cards)==21:
        print("You got lucky. You win.")
        play_again()


def compare():
    if sum(user_cards)==21  or sum(computer_cards)>21  :
        #or ((sum(user_cards)>sum(computer_cards) and sum(user_cards) in range(17,22)) and sum(computer_cards) in range(17,22))
        print()
        print(f"\t Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"\t Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print()
        print("Opponent went over. You win.")
        print()
        play_again()

    elif sum(user_cards)>sum(computer_cards) and sum(user_cards) in range(17,22) and sum(computer_cards) in range(17,22) and inp_play=='n':
        print()
        print(f"\t Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"\t Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print()
        print("Opponent lose. You win.")
        print()
        play_again()

    elif sum(computer_cards)==21 or sum(user_cards)>21 :
        #or (sum(computer_cards)>sum(user_cards) and sum(user_cards) in range(17,22) and sum(computer_cards) in range(17,22))
        print()
        print(f"\t Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"\t Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print()
        print("You went over. Computer wins.")
        print()
        play_again()
    
        
    elif sum(computer_cards)>sum(user_cards) and sum(user_cards) in range(17,22) and sum(computer_cards) in range(17,22) and inp_play=='n':
        print()
        print(f"\t Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"\t Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print()
        print("You lose. Computer wins.")
        print()
        play_again()


    elif sum(user_cards)==sum(computer_cards) and sum(user_cards) in range(17,22):
        print()
        print(f"\t Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"\t Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print()
        print("It's a draw.")
        print()
        play_again()

    
def play():
    user_cards.append(deal_card(user_cards))
    print(f"\t Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"\t Computer's first card: {computer_cards[0]}")

append()


def blackjack():
    global inp_play
    while(True):
        print()
        inp_play=input("Type 'y' to get another card, type 'n' to pass: ")
        if inp_play=='y':
            play()
            compare()        

        elif inp_play=='n':
            while sum(computer_cards)<17:
                computer_cards.append(deal_card(computer_cards))
            
            compare()
            break
        
blackjack()

