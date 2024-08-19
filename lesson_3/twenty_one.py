'''
My solo attempt at twenty one. I don't think my implementation was the worst,
but I feel like the way I set the game up wasn't great because it required some
functions to be somewhat redundant (deal_cards()) or require certain arguments
for minor things.
'''

import random
import os

def prompt(message):
    print(f'==> {message}')

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10,
            'Jack', 'Queen', 'King', 'Ace'
            ]

DECK = {suit: CARDS.copy() for suit in SUITS}

CARDS_PER_SUIT = 13

CARD_VALUES = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
}

TWENTY_ONE = 21

ACE_VALUE = 11

def clear_screen():
    os.system('clear')

def initialize_dealt():
    return {
        'Clubs': [],
        'Diamonds': [],
        'Hearts': [],
        'Spades': [],
    }

def initialize_hand():
    return {}, {}, {}

def announce_player_hand(hand):
    prompt('Your current hand is: ')

    for suit, cards in hand.items():
        for card in cards:
            prompt(f'{card} of {suit}')

def announce_dealer_hand(hand, dealer_unseen):
    prompt('The dealer\'s hand is: ')

    for suit, cards in hand.items():
        for card in cards:
            if {suit: card} != dealer_unseen:
                prompt(f'{card} of {suit}')

def deal_cards(dealt, p_hand, d_hand, dealer_unseen):
    for i in range(4):
        card_suit = random.choice(SUITS)
        card_value = DECK[card_suit][
            random.choice(range(0, CARDS_PER_SUIT))]
        card = {
            card_suit: card_value
        }

        while card[card_suit] in dealt[card_suit]:
            card_suit = random.choice(SUITS)
            card_value = DECK[card_suit][
                random.choice(range(0, CARDS_PER_SUIT))]
            card = {
                card_suit: card_value
            }

        dealt[card_suit].append(card_value)

        if i <= 1:
            if card_suit in p_hand:
                p_hand[card_suit].append(card_value)
            else:
                p_hand[card_suit] = [card_value]

        if i > 1:
            if not d_hand:
                dealer_unseen[card_suit] = card_value

            if card_suit in d_hand:
                d_hand[card_suit].append(card_value)
            else:
                d_hand[card_suit] = [card_value]

def total_hand(hand):
    hand_total = 0
    ace_counter = 0

    for cards in hand.values():
        for card in cards:
            if card == 'Ace':
                ace_counter += 1
            else:
                hand_total += CARD_VALUES.get(card)

    if ace_counter:
        for _ in range(ace_counter):
            if hand_total + ACE_VALUE <= TWENTY_ONE:
                hand_total += ACE_VALUE
            else:
                hand_total += 1

    return hand_total

def announce_total(total):
    prompt(f'Hand total is: {total}')

def card_hit(hand, dealt):
    card_suit = random.choice(SUITS)
    card_value = DECK[card_suit][random.choice(range(0, CARDS_PER_SUIT))]
    card = {
        card_suit: card_value
    }

    while card[card_suit] in dealt[card_suit]:
        card_suit = random.choice(SUITS)
        card_value = DECK[card_suit][random.choice(range(0, CARDS_PER_SUIT))]
        card = {
            card_suit: card_value
        }

    dealt[card_suit].append(card_value)

    if card_suit in hand:
        hand[card_suit].append(card_value)
    else:
        hand[card_suit] = [card_value]

def player_turn(hand, dealers_hand, dealer_unseen, dealt):
    player_hand_total = total_hand(hand)

    if player_hand_total == TWENTY_ONE:
        announce_player_hand(hand)
        prompt(f'You were dealt {TWENTY_ONE}!')
        input('Enter to continue. ')
        return player_hand_total

    while not busted(player_hand_total):
        clear_screen()

        announce_dealer_hand(dealers_hand, dealer_unseen)
        prompt('And one face down card.')
        print('')

        announce_player_hand(hand)
        print('')

        announce_total(player_hand_total)

        if player_hand_total == TWENTY_ONE:
            input('Enter to continue. ')
            break

        prompt('Hit or stay? (h/s)')
        hit_or_stay = input().strip()

        while hit_or_stay.lower() not in ['h', 'hit', 's', 'stay']:
            prompt('Please enter a valid input: (h/s)')
            hit_or_stay = input().strip()

        if hit_or_stay.lower() in ['h', 'hit']:
            clear_screen()
            card_hit(hand, dealt)
            announce_player_hand(hand)
            player_hand_total = total_hand(hand)
            announce_total(player_hand_total)
            print('')

        else:
            break

    if busted(player_hand_total):
        prompt('You busted!')
        prompt('The dealer wins!')
        print('')

    else:
        prompt(f'You sit at {player_hand_total}')
        print('')
        return player_hand_total

    return player_hand_total

def dealer_turn(hand, player_pts, dealt, dealer_unseen):
    clear_screen()
    dealer_hand_total = total_hand(hand)

    if dealer_hand_total == TWENTY_ONE:
        prompt('The dealer\'s hand is:')
        announce_dealer_hand(hand, dealer_unseen)
        prompt('The dealer has TWENTY_ONE!')

    else:
        while dealer_hand_total < 16:
            prompt(f'You sit at {player_pts}')
            print('')

            dealer_hand_total = total_hand(hand)

            announce_dealer_hand(hand, dealer_unseen)
            prompt('And one face down card.')

            input('The dealer hits! (enter to continue).')
            print('')

            card_hit(hand, dealt)
            clear_screen()

            dealer_hand_total = total_hand(hand)

        dealer_hand_total = total_hand(hand)

    clear_screen()
    prompt(f'You sit at {player_pts}')
    print('')


    announce_dealer_hand(hand, dealer_unseen)
    for suit, card in dealer_unseen.items():
        prompt(f'And the face down card was the {card} of {suit}!')
        print('')

    announce_total(dealer_hand_total)

    return dealer_hand_total

def get_winner(player, dealer):
    if player > dealer:
        return 'player'

    if dealer > player:
        return 'dealer'

    return 'tie'

def announce_winner(won, player, dealer):
    if won == 'tie':
        prompt(f'You had {player} points, and the dealer had {dealer} points!')
        prompt('It\'s a tie!')
    else:
        prompt(f'You had {player} points, and the dealer had {dealer} points!')
        prompt(f'The {won} wins!')

def busted(points):
    return points > TWENTY_ONE

def welcome():
    clear_screen()
    prompt('Welcome to Twenty One.')
    prompt('Press enter to play. ')
    input('')

welcome()

def play_again():
    while True:
        replay = input('Play again? (y/n): ').strip().lower()
        if replay in ['', 'y', 'yes']:
            return True
        if replay in ['n', 'no']:
            return False

        print("Invalid input. Please enter a valid input (y/n).")

def twenty_one():
    while True:
        clear_screen()
        dealt_cards = initialize_dealt()
        player_hand, dealer_hand, dealer_face_down = initialize_hand()
        deal_cards(dealt_cards, player_hand, dealer_hand, dealer_face_down)

        player_points = player_turn(
            player_hand,
            dealer_hand,
            dealer_face_down,
            dealt_cards
        )

        if player_points <= TWENTY_ONE:
            dealer_points = dealer_turn(
                dealer_hand,
                player_points,
                dealt_cards,
                dealer_face_down
            )

            if dealer_points > TWENTY_ONE:
                prompt('The dealer busts! You win!')
            else:
                winner = get_winner(player_points, dealer_points)
                announce_winner(winner, player_points, dealer_points)

        if not play_again():
            break

twenty_one()

clear_screen()
prompt('Thanks for playing!')
