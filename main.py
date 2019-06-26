import install_requirements
import casino
import pygame
import sys
import os
import math
import time
import tkinter as tk
from tkinter import messagebox


pygame.init()
cardBack = pygame.image.load(os.path.join('png', 'cardBack.png'))
screen = pygame.display.set_mode((1300, 900))
pygame.display.set_caption('Black Jack')
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('monospace', 70)
smallFont = pygame.font.SysFont('monospace', 30)
bg = pygame.image.load(os.path.join('back', 'background.jpg'))
screen.fill((0,128,0))
clock = pygame.time.Clock()
deck = casino.cards()
cardList = deck.getCards()
d = casino.dealer(cardList)
p = casino.player(cardList)

pygame.display.flip()

onTable = []
topCards = []

cardImg = [None]
    # Load 52 Images
two_clubs = pygame.image.load(os.path.join('png', '2_of_clubs.png'))
two_diamonds = pygame.image.load(os.path.join('png', '2_of_diamonds.png'))
two_hearts = pygame.image.load(os.path.join('png', '2_of_hearts.png'))
two_spades = pygame.image.load(os.path.join('png', '2_of_spades.png'))

three_clubs = pygame.image.load(os.path.join('png', '3_of_clubs.png'))
three_spades = pygame.image.load(os.path.join('png', '3_of_spades.png'))
three_diamonds = pygame.image.load(os.path.join('png', '3_of_diamonds.png'))
three_hearts = pygame.image.load(os.path.join('png', '3_of_hearts.png'))

four_clubs = pygame.image.load(os.path.join('png', '4_of_clubs.png'))
four_spades = pygame.image.load(os.path.join('png', '4_of_spades.png'))
four_diamonds = pygame.image.load(os.path.join('png', '4_of_diamonds.png'))
four_hearts = pygame.image.load(os.path.join('png', '4_of_hearts.png'))

five_clubs = pygame.image.load(os.path.join('png', '5_of_clubs.png'))
five_spades = pygame.image.load(os.path.join('png', '5_of_spades.png'))
five_diamonds = pygame.image.load(os.path.join('png', '5_of_diamonds.png'))
five_hearts = pygame.image.load(os.path.join('png', '5_of_hearts.png'))

six_clubs = pygame.image.load(os.path.join('png', '6_of_clubs.png'))
six_spades = pygame.image.load(os.path.join('png', '6_of_spades.png'))
six_diamonds = pygame.image.load(os.path.join('png', '6_of_diamonds.png'))
six_hearts = pygame.image.load(os.path.join('png', '6_of_hearts.png'))

seven_clubs = pygame.image.load(os.path.join('png', '7_of_clubs.png'))
seven_spades = pygame.image.load(os.path.join('png', '7_of_spades.png'))
seven_diamonds = pygame.image.load(os.path.join('png', '7_of_diamonds.png'))
seven_hearts = pygame.image.load(os.path.join('png', '7_of_hearts.png'))

eight_clubs = pygame.image.load(os.path.join('png', '8_of_clubs.png'))
eight_spades = pygame.image.load(os.path.join('png', '8_of_spades.png'))
eight_diamonds = pygame.image.load(os.path.join('png', '8_of_diamonds.png'))
eight_hearts = pygame.image.load(os.path.join('png', '8_of_hearts.png'))

nine_clubs = pygame.image.load(os.path.join('png', '9_of_clubs.png'))
nine_spades = pygame.image.load(os.path.join('png', '9_of_spades.png'))
nine_diamonds = pygame.image.load(os.path.join('png', '9_of_diamonds.png'))
nine_hearts = pygame.image.load(os.path.join('png', '9_of_hearts.png'))

ten_clubs = pygame.image.load(os.path.join('png', '10_of_clubs.png'))
ten_spades = pygame.image.load(os.path.join('png', '10_of_diamonds.png'))
ten_diamonds = pygame.image.load(os.path.join('png', '10_of_hearts.png'))
ten_hearts = pygame.image.load(os.path.join('png', '10_of_spades.png'))

