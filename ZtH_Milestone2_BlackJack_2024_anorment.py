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

finalThankText = """
    ______)                                      
   (, /  /)          /)                          
     /  (/   _  __  (/_         ___              
  ) /   / )_(_(_/ (_/(__   (_/_(_)(_(_        /  
 (_//)                /)  .-/    ,           /   
   // _____     __   // _(_/      __   _    /    
  /(_(_)/ (_    /_)_(/_(_(_(_/__(_/ (_(_/_ o     
 /)          .-/          .-/        .-/         
(/          (_/          (_/        (_/                            
"""

#TODO add advanced rules capability
#TODO this

advancedGame = False # game defaults to normal rules
amountOfPlayers = 1
playersList = []
fastType = False
gameModeRunOut = True
gameModeRoundsToPlay = 999999
currentRound = 1
active = True

suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

displayHorizontal = {
    'Top':      r".------.",
    'Bottom':   r"`------'",

    'c-2':      r"| |A+| |",
    'c-3':      r"| |+N| |",

    'Dealer-1': r"| .--. |", # Dealer
    'Dealer-4': r"| '--' |",

    'Two-1':    r"|2.--. |",
    'Two-4':    r"| '--'2|",

    'Three-1':  r"|3.--. |",
    'Three-4':  r"| '--'3|",

    'Four-1':   r"|4.--. |",
    'Four-4':   r"| '--'4|",

    'Five-1':   r"|5.--. |",
    'Five-4':   r"| '--'5|",

    'Six-1':    r"|6.--. |",
    'Six-4':    r"| '--'6|",

    'Seven-1':  r"|7.--. |",
    'Seven-4':  r"| '--'7|",

    'Eight-1':  r"|8.--. |",
    'Eight-4':  r"| '--'8|",

    'Nine-1':   r"|9.--. |",
    'Nine-4':   r"| '--'9|",

    'Ten-1':    r"|10--. |",
    'Ten-4':    r"| '--10|",

    'Jack-1':   r"|J.--. |",
    'Jack-4':   r"| '--'J|",

    'Queen-1':  r"|Q.--. |",
    'Queen-4':  r"| '--'Q|",

    'King-1':   r"|K.--. |",
    'King-4':   r"| '--'K|",

    'Ace-1':    r"|A.--. |",
    'Ace-4':    r"| '--'A|"
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

### END CARD CLASS ###
    
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

### END DECK CLASS ###
    
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
        self.blackjack = False
        # kinda clunky here, but will display in a good view
        self.displayedHandTop = []
        self.displayedHandLineOne = []
        self.displayedHandLineTwo = []
        self.displayedHandLineThree = []
        self.displayedHandLineFour = []
        self.displayedHandBottom = []


    def starting_deal(self, deck):
        # used once in order to deal 2 cards for starting hand
        for _ in range(2):
            card = deck.deal()
            self.hand.append(card)
            self.add_card_to_display(card)
            
    def hit(self, deck):
        # used every time a player hits
        card = deck.deal()
        self.hand.append(card)
        self.add_card_to_display(card)

    def print_out_card_total(self): #TODO make this a print statement
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
            return total - 10 # no longer an issue here, need a comparison int
        else:
            return total

    def add_card_to_display(self, card):
        # adding cards to the display
        self.displayedHandTop.append(displayHorizontal["Top"])
        self.displayedHandLineOne.append(displayHorizontal[f"{card}-1"])
        self.displayedHandLineTwo.append(displayHorizontal["c-2"])
        self.displayedHandLineThree.append(displayHorizontal["c-3"])
        self.displayedHandLineFour.append(displayHorizontal[f"{card}-4"])
        self.displayedHandBottom.append(displayHorizontal["Bottom"])
        
    def print_out_hand(self, a=0, b=999, c=1, name = True):
        # prints out the cards in the players hand all fancy like
        # rewriting to print horizontal 
        if name:
            print(f"{self.name}'s current hand:")
        print(" ".join(self.displayedHandTop[a:b:c]))
        print(" ".join(self.displayedHandLineOne[a:b:c]))
        print(" ".join(self.displayedHandLineTwo[a:b:c]))
        print(" ".join(self.displayedHandLineThree[a:b:c]))
        print(" ".join(self.displayedHandLineFour[a:b:c]))
        print(" ".join(self.displayedHandBottom[a:b:c]))

    def player_information_printout(self):
        return f"Player {self.name} has {self.bank} in their bank"
    
    def __str__(self):
        return self.name
    
### END PLAYER CLASS ###
    
class Dealer(Player): 
    def __init__(self, name = "Dealer"):
        self.name = name
        self.hand = []
        self.natural = False
        self.bust = False
        self.blackjack = False

        self.displayedHandTop = []
        self.displayedHandLineOne = []
        self.displayedHandLineTwo = []
        self.displayedHandLineThree = []
        self.displayedHandLineFour = []
        self.displayedHandBottom = []

    def starting_deal(self, deck):
        
        for _ in range(2):
            card = deck.deal()
            self.hand.append(card)
            self.add_card_to_display(str(card))

        self.add_card_to_display('Dealer')
        
    
    def initial_hand_display(self):
        print("Dealers initial hand: ")
        
        self.print_out_hand(a=2, b=0,c= -1, name = False)

        self.displayedHandTop.pop()
        self.displayedHandLineOne.pop()
        self.displayedHandLineTwo.pop()
        self.displayedHandLineThree.pop()
        self.displayedHandLineFour.pop()
        self.displayedHandBottom.pop()

    def __str__(self):
        return "Dealer is watching over the game"
    
### END DEALER CLASS ###
    
def slow_type(stringToSlowType):
    # https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
    # used for a more astetically pleasing approach to posting rules as opposed to posting a huge block of text

    if fastType == True:
        typing_speed = 7000 #wpm
    else:
        typing_speed = 500

    for letter in stringToSlowType:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

def resize_terminal():
    system('mode con: cols=150 lines=49')

def intro():
    
    global fastType
    fastType = False
    slow_type("Welcome to Alex's")
    time.sleep(.5)
    fastType = True
    slow_type(gameName)

def print_rules(bigNames = True):
    #separated from into just in case there is a need to add a rules call
    #bigNames can be used to add the ASCII art or take it away
    
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

def initiate_starting_deck():
    global mainDeck 
    mainDeck = Deck()
    mainDeck.shuffle()
    mainDeck.split()

def multiple_players_multiple_decks(amountOfNewDecks):
    # called when requested to be above 1 player, will then add extra decks to match the number of players and then cut the deck

    for i in range(amountOfNewDecks):
        i = Deck()
        mainDeck.combine(i)
    mainDeck.shuffle()
    print(mainDeck.cut())

def player_request():
    # setting the amount of players with recursion to cover errors, then calls extra decks for more than 1 player

    global amountOfPlayers
    temp_player_request = input("Please enter the amount of players from 1 to 7: ")

    if temp_player_request.lower() == 'q':
        input("quitting..")
        quit()

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

    for player in range(amountOfPlayers):
        newPlayer = input(f"Player {player+1}, please enter your name: ")
        
        playersList.append(Player(newPlayer))

def game_mode_selection():
    global gameModeRoundsToPlay
    global gameModeRunOut
    global advancedGame

    #TODO make advaned rules work

    # Can probably make this and "play_until" the same function, only run once at the beginning of the game
    gameModeCheck = input("Default settings for the game is normal rules with runout - that is, player(s) will play until they run out of money\nWould you like to play a specified number of rounds instead? (y/n): ")

    if gameModeCheck.lower() == 'q':
        input("quitting..")
        quit()

    if gameModeCheck.lower() == "y":
        #player would like to play a number of rounds instead of running out

        gameModeRunOut = False
        #error catching for amount of rounds
        while True:
            gameModeCheck = input("Please enter the number of rounds that you would want to play: ")

            if gameModeCheck.lower() == 'q':
                input("quitting..")
                quit()

            try:
                gameModeCheck = int(gameModeCheck)
                gameModeRoundsToPlay = gameModeCheck
                break
            except ValueError:
                print("Please enter a number of rounds to play.")
                continue
    elif gameModeCheck.lower() == "n":
        gameModeRunOut = True
    else:
        print("Please enter y for yes or n for no")
        game_mode_selection()

    while True:
        #error catching for advanced rules
        gameModeCheck = input("Would you like to play by advanced rules including pairs splitting and double downs? (y/n): \nAdvaned rules currently not supported")

        if gameModeCheck.lower() == 'y':
            advancedGame = True
            break
        elif gameModeCheck.lower() == 'n':
            advancedGame = False
            break
        else:
            print("Please enter y for yes or n for no")
            continue
    
def first_round_deal():
    # get the initial deal out for each player and the dealer, and displayes dealer 1 card

    for player in playersList:
        if player.active == False:
            continue
        player.starting_deal(mainDeck)
    
    mxDeal.starting_deal(mainDeck)
    print(mxDeal)
    mxDeal.initial_hand_display()
    
def natural_check():
    # Check for naturals - players first after deal only

    if len(playersList[0].hand) > 2:
        return
    
    for player in playersList:
        if player.active == False:
            continue

        if player.get_card_total() == 21:
            player.natural = True
        else:
            player.natural = False

    if mxDeal.get_card_total() == 21:
        mxDeal.natural = True

def show_all_hands():
    # display the cards for each player 
    # removing this function
    
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
        if cashAvailable == 0:
            n += 1
            continue

        betRequest = input(f"{playersList[n]}, please enter your bet up to $500, you have ${cashAvailable} to bet: ")
        
        if betRequest.lower() == 'q':
            final_thanks_and_final_printout()

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

def player_turn():
    # player turn until all players are finished
    #TODO add advanced logic

    n = 0

    for player in playersList:
        if player.active == False:
            continue

        print(f"{player.name}, it's your turn! You have ${player.bank} and {player.get_card_total()} points in your hand.")
    
        while True:
            player.print_out_hand()
            print(f"Current points = {player.get_card_total()}")
            if player.natural == True:
                print(f"{player.name} has a natural 21 and will get 1.5x their bet.")
                break

            playerAction = input("Now would you like to hit(1) or stay(2)? ")
            if playerAction.lower() == 'q':
                final_thanks_and_final_printout()

            elif playerAction.lower() == 'hit' or playerAction == '1':
                player.hit(mainDeck)
                if player.get_card_total() == 21:
                    player.print_out_hand()
                    print(f"Current points = {player.get_card_total()}")
                    player.blackjack = True
                    print(f"Congratulations {player.name}! You have a blackjack!\nMoving on to next player\n\n")
                    break

                elif player.get_card_total() > 21:
                    player.print_out_hand()
                    print(f"Current points = {player.get_card_total()}")
                    player.bust = True
                    print(f"Bad luck! {player.name} has bust and will lose their bet.\n\n")
                    break
                
            elif playerAction.lower() == 'stay' or playerAction == '2':
                print(f"{player.name} has stayed, moving to next player.\nMoving on to next player\n\n")
                break
                
def dealer_turn():
    # dealer turn, moved dealer natural check here since the original deal only showed 1 card

    print("Dealers turn!")
    mxDeal.print_out_hand()
    dealerPoints = mxDeal.get_card_total()
    print(f"Dealers current points = {dealerPoints}")

    while dealerPoints < 17:
        mxDeal.hit(mainDeck)
        print("Dealer under 17, dealer hits!")
        mxDeal.print_out_hand()
        dealerPoints = mxDeal.get_card_total()
        print(f"Dealers current points = {dealerPoints}")
    
    if dealerPoints == 21:
        if mxDeal.natural == True:
            print("Dealer natural 21!\nEveryone loses their bets unless they also have a natural!")
            return

        print("Dealer BlackJack!")
        mxDeal.blackjack = True
    elif dealerPoints > 21:
        mxDeal.bust = True
        print("Dealer bust!\nEveryone still active wins!")
    
def player_bank_at_zero(player):
    player.active = False
    if player.roundOut == 0:
        player.roundOut = currentRound
        print(f"{player.name} has lost all of their money and has played their final turn during round {currentRound}")

def payout_and_turn_end():
    #repeat until number of rounds is achieved or all players are zeroed out in the bank, must display final point score
    global currentRound
    for player in playersList:
        
        # immeadiatly weed out players that have lost in previous rounds
        if player.active == False:
            continue

        # dealer bust + player has not bust
        elif mxDeal.bust == True and player.bust == False:
            print(f"{player.name} has won {player.bet}!")
            player.bank = player.bank + player.bet
            continue

        # against dealer natural, only way to win is for the player to also have a natural
        elif mxDeal.natural == True: 
            if player.natural == True:
                player.bank = player.bank + player.bet
                print(f"{player.name} has countered a dealer natural with one of their own! You win you bet back!")
                continue
            elif player.natural == False:
                player.bank = player.bank - player.bet
                print(f"{player.name} does not have a natural and lost their bet")
                if player.bank == 0:
                    player_bank_at_zero(player)
                    continue
                continue

        # taking the bet amount away from players that have bust this round
        elif player.bust == True:
            player.bank = player.bank - player.bet
            print(f"{player.name} has bust, and has lost {player.bet}!")
            if player.bank == 0:
                player_bank_at_zero(player)
            continue
        
        # player natural wins 1.5x bet
        elif player.natural == True:
            player.bank = player.bank + (player.bet * 1.5)
            print(f"{player.name} has won with a natural blackjack and has won ${player.bet * 1.5}!")
            continue

        # player 21 pts win
        elif mxDeal.blackjack == False and player.blackjack == True:
            player.bank = player.bank + player.bet
            print(f"{player.name} has won with a 21 and has won ${player.bet}!")
            continue

        # Dealer and player 21 pts, no bank change
        elif mxDeal.blackjack == True and player.blackjack == True:
            print(f"{player.name} has countered a dealer blackjack with one of their own! Your bet has been returned!")
            continue

        # Dealer 21 player loss
        elif mxDeal.blackjack == True:
            player.bank = player.bank - player.bet
            print(f"{player.name} has lost to a dealer blackjack and lost ${player.bet}!")
            if player.bank == 0:
                player_bank_at_zero(player)
            continue

        # Dealer more or equal points to player, player loss    
        elif mxDeal.get_card_total() >= player.get_card_total():
            player.bank = player.bank - player.bet
            print(f"{player.name} has less or equal points to the dealer and has lost ${player.bet}!")
            if player.bank == 0:
                player_bank_at_zero(player)
            continue
        
        # player more points than dealer, player win
        elif player.get_card_total() > mxDeal.get_card_total():
            player.bank = player.bank + player.bet
            print(f"{player.name} has more points to the dealer and has won ${player.bet}!")
            continue

def reset_all(playerCount):
    #this will reset all player hands and check to make sure the deck has enough cards to make it through next round
    global currentRound
    global gameModeRoundsToPlay
    global active

    if currentRound == gameModeRoundsToPlay:
        active = False
        return
    
    this = False
    for player in playersList:
        if player.active == True:
            this = True
    if this == False:
        active = False
        return
    
    mxDeal.blackjack = False
    mxDeal.natural = False
    mxDeal.hand.clear()
    mxDeal.bust = False
    mxDeal.displayedHandTop.clear()
    mxDeal.displayedHandLineOne.clear()
    mxDeal.displayedHandLineTwo.clear()
    mxDeal.displayedHandLineThree.clear()
    mxDeal.displayedHandLineFour.clear()
    mxDeal.displayedHandBottom.clear()

    for player in playersList:
        if player.active == False:
            continue
        player.blackjack = False
        player.natural = False
        player.hand.clear()
        player.bust = False
        player.bet =0
        player.displayedHandTop.clear()
        player.displayedHandLineOne.clear()
        player.displayedHandLineTwo.clear()
        player.displayedHandLineThree.clear()
        player.displayedHandLineFour.clear()
        player.displayedHandBottom.clear()

        #if player.active == False and player.roundOut == currentRound:
        #    print(f"{player.name} has lost after {player.roundOut} rounds")
        print(player.player_information_printout())
    
    if len(mainDeck)/5 <= playerCount:
        #time to reset the deck!
        print(f"Reshuffling the deck! Well done lasting this long everyone :D")
        initiate_starting_deck()

        if playerCount > 1:
            multiple_players_multiple_decks(playerCount - 1)
    
def final_thanks_and_final_printout():
    # final thanks and final printout
    global fastType
    global currentRound

    #fastType = False
    print(f"Game Over!\nCongratulations everyone, current round is {currentRound - 1}, scores are as follows:")

    for player in playersList:
        print(player.player_information_printout())

        if player.active == True:
            print(f"{player.name} has lasted through the whole game")

        else:
            print(f"{player.name} has lost during round {player.roundOut}")

    fastType = True
    slow_type(finalThankText)
    input()
    quit()
    
"""
Basic game logic to follow
after initial setup, looping logic will run until the game is complete
"""

initiate_starting_deck()
mxDeal = Dealer()
resize_terminal()  # eyy it works!!  good to keep in mind for future projects
intro()
time.sleep(1)
print_rules()
# noticing a problem here, the terminal isnt big enough to handle the "advanced rules" all together
# I can split the words but i wanna try resizing the terminal first 
game_mode_selection()
player_request()

while active:
    first_round_deal()
    betting_round()
    #show_all_hands()
    natural_check()
    player_turn()
    dealer_turn()
    payout_and_turn_end()
    reset_all(amountOfPlayers)
    currentRound += 1

final_thanks_and_final_printout()

