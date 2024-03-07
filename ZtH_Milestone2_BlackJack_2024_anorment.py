"""
Created by Alex Norment
on 3.1.2024
The goal is to create a simple blackjack game for the user vs an automated dealer using at least one class and OOP in some way during the program. 
This program must contain:
1. The player able to stand or hit
2. player must be able to choose their betting amount
3. program must keep track of the players total money
4. need to alert for player wins, losses, and busts
"""

import sys
import time
import random

ruleLettering = r"""
 ______     __  __     __         ______     ______    
/\  == \   /\ \/\ \   /\ \       /\  ___\   /\  ___\   
\ \  __<   \ \ \_\ \  \ \ \____  \ \  __\   \ \___  \  
 \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \/\_____\ 
  \/_/ /_/   \/_____/   \/_____/   \/_____/   \/_____/ """

rules = r"""
>The goal is to get as close as possible to 21 without going over
>Aces are 11 or 1
>Face cards are 10
>Bets are limited between $2 and $500
>All players cards are delt face up with the dealer having 1 face down card
>When the player has a "natural" (an ace and a 10 card) giving an immeadiate 21, dealer pays 1.5x times the payer bet
>if the dealer has a "natural" (an ace and a 10 card), all players lose their bet
>if both the player and dealer have a "natural" that player gains back their bet
>once all players have finished their turn, the dealer will play and their face down card will be turned face up
    -if total of dealer's cards is 17 or more they stand, but will have to continue to hit until reaching that number or above
"""

advLettering = r"""
 ______     _____     __   __   ______     __   __     ______     ______     _____        ______     __  __     __         ______     ______    
/\  __ \   /\  __-.  /\ \ / /  /\  __ \   /\ "-.\ \   /\  ___\   /\  ___\   /\  __-.     /\  == \   /\ \/\ \   /\ \       /\  ___\   /\  ___\   
\ \  __ \  \ \ \/\ \ \ \ \'/   \ \  __ \  \ \ \-.  \  \ \ \____  \ \  __\   \ \ \/\ \    \ \  __<   \ \ \_\ \  \ \ \____  \ \  __\   \ \___  \  
 \ \_\ \_\  \ \____-  \ \__|    \ \_\ \_\  \ \_\\"\_\  \ \_____\  \ \_____\  \ \____-     \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \/\_____\ 
  \/_/\/_/   \/____/   \/_/      \/_/\/_/   \/_/ \/_/   \/_____/   \/_____/   \/____/      \/_/ /_/   \/_____/   \/_____/   \/_____/   \/_____/ """

advancedRules = r"""
splitting pairs
>if both original cards are the same (2 jacks, 2 6's, etc) the player can treat them as two different hands
>to do this, the original bet must also be placed on the second hand
>the left hand will be played first and must be hit at least once, then the right hand will be played
>if the player has 2 aces, the player will be given one card each for both hands and will not be allowed to draw again
>If the player receives a natural from this, the payoff will be equal to the bet and not 1.5x as opposed to a normal natural

Double down
>if a player received cards totaling 9,10, or 11 the player can double down, where they double their bet and receive a facedown card which will be reveiled once all bets are settled and players are done with their turn

>The dealer cannot double down or split pairs, and the player cannot do both but only play one way; normally, split, or double down
"""

#TODO add an advanced set of game rules for multiple players including deck cuts, using the same amount of decks as players, double down, and splitting pairs
advancedGame = False
amountOfPlayers = 1
playersList = []
fastType = False


suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
display = {
    "Two":
    r"""
.------.
|2.--. |
| (\/) |
| :\/: |
| '--'2|
`------'""",
    "Three":
    r"""
.------.
|3.--. |
| :(): |
| ()() |
| '--'3|
`------'""",
    "Four": 
    r"""
.------.
|4.--. |
| :/\: |
| :\/: |
| '--'4|
`------'""",
    "Five":
    r"""
.------.
|5.--. |
| :/\: |
| (__) |
| '--'5|
`------'""",
    "Six":
    r"""
.------.
|6.--. |
| (\/) |
| :\/: |
| '--'6|
`------'""",
    "Seven":
    r"""
.------.
|7.--. |
| :(): |
| ()() |
| '--'7|
`------'""",
    "Eight":
    r"""
.------.
|8.--. |
| :/\: |
| :\/: |
| '--'8|
`------'""",
    "Nine":
    r"""
.------.
|9.--. |
| :/\: |
| (__) |
| '--'9|
`------'""",
    "Ten":
    r"""
.------.
|10--. |
| :/\: |
| (__) |
| '--10|
`------'""",
    "Jack":
    r"""
.------.
|J.--. |
| :(): |
| ()() |
| '--'J|
`------'""",
    "Queen":
    r"""
.------.
|Q.--. |
| (\/) |
| :\/: |
| '--'Q|
`------'""",
    "King":
    r"""
.------.
|K.--. |
| :/\: |
| :\/: |
| '--'K|
`------'""",
    "Ace":
    r"""
.------.
|A.--. |
| (\/) |
| :\/: |
| '--'A|
`------'"""
}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank
        
    def __int__(self):
        return self.value
    
class Deck:

    def __init__(self):
        # initial deal and update for the deck, will add all 52 cards
        self.deckOfCards = []
        self.testlist = []
        for rank in ranks:
            for suit in suits:
                self.testlist.append(rank)
                self.deckOfCards.append(Card(rank, suit))
    
    def combine(self, *args):
        # to deal multiple decks, call a different deck class and then combine here, can accept all decks needed
        for arg in args:
            self.deckOfCards = self.deckOfCards + arg.deckOfCards

    def shuffle(self):
        random.shuffle(self.deckOfCards)
    
    def deal(self):
        # used with the Player.hit() to deal single cards

        return self.deckOfCards.pop()
    
    def split(self):
        # splitting the deck by random amount and adding it to the end of the deck list
        amtToSplit = random.randint(1, len(self.deckOfCards) - 1)
        for _ in range(amtToSplit):
            self.deckOfCards.append(self.deckOfCards.pop(0))
        pass

    def cut(self):
        # cutting out a random amount of cards from the front of the deck list to prevent counting cards
        amtToCut = random.randint(1, int((len(self.deckOfCards))/2))
        for _ in range(amtToCut):
            self.deckOfCards.pop(0)
        return "cutting deck..."

    def __len__(self):
        return len(self.deckOfCards)  

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bank = 1000
        self.bet = 0
        self.active = True

    def starting_deal(self, deck):
        # used once in order to deal 2 cards for starting hand
        for _ in range(2):
            self.hand.append(deck.deal())
        #print(self.hand[0])
        #print(self.hand[1])
            
    def hit(self, deck):
        # used every time a player hits
        self.hand.append(deck.deal())

    def get_card_total(self):
        # checks the total points that the player has and if the player busts *and* has an ace will return the lower number for the ace
        total =0
        hasAce = False

        for card in range(len(self.hand)):
            if int(self.hand[card]) == 11:
                hasAce = True
            total += int(self.hand[card])

        if total > 21 and hasAce == True:
            return f"{self.name}'s card total is: {total - 10}"
        else:
            return f"{self.name}'s card total is: {total}"

    def print_out_hand(self):
        # prints out the cards in the players hand all fancy like
        print(f"{self.name}'s current hand:")
        for card in range(len(self.hand)):
            print(display[str(self.hand[card])])

    def player_information_pintout(self):
        return f"Player {self.name} has {self.bank} in their bank"
    
    def __str__(self):
        return self.name
    
class Dealer(Player):
    def __init__(self, name = "Dealer"):
        self.name = name
        self.hand = []

    def starting_deal(self, deck):
        for _ in range(2):
            self.hand.append(deck.deal())
        return display[str(self.hand[1])]
    
    def __str__(self):
        return "Dealer is watching over the game"
    
def slow_type(inputString):
    # https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
    # used for a more astetically pleasing approach to posting rules as opposed to posting a huge block of text
    if fastType == True:
        typing_speed = 7000 #wpm
    else:
        typing_speed = 500

    for letter in inputString:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

