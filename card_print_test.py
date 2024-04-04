"""
Created by Alex Norment
on 3/11/24

This is a test of writing out card ASCII art in a row as opposed to a column
and will be ported to the ZtH milestone 2 project
"""
"""
OK, so I see 4 lines that are similar enough to eachother that they can be the same with the exception of one for one card
Looking at the designs, there are repeats of each line here and here, possible to use .format strings to reduce even more
"""

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.handDict = {}
        self.handTop = []
        self.handLnOne = []
        self.handLnTwo = []
        self.handLnThree = []
        self.handLnFour = []
        self.handBottom = []

def add_card_to_hand(player, card):
    player.handTop.append(lineStyle['top'])
    player.handLnOne.append(lineStyle[f'{card}-1'])
    player.handLnTwo.append(lineStyle[f'{card}-2'])
    player.handLnThree.append(lineStyle[f'{card}-3'])
    player.handLnFour.append(lineStyle[f'{card}-4'])
    player.handBottom.append(lineStyle['bottom'])

def add_card_to_hand_two(player, card):
    player.handTop.append(lineStyle['top'])
    player.handLnOne.append(lineStyle[f'{card}-1'])
    player.handLnTwo.append(lineStyle['c-2'])
    player.handLnThree.append(lineStyle['c-3'])
    player.handLnFour.append(lineStyle[f'{card}-4'])
    player.handBottom.append(lineStyle['bottom'])

def print_out_hand(player):
    print(" ".join(player.handTop))
    print(" ".join(player.handLnOne))
    print(" ".join(player.handLnTwo))
    print(" ".join(player.handLnThree))
    print(" ".join(player.handLnFour))
    print(" ".join(player.handBottom))
    pass

lineStyle = {
    #Top and bottom cards are the same throughout
    #only needing to change the middle lines
    'top':      r".------.",
    'bottom':   r"`------'",

    'c-2':      r"| |A+| |",
    'c-3':      r"| |+N| |",

    'd-1':      r"| .--. |",
    'd-2':      r"| :/\: |",
    'd-3':      r"| :\/: |",
    'd-4':      r"| '--' |",

    '2-1':      r"|2.--. |",
    '2-2':      r"| (\/) |",
    '2-3':      r"| :\/: |",
    '2-4':      r"| '--'2|",

    '3-1':      r"|3.--. |",
    '3-2':      r"| :(): |",
    '3-3':      r"| ()() |",
    '3-4':      r"| '--'3|",

    '4-1':      r"|4.--. |",
    '4-2':      r"| :/\: |",
    '4-3':      r"| :\/: |",
    '4-4':      r"| '--'4|",

    '5-1':      r"|5.--. |",
    '5-2':      r"| :/\: |",
    '5-3':      r"| (__) |",
    '5-4':      r"| '--'5|",

    '6-1':      r"|6.--. |",
    '6-2':      r"| (\/) |",
    '6-3':      r"| :\/: |",
    '6-4':      r"| '--'6|",

    '7-1':      r"|7.--. |",
    '7-2':      r"| :(): |",
    '7-3':      r"| ()() |",
    '7-4':      r"| '--'7|",

    '8-1':      r"|8.--. |",
    '8-2':      r"| :/\: |",
    '8-3':      r"| :\/: |",
    '8-4':      r"| '--'8|",

    '9-1':      r"|9.--. |",
    '9-2':      r"| :/\: |",
    '9-3':      r"| (__) |",
    '9-4':      r"| '--'9|",

    '10-1':     r"|10--. |",
    '10-2':     r"| :/\: |",
    '10-3':     r"| (__) |",
    '10-4':     r"| '--10|",

    'J-1':      r"|J.--. |",
    'J-2':      r"| :(): |",
    'J-3':      r"| ()() |",
    'J-4':      r"| '--'J|",

    'Q-1':      r"|Q.--. |",
    'Q-2':      r"| (\/) |",
    'Q-3':      r"| :\/: |",
    'Q-4':      r"| '--'Q|",

    'K-1':      r"|K.--. |",
    'K-2':      r"| :/\: |",
    'K-3':      r"| :\/: |",
    'K-4':      r"| '--'K|",

    'A-1':      r"|A.--. |",
    'A-2':      r"| (\/) |",
    'A-3':      r"| :\/: |",
    'A-4':      r"| '--'A|"
}

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

john = Player('John')
joe = Player('Joe')
add_card_to_hand(john, '2')
add_card_to_hand(john, 'd')
add_card_to_hand(john, '5')

add_card_to_hand_two(joe, '2')
add_card_to_hand_two(joe, 'd')
add_card_to_hand_two(joe, '5')

print_out_hand(john)
print_out_hand(joe)