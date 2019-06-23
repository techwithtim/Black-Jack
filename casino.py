
import random
# Card Value
# 1: Ace
# 2 - 10: 2 - 10
# 11: Jack
# 12: Queen
# 13: King
# Suits
# H: Hearts
# D: Diamonds
# C: Clubs
# S: Spades


class cards:
    def __init__(self):
        self.cardsL = []
        for x in range(1,14):
            card = x
            for i in range(4):
                if i == 0:
                    suit = 'H'
                elif i == 1:
                    suit = 'D'
                elif i == 2:
                    suit = 'C'
                elif i == 3:
                    suit = 'S'
                self.cardsL.append([card, suit])
                
        self.cardsL = self.cardsL * 4

    def getCards(self):
        return self.cardsL
        

class dealer:
    def __init__(self, c):
        # 4 decks
        self.curValue = 0
        self.cardsL = c
        self.cards = []

    def deal(self):
        r1 = random.randint(0, len(self.cardsL) - 1)
        randCard = self.cardsL[r1]
        self.cardsL.pop(r1)
        self.cards.append(randCard)
        
        r2 = random.randint(0, len(self.cardsL) - 1)
        randCard2 = self.cardsL[r2]
        self.cardsL.pop(r2)
        self.cards.append(randCard2)

        self.decision()
        return self.cards

    def decision(self):
        value = 0
        if self.cards[0][0] == 1 and self.cards[1][0] == 1:
            value = 2
        else:
            if self.cards[0][0] == 11 or self.cards[0][0] == 12 or self.cards[0][0] == 13:
                value += 10
            else:
                value += self.cards[0][0]
            if self.cards[1][0] == 11 or self.cards[1][0] == 12 or self.cards[1][0] == 13:
                value += 10
            else:
                value += self.cards[1][0]

        self.curValue = value

        if value == 11 and (self.cards[0][0] == 1 or self.cards[1][0] == 1):
            self.curValue = 21
            return self.curValue
        elif value < 17:
            self.hit()
        else:
            return self.curValue

    def hit(self):
        value = 0
        rand = random.randint(1, len(self.cardsL))
        card = self.cardsL[rand]
        self.cards.append(card)
        self.cardsL.pop(rand)

        if card[0] == 11 or card[0] == 12 or card[0] == 13:
            value = 10
        elif card[0] == 1 and self.curValue == 10:
            value = 11
        elif card[0] == 1 and self.curValue < 11:
            value = 11
        elif card[0] == 1 and self.curValue == 20:
            value = 1
        else:
            value = card[0]

        self.curValue += value
        if self.curValue < 17:
            self.hit()
        elif self.curValue > 21:
            return self.curValue
        else:
            return self.curValue

    def getScore(self):
        return self.curValue

    def reset(self):
        self.cards = []
        self.curValue = 0


class player():
    def __init__(self, c):
        self.cardsL = c
        self.cards = []
        self.curValue = 0

    def deal(self):
        r1 = random.randint(0, len(self.cardsL) - 1)
        randCard = self.cardsL[r1]
        self.cardsL.pop(r1)
        self.cards.append(randCard)

        r2 = random.randint(0, len(self.cardsL) - 1)
        randCard2 = self.cardsL[r2]
        self.cardsL.pop(r2)
        self.cards.append(randCard2)

        self.cardsL = self.cardsL

        value = 0
        if self.cards[0][0] == 11 or self.cards[0][0] == 12 or self.cards[0][0] == 13:
            value += 10
        else:
            value += self.cards[0][0]
        if self.cards[1][0] == 11 or self.cards[1][0] == 12 or self.cards[1][0] == 13:
            value += 10
        else:
            value += self.cards[1][0]

        self.curValue = value

        if value == 11 and (self.cards[0][0] == 1 or self.cards[1][0] == 1):
            self.curValue = 21


        return self.cards

    def hit(self):
        value = 0
        rand = random.randint(1,len(self.cardsL))
        card = self.cardsL[rand]
        self.cards.append(card)
        self.cardsL.pop(rand)

        if card[0] == 11 or card[0] == 12 or card[0] == 13:
            value = 10
        elif card[0] == 1 and self.curValue == 10:
            value = 11
        elif card[0] == 1 and self.curValue < 11:
            value = 11
        elif card[0] == 1 and self.curValue == 20:
            value = 1
        else:
            value = card[0]

        self.curValue += value
        if self.curValue > 21 and self.cards.__contains__(1):
            if self.cards.count(1) == 1:
                if self.curValue - 10 < 22:
                    self.curValue = self.curValue - 10


        return card

    def getScore(self):
        return self.curValue


c = cards()
deck = c.getCards()
d = dealer(deck)
p = player(deck)



