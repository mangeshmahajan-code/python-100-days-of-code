import random
import art

user_score: int=0
computer_score=0

# all needed function
def card_drawn(cards_list,):
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    cards_list.append(random.choice(cards))

def check_blackjack (cards_list):
    if sum(cards_list)==21:
        print("computer black jack")

def ace_drawn(cards):
    # Reduce 11 -> 1 as many times as needed
    while sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return sum(cards)

def who_win(user_c,user_s,computers_c,computer_s):
    print(f"Your final hand: {user_c}, final score: {user_s}")
    print(f"Computer's final hand: {computers_c}, final score:{computer_s} ")
    global another_card
    another_card= "n"

# for restarting game
yes_or_no=input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
while yes_or_no=="y":
    user_cards=[]
    computers_cards=[]

    print("\n"*20)
    print(art.logo)

    card_drawn(user_cards)
    card_drawn(user_cards)
    user_score=sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    card_drawn(computers_cards)
    card_drawn(computers_cards)
    computer_score = sum(computers_cards)
    print(f"Computer's first card:{computers_cards[0]}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
# for adding cards
    while another_card=="y":
        card_drawn(user_cards)
        user_score = ace_drawn(user_cards)

        card_drawn(computers_cards)
        computer_score=ace_drawn(computers_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card:{computers_cards[0]}")
# checking where any one is bust
        if user_score>21:
             who_win(user_cards,user_score,computers_cards,computer_score)
             print("You went over. You lose 😭")

        elif computer_score  > 21 :
            who_win(user_cards, user_score, computers_cards, computer_score)
            print("Opponent went over. You win 😁")

        elif computer_score ==21:
            who_win(user_cards, user_score, computers_cards, computer_score)
            print("Opponent win 'blackjack'")

        elif user_score ==21:
            who_win(user_cards, user_score, computers_cards, computer_score)
            print("you win 'blackjack'")
        else:
            another_card=input("Type 'y' to get another card, type 'n' to pass:").lower()
# if user want to compare cards by not adding card
    else:
        # rule- computer have atleast 17 score
        while  computer_score <= 17:
            card_drawn(computers_cards)
            computer_score=sum(computers_cards)

        if user_score>computer_score:
            who_win(user_cards, user_score, computers_cards, computer_score)
            print("you win")
        elif user_score==computer_score:
            who_win(user_cards, user_score, computers_cards, computer_score)
            print("draw")
        else:
            who_win(user_cards, user_score, computers_cards, computer_score)
            print("You lose 😤")
# asking for restarting game
    yes_or_no=input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
