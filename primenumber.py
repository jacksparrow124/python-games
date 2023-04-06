import random
import time



deck = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'k', 'q', 'j', 'ace']

player_hand = []
dealer_hand = []

def card_value(card):
    if card == 'ace':
        return 11
    elif card == 'k' or card == 'q' or card == 'j':
        return 10
    else:
        return int(card)
    
def hand_total():
    total = 0
for card in hand:
            total += card_value(card)
return total

def deal_cards():
    player_hand.append(random.choice(deck))
    player_hand.append(random.choice(deck))
    dealer_hand.append(random.choice(deck))
    dealer_hand.append(random.choice(deck))
    
def deal_hit(turn):
    if turn == 1:
        player_hand.append(random.choice(deck))
    else:
        dealer_hand.append(random.choice(deck))
        
def display_hand(hand):
    display = ''
    for card in hand:
        if len(display) >0:
                display += ','
        display += card
        return display
    
print ('-------------WELCOME TO BLACKJACK UNLIMITED--------------------')
time.sleep(1)
print ('a game of luck, and fun.')
time.sleep(1)


deal_cards()
turn = 1 
player_bust = False
display = display_hand(player_hand)
print ('okay gambler! heres your hand: %s'% display)

while turn == 1:
    print ('want to hit?')
    hit = input('yes or no?')
    if hit == 'Yes' or hit == 'yes':
        deal_hit(turn)
        display = display_hand(player_hand)
        print ('your hand is: %s'% display)
        player_points == hand_total(player_hand)
        if (player_points > 21):
            print ('you bust! try again!')
            player_bust = True
            turn = 2
        else:
            turn = 2

dealer_bust = False
dealer_points = display_hand(dealer_hand)
print ('dealers hand is %s'% display)
time.sleep(1)

if player_bust:
    print ('dealer wins!!!')
else:
    if dealer_points < 16:
        deal_hit(turn)
        print ('the dealer hit!!!')
        time.sleep(1)
        display = display_hand(dealer_hand)
        print ('the dealers hand: %s'% display)
        if dealer_points > 21:
            time.sleep(1)
            print ('the dealer busted!!!')
            dealer_bust = True
        time.sleep(2)
        
player_points = hand_total(player_hand)
dealer_points = hand_total(dealer_hand)


if player_points > dealer_points or dealer_bust:
    print ('YOU WON WITH %s!!!!!!!!!'% player_points)
else:
    print ('dealer wins with %!!!!'% dealer_points)
    
        
        
    




















