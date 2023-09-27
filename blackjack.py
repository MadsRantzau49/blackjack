import random

games = 1000000
number_decks = 8
og_bet = 10.0
bet = og_bet

deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4 * number_decks
random.shuffle(deck)
deck_len = len(deck)
reshuffle = int(deck_len / 2)

win = 0
loss = 0
push = 0
profit = 10.0
loss_streak = 0
higest_loss_streak = 0
    
for i in range(games):
    deck_len = len(deck) 
    if deck_len > reshuffle:
        player_hand = []
        dealer_hand = []

        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        
        while sum(player_hand) < 12:
            player_hand.append(deck.pop())
            if sum(player_hand) > 21:
                pass
            else:
                while sum(dealer_hand) < 17:
                    dealer_hand.append(deck.pop())
        if sum(player_hand) > sum(dealer_hand) and sum(player_hand) <= 21:
            win += 1
            profit += bet
            bet = 10.0
            if loss_streak > higest_loss_streak:
                higest_loss_streak = loss_streak
                loss_streak = 0
                
        elif sum(player_hand) == sum(dealer_hand):
            push += 1
         
        elif sum(player_hand) == 21 and sum(dealer_hand) != 21:
            win += 1
            profit += bet * 1.5
            bet = 10.0
            if loss_streak > higest_loss_streak:
                higest_loss_streak = loss_streak
                loss_streak = 0
                
        elif sum(player_hand) == 21 and sum(dealer_hand) == 21:
            push += 1
           
        else:
            loss += 1
            profit -= bet
            bet *= 2
            loss_streak += 1
    else:
        deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4 * number_decks
        random.shuffle(deck)

non_push_outcomes = win + loss  
win_percentage = win / non_push_outcomes * 100
loss_percentage = loss / non_push_outcomes * 100

print("win ", win, " ", win_percentage, "%")
print("loss ", loss, " ", loss_percentage, "%")
print("push ", push, " ", push / games * 100, "%")
print("profit ", profit)
for h in range(higest_loss_streak):
    og_bet *= 2
print(higest_loss_streak, "most loss:",og_bet)