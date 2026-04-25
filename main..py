import random

cards = [11, 2, 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 10, 10, 10]
random.shuffle(cards)

want_to_play = input('Do you want to play a game of Blackjack ? Type y/n: ')

while want_to_play == 'y':

    print("\n" + "-" * 25)
    print("      BLACKJACK")
    print("-" * 25)

    user_cards = []
    user_cards.append(cards[0])
    user_cards.append(cards[1])
    score = sum(user_cards)
    print(f'Your cards: {user_cards}, current score: {score}')

    computer_cards = []
    computer_cards.append(cards[random.randint(0,12)])
    computer_score = 0
    print(f'Computer shows: {computer_cards}')

    another = input('Draw another card? Type y/n: ')
    while True:
        if another == 'y':
            user_cards.append(cards[random.randint(0,12)])
            score = sum(user_cards)
            if score <= 21:
                print(f'Your cards: {user_cards} (score: {score})')
                print(f'Computer shows: {computer_cards}')
                another = input('Draw another card? Type y/n: ')
            elif score > 21:
                print(f'Your cards: {user_cards} (score: {score})')
                print('\nResult: You lose. You went over')
                break

        else:
            print(f'\nYour final hand: {user_cards} (score: {score})')
            computer_cards.append(cards[random.randint(0,12)])
            computer_score = sum(computer_cards)
            print(f'Computer hand: {computer_cards} (score: {computer_score})')
            if score == computer_score:
                print('\nResult: Draw.')
            elif computer_score > 21:
                print('\nResult: Computer went over. You win.')
            elif computer_score <= 21 and computer_score < score:
                print('\nResult: You win.')
            else:
                print('\nResult: You lose.')
            break
    again = input('\nDo you want to play again ? Type y/n: ')
    if again == 'y':
        continue
    else:
        print('\nThanks for playing this Blackjack game. ^^')
        break



