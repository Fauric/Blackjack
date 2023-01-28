#from IPython.display import clear_output
#clear_output()
import random

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
          'Jack':10,'Queen':10,'King':10,'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        self.deck_shoe = []        
        '''
        this for loop generates a deck of cards with each card being assigned to the Card class
        '''
        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shoe_size(self,size):  #increases the size of the deck shoe(how many decks are being shuffled in)
        self.deck_shoe = self.all_cards * size
        print(len(self.deck_shoe))
                
    def shuffle(self):
        random.shuffle(self.deck_shoe)
        
    def deal_one(self):
        return self.deck_shoe.pop(0)
'''
generates the deck we will be playing with (game_deck.deck_shoe)
'''    
deck_size = 6
game_deck = Deck()
game_deck.shoe_size(deck_size)
game_deck.shuffle()
## 6 DECK SHOE HAS BEEN GENERATED. WILL BE USING game_deck.deck_shoe() FOR THE FINAL DECK ##
'''
Gives the player and dealer a hand list and hand value
'''
player_hand = []
player_value = 0

dealer_hand = []
dealer_value = 0

def deal_hand():
    global player_value
    global dealer_value
    while len(dealer_hand) < 2:
        player_value += game_deck.deck_shoe[0].value
        player_hand.append(game_deck.deal_one())
        dealer_value += game_deck.deck_shoe[0].value
        dealer_hand.append(game_deck.deal_one())
    print(f'Dealer shows: {dealer_hand[0]}\nPlayer shows: {player_value}')

#def dealer_turn():

def win_check():
    if player_value > dealer_value:
        print(f'{player1} wins!')
        account1.deposit()
        next_round()
        
    elif player_value < dealer_value:
        print(f'Dealer wins, your current balance is {account1.balance}')
        next_round
    else:
        print("it's a tie")
        account1.tie_deposit()
        next_round()

def player_win():
        pass
        

class Account:
 
    def __init__(self,player1,balance=0,bid=0):
        self.player1 = player1
        self.balance = balance
        self.bid = bid
        
    def __str__(self):
        return f'Account owner:   {self.player1}\nAccount balance: {self.balance}'
    '''DEPOSIT NOT WORKING  '''    
    def deposit(self):
        self.balance = int(self.balance) + (int(self.bid))*2
        print(f'You won ${self.bid} Your new balance is {self.balance}.')

    def tie_deposit(self):
        self.balance = int(self.balance) + int(self.bid)
        print(f'Your current balance is {self.balance}')

    def blackjack_win(self):
        bj_value = int(self.bid)*1.5
        self.balance = int(self.bid) + bj_value + int(self.balance)
        print(f'You won {bj_value}. your new balance is {self.balance}.')
    
    def withdraw(self):
        self.bid = input(f'Your current balance is ${self.balance}. What would you like to bid? ')
        while int(self.bid) > int(self.balance):
            print(f'Funds Unavailable! Your current balance is {self.balance}.')
            self.bid = input(f'Your current balance is ${self.balance}. What would you like to bid? ')

        else:
            self.balance = int(self.balance) - int(self.bid)
            print(f'You have bid {self.bid}')

'''
game start up logic
'''

def next_round():
    global player_hand
    global player_value
    global dealer_hand
    global dealer_value
    global game_on

    another_round = input('Continue? Y or N :  ')
    if another_round.upper() == 'Y' or another_round.upper() == 'YES':
        
        player_hand = []
        player_value = 0
        dealer_hand = []
        dealer_value = 0
    
        blackjack()
    elif another_round.upper() == 'N' or another_round.upper() == 'NO':
        game_on = False
        print(f'Thank you for playing, your final balance is {account1.balance}')
        blackjack()


def blackjack():
    
    while game_on:
        global player_value
        global dealer_value

        account1.withdraw()
        
        deal_hand()
        '''BLACKJACK CHECK'''
        if player_value == 21 and len(player_hand) == 2:
            print('BLACKJACK!')
            account1.blackjack_win()
            next_round()
        else:
            '''PLAYER TURN'''
            while player_value <= 21:
                response = input('Hit or Stay?')
                if response.upper() == 'HIT' or response.upper() == 'H':
                    player_value += game_deck.deck_shoe[0].value
                    player_hand.append(game_deck.deal_one())
                    print(f'Dealer shows: {dealer_hand[0]}\nPlayer shows: {player_value}')
                elif response.upper() == 'STAY' or response.upper() == 'S':
                    break
                else:
                    print('Invalid response, choose again')
            else:
                print(f'Player Bust! current balance is ${account1.balance}')
                next_round()

        '''DEALER TURN'''
        while dealer_value < 17:
            print(f'Dealer shows {dealer_hand[0]} and {dealer_hand[1]} \nValue of: {dealer_value}')
            dealer_value += game_deck.deck_shoe[0].value
            dealer_hand.append(game_deck.deal_one())
            print(f'Dealer shows: {dealer_value}\nPlayer shows: {player_value}')
        else:
            if dealer_value <= 21:
                win_check()
            else:
                print('Dealer bust!')
                account1.deposit()
                next_round()

        break
    else:
        print(f'thank you for playing, your final balance is {account1.balance}')

player1 = input('Welcome Player, choose your name:  ')
begin = input(f'Welcome {player1} to blackjack, you will be playing with a {deck_size} deck shoe. Would you like to begin? Y or N?')
account1 = Account(player1,500,0)
game_on = True

if begin.upper() == 'Y' or begin.upper() == 'YES':
    game_on = True
    blackjack()
else:
    game_on = False

if game_on == False:
    print('game over')