jack_clubs = pygame.image.load(os.path.join('png', 'jack_of_clubs.png'))
jack_spades = pygame.image.load(os.path.join('png', 'jack_of_spades.png'))
jack_diamonds = pygame.image.load(os.path.join('png', 'jack_of_diamonds.png'))
jack_hearts = pygame.image.load(os.path.join('png', 'jack_of_hearts.png'))

queen_clubs = pygame.image.load(os.path.join('png', 'queen_of_clubs.png'))
queen_spades = pygame.image.load(os.path.join('png', 'queen_of_spades.png'))
queen_diamonds = pygame.image.load(os.path.join('png', 'queen_of_diamonds.png'))
queen_hearts = pygame.image.load(os.path.join('png', 'queen_of_hearts.png'))

king_clubs = pygame.image.load(os.path.join('png', 'king_of_clubs.png'))
king_spades = pygame.image.load(os.path.join('png', 'king_of_spades.png'))
king_diamonds = pygame.image.load(os.path.join('png', 'king_of_diamonds.png'))
king_hearts = pygame.image.load(os.path.join('png', 'king_of_hearts.png'))

ace_clubs = pygame.image.load(os.path.join('png', 'ace_of_clubs.png'))
ace_spades = pygame.image.load(os.path.join('png', 'ace_of_spades.png'))
ace_diamonds = pygame.image.load(os.path.join('png', 'ace_of_diamonds.png'))
ace_hearts = pygame.image.load(os.path.join('png', 'ace_of_hearts.png'))

cardImg.append([ace_clubs, ace_diamonds, ace_hearts, ace_spades])
cardImg.append([two_clubs, two_diamonds, two_hearts, two_spades])
cardImg.append([three_clubs, three_diamonds, three_hearts, three_spades])
cardImg.append([four_clubs, four_diamonds, four_hearts, four_spades])
cardImg.append([five_clubs, five_diamonds, five_hearts, five_spades])
cardImg.append([six_clubs, six_diamonds, six_hearts, six_spades])
cardImg.append([seven_clubs, seven_diamonds, seven_hearts, seven_spades])
cardImg.append([eight_clubs, eight_diamonds, eight_hearts, eight_spades])
cardImg.append([nine_clubs, nine_diamonds, nine_hearts, nine_spades])
cardImg.append([ten_clubs, ten_diamonds, ten_hearts, ten_spades])
cardImg.append([jack_clubs, jack_diamonds, jack_hearts, jack_spades])
cardImg.append([queen_clubs, queen_diamonds, queen_hearts, queen_spades])
cardImg.append([king_clubs, king_diamonds, king_hearts, king_spades])

one = pygame.image.load(os.path.join('chips', '1.png'))
two = pygame.image.load(os.path.join('chips', '2.png'))
five = pygame.image.load(os.path.join('chips', '5.png'))
ten = pygame.image.load(os.path.join('chips', '10.png'))
twenty = pygame.image.load(os.path.join('chips', '20.png'))

didBet = False
betChips = 0
chips = []
betArray = []
playerChips = 50

chips.append([one, 20, 225, 1])
chips.append([two, 20, 300, 2])
chips.append([five, 20, 375, 5])
chips.append([ten, 20, 450, 10])
chips.append([twenty, 20, 525, 20])


def lost():
    screen.fill((0,128,0))
    label = myfont.render('Press any key to play again', 1, (255,255,255))
    label2 = myfont.render('Out of Chips...', 1, (255,255,255))
    screen.blit(label, (100, 450))
    screen.blit(label2, (350, 350))
    pygame.display.update()
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            firstStart()
            break
        if ev.type == pygame.QUIT:
            pygame.quit()


