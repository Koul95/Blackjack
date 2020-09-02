suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
import random



class Cards:
    
    def __init__(self,suits,ranks):
        
        self.suits=suits
        self.ranks=ranks
        self.value=values[self.ranks]
        
    def __str__(self):
        
        return self.ranks+' of '+self.suits


class Deck:
    
    def __init__(self):
        
        self.cards=[]
        for suit in suits:
            for rank in ranks:
                
                self.cards.append(Cards(suit,rank))
                
    
    def __str__(self):
        
        my_deck=''
        for _ in self.cards:
            
            my_deck+=_.__str__()
            
        
        return my_deck
    
    def deal_card(self):
        
        return self.cards.pop()
    
    
    def shuffle(self):
        
        random.shuffle(self.cards)
        
        
class Chips:
    
    def __init__(self,total_chips=100):
        
        self.total_chips=total_chips
    
    def win_chips(self,winning_chips):
        
        self.total_chips+=winning_chips
        
    def loose_chips(self,lost_chips):
        
        self.total_chips-=lost_chips
        
         	

class Hand:
    
    def __init__(self):
        
        self.hand_cards=[]
        self.total_card_value=0
        self.aces=0
        
    def add_cards(self,added_card):
        
        self.hand_cards.append(added_card)
        self.total_card_value+=added_card.value
        if added_card.ranks=='Ace':
            self.aces+=1
            
        while self.total_card_value>21 and self.aces:
            
            self.total_card_value-=10
            self.aces-=1
            
    def refresh(self):
        self.hand_cards.clear()
            
    
            
    
def replay():
    
    choice=''
    
    while choice not in ['Y','N']:
        
        choice = input('Do you want to replay [Y/N] Please enter a valid input  ').upper()
        
    if choice=='Y':
        return True
    
    else:
        return False
    
    


def hit(new_deck,player_hand):
    
    player_hand.add_cards(new_deck.deal_card())
        
        
    
    
    
def show_some_cards(player_hand,dealer_hand):
    
    print('Players Hand')
    for i in range(len(player_hand.hand_cards)):
        print(player_hand.hand_cards[i])
        
    print('Total Value:'+str(player_hand.total_card_value))
    print('-----------------\n')
    
    
    
    
    print('\nDealer Hand')
    print('<--Hidden--Card-->')
    for i in range(1,len(dealer_hand.hand_cards)):
        print(dealer_hand.hand_cards[i])
    print('-----------------\n')
        
        
        
def show_all_cards(player_hand,dealer_hand):
    
    print('Players Hand')
    for i in range(len(player_hand.hand_cards)):
        print(player_hand.hand_cards[i])
    
    print('Total Value:'+str(player_hand.total_card_value))
    print('-----------------\n')
    
    
        
    
    
    print('\nDealer Hand')
    
    for i in range(len(dealer_hand.hand_cards)):
        print(dealer_hand.hand_cards[i])
        
    print('Total Value:'+str(dealer_hand.total_card_value))
    print('-----------------\n')


def take_bet(player_chips):
    
    betted_chips=player_chips.total_chips+1
    
    while betted_chips>player_chips.total_chips:
        
        betted_chips=int(input('Enter the valid no. of chips you want to bet:'))
        
    return betted_chips
        
        
    
    
def hit_or_stand():
    
    choice=''
    
    while choice not in ['H','S']:
        
        choice=input('Press H for hit and S for stand ').upper()
        
    if choice=='H':
        
        return True
    
    else:
        
        return False
        
        


while True:
    
    
    
    print('Welcome to the game of blackjack')
    
    new_deck=Deck()
    
    new_deck.shuffle()
    
    
    player_chips=Chips()
    
      

    
    
    
    game_mode=True
    
    
    while game_mode:
               
        player_hand=Hand()
        dealer_hand=Hand()

        betted_chips=take_bet(player_chips)

        
        player_hand.add_cards(new_deck.deal_card())
        player_hand.add_cards(new_deck.deal_card())
    
        dealer_hand.add_cards(new_deck.deal_card())
        dealer_hand.add_cards(new_deck.deal_card())
        show_some_cards(player_hand,dealer_hand)
        
        flag=0
        
        while hit_or_stand():
            
            hit(new_deck,player_hand)
            show_some_cards(player_hand,dealer_hand)
            
            if player_hand.total_card_value>21:
                
                show_all_cards(player_hand,dealer_hand)
                print('Player Lost\n')
                player_chips.loose_chips(betted_chips)
                print('Remaining chips:'+str(player_chips.total_chips))
                
                flag=1
                break;
                
            elif player_hand.total_card_value==21:
                
                show_all_cards(player_hand,dealer_hand)
                print('Player Hit Blackjack!!\n')
                player_chips.win_chips(betted_chips)
                print('Remaining chips:'+str(player_chips.total_chips))
                
                flag=1
                break;
        
        
        if flag==0:
            
            
            while dealer_hand.total_card_value<=player_hand.total_card_value:
                
                hit(new_deck,dealer_hand)
                
                
                
             
            if dealer_hand.total_card_value>21:
                
                show_all_cards(player_hand,dealer_hand)
                print('Player Won\n')
                player_chips.win_chips(betted_chips)
                print('Remaining chips:'+str(player_chips.total_chips))
                    
                
                    
            elif dealer_hand.total_card_value>player_hand.total_card_value and dealer_hand.total_card_value<=21:
                
                show_all_cards(player_hand,dealer_hand)
                print('Player Lost\n')
                player_chips.loose_chips(betted_chips)
                print('Remaining chips:'+str(player_chips.total_chips))
                    
                
                
        if not replay():
            game_mode=False
            print('Thanks for playing ')
                
        
        
        
                    
                
                
            
            
            
         
     