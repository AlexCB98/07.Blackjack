import random

cards = [11, 2, 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 10, 10, 10]
random.shuffle(cards)

# My cards
def my_cards():

    user_cards = []
    user_cards.extend(cards[0][1])

    score = sum(user_cards)

    return f'You cards: {user_cards}, current score: {score}'

my_cards()