def intro():
    global fastType
    fastType = False
    slow_type("Welcome to Alex's")
    time.sleep(.5)
    fastType = True
    slow_type(r"""
 ______     __         ______     ______     __  __          __     ______     ______     __  __    
/\  == \   /\ \       /\  __ \   /\  ___\   /\ \/ /         /\ \   /\  __ \   /\  ___\   /\ \/ /    
\ \  __<   \ \ \____  \ \  __ \  \ \ \____  \ \  _"-.      _\_\ \  \ \  __ \  \ \ \____  \ \  _"-.  
 \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\    /\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/\/_/    \/_____/   \/_/\/_/   \/_____/   \/_/\/_/ 
""")

def print_rules():
    global fastType
    fastType = True
    slow_type(ruleLettering)
    fastType = False
    slow_type(rules)
    time.sleep(1)
    fastType = True
    slow_type(advLettering)
    fastType = False
    slow_type(advancedRules)

def player_request():
    # setting the amount of players with recursion to cover errors, then calls extra decks for more than 1 player
    global amountOfPlayers
    temp_player_request = input("Please enter the amount of players from 1 to 7: ")

    try:
        amountOfPlayers = int(temp_player_request)
    except ValueError:
        print("please enter a single number character instead of spelling it out")
        player_request()

    if amountOfPlayers > 7:
        print("A max of 7 players is available, please enter a number from 1 to 7")
        player_request()
    elif amountOfPlayers < 1:
        print("A minimm of 1 player must be chosen, please enter a number from 1 to 7")
    
    if amountOfPlayers > 1:
        multiple_players_multiple_decks(amountOfPlayers - 1)

    create_players(amountOfPlayers)

def create_players(amountOfPlayers):
    for player in range(amountOfPlayers):
        newPlayer = input(f"Player {player+1}, please enter your name: ")
        
        playersList.append(Player(newPlayer))
    pass

def multiple_players_multiple_decks(amountOfNewDecks):
    # called when requested to be above 1 player, will then add extra decks to match the number of players and then cut the deck
    for i in range(amountOfNewDecks):
        i = Deck()
        mainDeck.combine(i)
    mainDeck.shuffle()
    mainDeck.cut()

def initiate_starting_deck():
    global mainDeck 
    mainDeck = Deck()
    mainDeck.shuffle()
    mainDeck.split()

def game_mode_selection():
    #TODO make a selction to turn on advanced rules
    pass

def play_until():
    #TODO request the number of rounds to play or run out of cash

    pass

def starting_deal():
    #TODO get the initial deal out for each player and the dealer
    pass

def show_all_hands():
    #TODO display the cards for each player and the single for the dealer
    pass

def betting_round():
    #TODO request bets, and check for naturals - player first
    pass

def natural_check():
    # Check for naturals - players first
    pass

def player_turn():
    #TODO player turn until all players are finished, must display final point score and if the player busts
    pass

def dealer_turn():
    #TODO dealer turn
    pass

def payout_and_turn_end():
    #TODO payout, end turn
    #repeat until number of rounds is achieved or all players are zeroed out in the bank
    pass

def test_numero_one():
    John = Player(input("Player 1, please enter your name: "))

    John.starting_deal(mainDeck)
    John.hit(mainDeck)
    John.hit(mainDeck)
    John.print_out_hand()
    print(John.get_card_total())

def test_numero_two():
    mrDeal = Dealer()
    print(mrDeal.starting_deal(mainDeck))
    mrDeal.print_out_hand()
    print(mrDeal.get_card_total())
    print(mrDeal)

initiate_starting_deck()
#intro()
#time.sleep(1)
#print_rules()

game_mode_selection()
play_until()
#player_request()





create_players(3)
for x in range(len(playersList)):
    playersList[x].starting_deal(mainDeck)
    playersList[x].hit(mainDeck)
    playersList[x].hit(mainDeck)
    playersList[x].print_out_hand()
    print(playersList[x].get_card_total())
