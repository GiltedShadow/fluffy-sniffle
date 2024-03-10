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
from os import system
import sys
import time
import random

gameName = r"""
 ______     __         ______     ______     __  __          __     ______     ______     __  __    
/\  == \   /\ \       /\  __ \   /\  ___\   /\ \/ /         /\ \   /\  __ \   /\  ___\   /\ \/ /    
\ \  __<   \ \ \____  \ \  __ \  \ \ \____  \ \  _"-.      _\_\ \  \ \  __ \  \ \ \____  \ \  _"-.  
 \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\    /\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/\/_/    \/_____/   \/_/\/_/   \/_____/   \/_/\/_/ """

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
>All bets up to $500 are accepted, starting cash is $1000
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

#TODO add advanced rules capability
advancedGame = False # game defaults to normal rules
amountOfPlayers = 1
playersList = []
# playerNaturalCheck = {}
# dealerBlackJack = False
# dealerNatural21 = False
fastType = False
gameModeRunOut = True
gameModeRoundsToPlay = 0
currentRound = 0
active = True

suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
display = {
    "Dealer":
    r"""
.------.
| .--. |
| :/\: |
| :\/: |
| '--' |
`------'""",
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
        self.roundOut = 0
        self.bust = False
        self.natural = False
        self.backjack = False

    def starting_deal(self, deck):
        # used once in order to deal 2 cards for starting hand
        for _ in range(2):
            self.hand.append(deck.deal())
        #print(self.hand[0])
        #print(self.hand[1])
            
    def hit(self, deck):
        # used every time a player hits
        self.hand.append(deck.deal())

    def print_out_card_total(self):
        return f"{self.name}'s card total is: {self.get_card_total()}"
    
    def get_card_total(self):
        # checks the total points that the player has and if the player busts *and* has an ace will return the lower number for the ace
        total =0
        hasAce = False

        for card in range(len(self.hand)):
            if int(self.hand[card]) == 11:
                hasAce = True
            total += int(self.hand[card])

        if total > 21 and hasAce == True:
            return total - 10 # issue here, need a comparison int
        else:
            return total

    def print_out_hand(self):
        # prints out the cards in the players hand all fancy like
        print(f"{self.name}'s current hand:")
        for card in range(len(self.hand)):
            print(display[str(self.hand[card])])

    def player_information_printout(self):
        return f"Player {self.name} has {self.bank} in their bank"
    
    def __str__(self):
        return self.name
    
class Dealer(Player):
    def __init__(self, name = "Dealer"):
        self.name = name
        self.hand = []
        self.natural = False
        self.bust = False
        self.blackjack = False

    def starting_deal(self, deck):
        for _ in range(2):
            self.hand.append(deck.deal())
        return display[str(self.hand[1])]
    
    def initial_hand_display(self):
        print("Dealers initial hand: ")
        print(display["Dealer"])
        print(display[str(self.hand[1])])

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
    slow_type(gameName)

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
        player_request()
    
    if amountOfPlayers > 1:
        multiple_players_multiple_decks(amountOfPlayers - 1)

    #create_players(amountOfPlayers) #likely do not need this function since its only called here
    for player in range(amountOfPlayers):
        newPlayer = input(f"Player {player+1}, please enter your name: ")
        
        playersList.append(Player(newPlayer))

def create_players(amountOfPlayers):
    #likely do not need this function since its only called here
    for player in range(amountOfPlayers):
        newPlayer = input(f"Player {player+1}, please enter your name: ")
        
        playersList.append(Player(newPlayer))
    
def multiple_players_multiple_decks(amountOfNewDecks):
    # called when requested to be above 1 player, will then add extra decks to match the number of players and then cut the deck
    for i in range(amountOfNewDecks):
        i = Deck()
        mainDeck.combine(i)
    mainDeck.shuffle()
    print(mainDeck.cut())

def initiate_starting_deck():
    global mainDeck 
    mainDeck = Deck()
    mainDeck.shuffle()
    mainDeck.split()

def resize_terminal():
    system('mode con: cols=150 lines=49')
    pass

def game_mode_selection():
    global gameModeRoundsToPlay
    global gameModeRunOut
    global advancedGame

    #TODO make advaned rules work

    # Can probably make this and "play_until" the same function, only run once at the beginning of the game
    gameModeCheck = input("Default settings for the game is normal rules with runout - that is player(s) will run out of money\nTo change this, please enter an amount of rounds to play, otherwise just hit enter to runout: ")

    if gameModeCheck != '':
        try:
            gameModeRoundsToPlay = int(gameModeCheck)
            gameModeRunOut = False
        except ValueError:
            print("Please enter a number, or just press enter to play as runout.")
            game_mode_selection()
    
    gameModeCheck = input("Would you like to play by advanced rules including pairs splitting and double downs? (y/n): \nAdvaned rules currently not supported")

    if gameModeCheck.lower() == 'y':
        advancedGame = True
    elif gameModeCheck.lower() == 'n':
        advancedGame = False

def play_until(gameModeRoundsToPlay):
    #TODO request the number of rounds to play or run out of cash
    # functionality moved to game_mode_selection
    pass

def first_round_deal():
    # get the initial deal out for each player and the dealer, and displayes dealer 1 card
    for player in playersList:
        player.starting_deal(mainDeck)
    
    mrDeal.starting_deal(mainDeck)
    print(mrDeal)
    mrDeal.initial_hand_display()
    
def show_all_hands():
    # display the cards for each player 
    for player in playersList:
        print(player.player_information_printout())
        player.print_out_hand()
        print(player.print_out_card_total())
        print("\n\n")

def betting_round():
    #request bets, and check for naturals - player first - no calls needed, game is player vs dealer

    playerCount = len(playersList)
    n = 0
    while n < playerCount:
        cashAvailable = playersList[n].bank
        betRequest = input(f"{playersList[n]}, please enter your bet up to $500, you have ${cashAvailable} to bet: ")
        try:
            betRequest = int(betRequest)
        except ValueError:
            print("please enter a number and not a word value")
            continue

        if betRequest > 500:
            print("Please enter a value $500 or under")
            continue
        elif betRequest < 1:
            print("Please enter a real value of money, this should not be zero or negative")
            continue
        elif betRequest >= 1 <= 500:
            if betRequest > cashAvailable:
                print("That is more than the money you have to bet")
                continue
            playersList[n].bet = betRequest

            n += 1

def natural_check():
    # Check for naturals - players first (first round only)
    # global dealerNatural21

    if len(playersList[0].hand) > 2:
        return
    for player in playersList:
        if player.get_card_total() == 21:
            player.natural = True
            # playerNaturalCheck[str(player.name)] = True
        else:
            player.natural = False
            # playerNaturalCheck[str(player.name)] = False

    if mrDeal.get_card_total() == 21:
        mrDeal.natural = True
        # dealerNatural21 = True

def player_turn():
    #TODO player turn until all players are finished, must display final point score and if the player busts
    #TODO add advanced logic




    pass

def dealer_turn():
    # dealer turn, moved dealer natural check here since the original deal only showed 1 card
    global dealerBlackJack

    print("Dealers turn!")
    mrDeal.print_out_hand()
    dealerPoints = mrDeal.get_card_total()

    while dealerPoints < 17:
        mrDeal.hit(mainDeck)
        print(display[str(mrDeal.hand[-1])])
        dealerPoints = mrDeal.get_card_total()
    
    if dealerPoints == 21:
        print("Dealer BlackJack!")
        dealerBlackJack = True
    elif dealerPoints > 21:
        mrDeal.bust = True
        print("Dealer bust!\nEveryone still active wins!")
    
def payout_and_turn_end():
    #TODO payout, end turn
    #repeat until number of rounds is achieved or all players are zeroed out in the bank

    n=0
    
    for player in playersList:
        
        # immeadiatly weed out players that have lost in previous rounds
        if player.active == False:
            n += 1
            continue

        # dealer bust + player still active
        if mrDeal.bust == True and player.bust == False:
            print(f"{player.name} has won {player.bet}!")
            player.bank = player.bank + player.bet

        # taking the bet amount away from players that have bust this round
        elif player.bust == True:
            player.bank = player.bank - player.bet
            print(player.player_information_printout())
            n += 1
            continue

        # against dealer natural, only way to win is for the player to also have a natural
        if mrDeal.natural == True: 
            for player in playersList:
                if player.natural == True:
                    player.bank = player.bank + player.bet
                    print(f"{player.name} has countered a dealer natural with one of their own! You win you bet back!")
                pass
            player.bank = player.bank - player.bet
        

        #TODO check against naturals for 1.0x payout, then non dealer blackjack and player natural for 1.5x payout, then normal wins and losses
        if dealerBlackJack == False:
            pass
    pass

def reset_all(playerCount):
    #this will reset all player hands and check to make sure the deck has enough cards to make it through next round

    for player in playersList:
        player.hand.clear()
        player.bust = False
        player.natural = False
        if player.active == False:
            print(f"{player.name} has lost after {player.roundOut} rounds")
            player.roundOut = currentRound
        else:
            print(player.player_information_printout())
    
    if len(mainDeck)/5 <= playerCount:
        #time to reset the deck!
        print(f"Reshuffling the deck! Well done lasting this long everyone :D")
        initiate_starting_deck()
        if playerCount > 1:
            multiple_players_multiple_decks(playerCount - 1)
    



def final_thanks_and_final_printout():
    #TODO final thanks and final printout
    

    pass

"""
Basic game logic to follow
after initial setup, looping logic will run until the game is complete
"""

initiate_starting_deck()
mrDeal = Dealer()
#resize_terminal()  # eyy it works!!  good to keep in mind for future projects
#intro()
#time.sleep(1)
#print_rules()
# noticing a problem here, the terminal isnt big enough to handle the "advanced rules" all together
# I can split the words but i wanna try resizing the terminal first 
print(str(mrDeal.natural))
game_mode_selection()
player_request()

while active:
    first_round_deal()
    betting_round()
    show_all_hands()
    natural_check()
    player_turn()
    dealer_turn()
    payout_and_turn_end()
    reset_all(amountOfPlayers)
    currentRound += 1

final_thanks_and_final_printout()