def bet():
    global betChips
    global playerChips
    label = myfont.render('Please place your bet: ', 1, (255,255,255))
    screen.blit(label, (230, 430))
    updateChips()
    pygame.display.update()
    while True:
        label = smallFont.render('Press space when finished', 1, (255, 255, 255))
        screen.blit(label, (430, 850))
        updateChips()
        pygame.display.update()
        ev = pygame.event.poll()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i in range(len(chips)):
                if pos[0] > chips[i][1] and pos[0] < chips[i][1] + 50:
                    if pos[1] > chips[i][2] and pos[1] < chips[i][2] + 50:
                        if playerChips - chips[i][3] >= 0:
                            betChips += chips[i][3]
                            dealChips(chips[i][0], 525 + i * 50, 550, chips[i][1], chips[i][2])
                            playerChips -= chips[i][3]
                        else:
                            root = tk.Tk()
                            messagebox.showinfo('Not enough chips!', ('You do not have enough \n chips to bet that amount, \n your current amount of chips is ' + str(playerChips)))
                            try:
                                root.destroy()
                            except:
                                pass
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.KEYDOWN:
            if betChips >= 1:
                pygame.draw.rect(screen, (0, 128, 0), (429, 849, 600, 100))
                break


def drawChip(img, x, y):
    w = 50
    h = 50
    newIMG = pygame.transform.scale(img, (w, h))
    screen.blit(newIMG, (x,y))


def firstStart():
    global playerChips
    reset()
    playerChips = 50
    screen.fill((0,128,0))
    label = myfont.render('Welcome to Black Jack!', 1, (255, 255, 255))
    label2 = myfont.render('Press space to start', 1, (255,255,255))
    screen.blit(label2, (225, 550))
    screen.blit(label, (175, 400))
    pygame.display.update()
    pygame.init()

    while True:
        clock.tick(60)
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.KEYDOWN:
            dealplayer(675, 650)
            dealplayer(500, 650)
            dealplayer(675, 50)
            dealplayer(500, 50)
            bet()
            main()

def restart():
    global playerChips
    screen.fill((0,128,0))
    pygame.display.update()
    pygame.init()

    if playerChips == 0:
        lost()

    while True:
        clock.tick(60)
        dealplayer(675, 650)
        dealplayer(500, 650)
        dealplayer(675, 50)
        dealplayer(500, 50)
        bet()
        main()

def reset():
    global onTable
    global cardImg
    global topCards
    global didBet
    global betChips
    global betArray
    betArray = []
    onTable = []
    topCards = []
    didBet = False
    betChips = 0
    time.sleep(1)


def dealChips(img, x, y, s, w):
    endx = x
    endy = y
    movex = s
    movey = w
    x_dist = x - s
    y_dist = y - w
    constant_x = x_dist / 50
    constant_y = y_dist / 30

    for i in range(100):
        if movey >= endy and movex >= endx:
            break
        else:
            screen.fill((0, 128, 0))
            drawChip(img, movex, movey)
            if movex <= endx:
                movex += constant_x
            if movey <= endy:
                movey += constant_y

        for d in range(len(onTable)):
            drawCard(onTable[d][0], onTable[d][1], onTable[d][2])

        for i in range(len(chips)):
            drawChip(chips[i][0], chips[i][1], chips[i][2])

        for q in range(len(betArray)):
            drawChip(betArray[q][0], betArray[q][1], betArray[q][2])

        clock.tick(50)
        drawCard(cardBack, 15, 15)
        updateChips()
        pygame.display.update()

    betArray.append([img, movex, movey])


def dealplayer(x,y):
    endx = x
    endy = y
    movex = 0
    movey = 0

    h = math.sqrt(endx**2 + endy**2)

    for i in range(round(h / 10)):
        screen.fill((0, 128, 0))
        movex += endx / (h/10)
        movey += endy / (h/10)
        drawCard(cardBack, movex, movey)
        for d in range(len(onTable)):
            drawCard(onTable[d][0], onTable[d][1], onTable[d][2])

        for i in range(len(chips)):
            drawChip(chips[i][0], chips[i][1], chips[i][2])

        for w in range(len(betArray)):
            drawChip(betArray[w][0], betArray[w][1], betArray[w][2])

        clock.tick(50)
        drawCard(cardBack, 15, 15)
        updateChips()
        pygame.display.update()

    onTable.append([cardBack, x, y])

