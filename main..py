import random

cards = [11, 2, 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 10, 10, 10]
random.shuffle(cards)

# My cards
def my_cards():

    user_cards = []
    user_cards.append(cards[0])
    user_cards.append(cards[1])
    score = sum(user_cards)
    print(f'Your cards: {user_cards}, current score: {score}')

    another = input('Do you want another card? Type y/n: ')
    while True:
        if another == 'y':
            user_cards.append(cards[2])
            score = sum(user_cards)
            if score < 21:
                print(f'Your cards: {user_cards}, current score: {score}')
                another = input('Do you want another card? Type y/n: ')
            elif score > 21:
                print(f'Your cards: {user_cards}, current score: {score}')
                return 'You went over. You lose.'
        else:
            return f'Your final cards: {user_cards}, final score: {score}'

print(my_cards())

