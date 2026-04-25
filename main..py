import random

cards = [11, 2, 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 10, 10, 10]
random.shuffle(cards)

want_to_play = input('Do you want to play a game of Blackjack ? Type y/n: ')

while want_to_play == 'y':

    user_cards = []
    user_cards.append(cards[0])
    user_cards.append(cards[1])
    score = sum(user_cards)
    print(f'    Your cards: {user_cards}, current score: {score}')

    computer_cards = []
    computer_cards.append(cards[random.randint(0,12)])
    computer_score = 0
    print(f'    Computer first card is: {computer_cards}')

    another = input('Do you want another card? Type y/n: ')
    while True:
        if another == 'y':
            user_cards.append(cards[random.randint(0,12)])
            score = sum(user_cards)
            if score <= 21:
                print(f'    Your cards: {user_cards}, current score: {score}')
                print(f'    Computer first card is: {computer_cards}')
                another = input('Do you want another card? Type y/n: ')
            elif score > 21:
                print(f'    Your cards: {user_cards}, current score: {score}')
                print('You lose. You went over')
                break

        else:
            print(f'    Your final cards: {user_cards}, final score: {score}')
            computer_cards.append(cards[random.randint(0,12)])
            computer_score = sum(computer_cards)
            print(f'    Computer final cards: {computer_cards}, final score: {computer_score}')
            if score == computer_score:
                print('         Draw.')
            elif computer_score > 21:
                print(f'    Computer final cards: {computer_cards}, final score: {computer_score}')
                print('Computer went over. You win.')
            elif computer_score <= 21 and computer_score < score:
                print('         You win.')
            else:
                print('         You lose.')
            break
    again = input('Do you want to play a game of Blackjack ? Type y/n: ')
    if again == 'y':
        continue
    else:
        print('Thanks for playing this Blackjack game. ^^')
        break