def dealplayerHit(hit,x,y):
    endx = x
    endy = y
    movex = 0
    movey = 0

    h = math.sqrt(endx**2 + endy**2)

    for i in range(round(h / 10)):
        screen.fill((0, 128, 0))
        updateChips()
        movex += endx / (h/10)
        movey += endy / (h/10)
        drawCard(cardBack, movex, movey)
        for d in range(len(onTable)):
            drawCard(onTable[d][0], onTable[d][1], onTable[d][2])
        for i in range(len(chips)):
            drawChip(chips[i][0], chips[i][1], chips[i][2])

        for w in range(len(betArray)):
            drawChip(betArray[w][0], betArray[w][1], betArray[w][2])
        drawCard(cardBack, 15, 15)
        clock.tick(50)
        pygame.display.update()

    onTable.append([hit, x, y])


def cardImage(n, suit):

    if suit == 'C':
        return cardImg[n][0]
    elif suit == 'D':
        return cardImg[n][1]
    elif suit == 'H':
        return cardImg[n][2]
    elif suit == 'S':
        return cardImg[n][3]


def updateChips():
    global playerChips
    pygame.draw.rect(screen, (0,128,0), (39, 585, 200, 40), 0)
    label = smallFont.render('Chips: ' + str(playerChips), 1, (255,255,255))
    screen.blit(label, (10, 585))


def updateScore(turn=False):
    dScore = d.getScore()
    pScore = p.getScore()
    score1 = smallFont.render(str(dScore), 1, (255,255,255))
    score2 = smallFont.render(str(pScore), 1, (255, 255, 255))
    screen.blit(score2, (1150, 700))
    if turn:
        screen.blit(score1, (1150, 50))


def drawCard(img, x, y):
    white = (255, 255, 255)
    w = 130
    h = 181
    pygame.draw.rect(screen, white, (x - 5, y - 4, w + 10, h + 8), 0)
    newIMG = pygame.transform.scale(img, (w, h))
    screen.blit(newIMG, (x,y))


def main():
    # DRAWING AND INIT
    # VARIABLES
    global d
    global p
    global playerChips
    deck = casino.cards()
    cardList = deck.getCards()
    d = casino.dealer(cardList)
    p = casino.player(cardList)
    playerCards = p.deal()
    dealerCards = d.deal()
    allowHit = False
    playerReveal = False
    playerTurn = True
    playerStay = False
    onTable[2] = [cardImage(dealerCards[0][0], dealerCards[0][1]), 675, 50]
    onTable[3] = [cardBack, 500, 50]
    while True:

        pygame.display.update()
        clock.tick(60)
        # PLAYER DECISION
        if playerReveal == False:
            drawCard(cardBack, 675, 650)
            drawCard(cardBack, 500, 650)
            label = smallFont.render('Press space to reveal cards', 1, (255,255,255))
            screen.blit(label, (430, 850))
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    # Show cards
                    playerReveal = True
                    allowHit = True
                    drawCard(cardImage(playerCards[0][0], playerCards[0][1]), 675, 650)
                    drawCard(cardImage(playerCards[1][0], playerCards[1][1]), 500, 650)
                    onTable[0] = [cardImage(playerCards[0][0], playerCards[0][1]), 675, 650]
                    onTable[1] = [cardImage(playerCards[1][0], playerCards[1][1]), 500, 650]
                    pygame.draw.rect(screen, (0, 128, 0), (429, 849, 550, 100))
            pygame.display.update()
        else:
            label = smallFont.render('Press space to hit and tab to stay', 1, (255, 255, 255))
            screen.blit(label, (350, 850))
            updateScore()
            pygame.display.update()

            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_TAB:
                    playerStay = True
                    updateScore(True)
                if ev.key == pygame.K_SPACE:

                    if allowHit:
                        hitCard = p.hit()
                        if len(p.cards) == 3:
                            dealplayerHit(cardImage(hitCard[0], hitCard[1]), 325, 650)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 325, 650)
                            updateScore()
                        elif len(p.cards) == 4:
                            dealplayerHit(cardImage(hitCard[0], hitCard[1]), 850, 650)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 850, 650)
                            updateScore()
                        elif len(p.cards) == 5:
                            dealplayerHit(cardImage(hitCard[0], hitCard[1]), 150, 650)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 150, 650)
                            updateScore()
                        elif len(p.cards) == 6:
                            dealplayerHit(cardImage(hitCard[0], hitCard[1]), 1025, 650)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 1025, 650)
                            updateScore()
                    allowHit = True
                    pygame.display.update()

            if p.getScore() > 21:
                label = myfont.render('You Went Over 21 :(', 1, (255,255,255))
                screen.blit(label, (300, 430))
                allowHit = False
                updateChips()
                pygame.display.update()
                time.sleep(1)
                pygame.draw.rect(screen, (0,128,0), (0, 640, 1300,200))
                pygame.draw.rect(screen, (0, 128, 0), (200, 40, 1300, 200))
                pygame.display.update()
                break

            elif p.getScore() == 21 and len(p.cards) == 2:
                allowHit = False
                playerChips += betChips * 3
                label = myfont.render('BLACK JACK!', 1, (255, 255, 255))
                screen.blit(label, (420, 430))
                updateChips()
                pygame.display.update()
                time.sleep(1)
                pygame.draw.rect(screen, (0, 128, 0), (0, 640, 1300, 200))
                pygame.draw.rect(screen, (0, 128, 0), (200, 40, 1300, 200))
                pygame.display.update()
                break

            elif playerStay:
                playerTurn = False
                allowHit = False
                updateScore()
                pygame.display.update()

# ---------------------------------------------------------------------------------------------------------
        # DEALER

        if playerTurn == False:
            drawCard(cardImage(dealerCards[1][0], dealerCards[1][1]), 500, 50)
            try:
                ind = onTable.index([cardBack, 500, 50])
                onTable[ind] = [cardImage(dealerCards[1][0], dealerCards[1][1]), 500, 50]
            except:
                pass
            updateScore()
            if len(d.cards) > 2:
                dealplayerHit(cardImage(dealerCards[2][0], dealerCards[2][1]), 325, 50)
                drawCard(cardImage(dealerCards[2][0], dealerCards[2][1]), 325, 50)
                pygame.display.update()
                time.sleep(0.3)
            if len(d.cards) > 3:
                dealplayerHit(cardImage(dealerCards[3][0], dealerCards[3][1]), 850, 50)
                drawCard(cardImage(dealerCards[3][0], dealerCards[3][1]), 850, 50)
                pygame.display.update()
                time.sleep(0.3)
            if len(d.cards) > 4:
                dealplayerHit(cardImage(dealerCards[4][0], dealerCards[4][1]), 150, 50)
                drawCard(cardImage(dealerCards[4][0], dealerCards[4][1]), 150, 50)
                pygame.display.update()
                time.sleep(0.3)
            if len(d.cards) > 5:
                dealplayerHit(cardImage(dealerCards[5][0], dealerCards[5][1]), 1025, 50)
                drawCard(cardImage(dealerCards[5][0], dealerCards[5][1]), 1025, 50)
                pygame.display.update()
                time.sleep(0.3)
            updateScore(True)

            if d.getScore() > p.getScore():
                if d.getScore() < 22:
                    label = myfont.render('You Lost', 1, (255,255,255))
                    screen.blit(label, (510, 430))
                    updateChips()
                    pygame.display.update()
                    break
                else:
                    playerChips += betChips * 2
                    label = myfont.render('Dealer Bust\'s, You Win', 1, (255,255,255))
                    screen.blit(label, (230, 430))
                    updateChips()
                    pygame.display.update()
                    break
            elif d.getScore() < p.getScore():
                playerChips += betChips * 2
                label = myfont.render('Winner!', 1, (255,255,255))
                screen.blit(label, (475, 430))
                updateChips()
                pygame.display.update()
                break
            else:
                playerChips += betChips
                label = myfont.render('Tie', 1, (255,255,255))
                screen.blit(label, (600, 450))
                updateChips()
                pygame.display.update()
                break
        else:
            drawCard(cardImage(dealerCards[0][0], dealerCards[0][1]), 675, 50)
            drawCard(cardBack, 500, 50)
    time.sleep(1)

    reset()
    restart()

firstStart()


