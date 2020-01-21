# -*- coding: utf-8 -*-
"""
Created on Sat January 18 1:02 PM 2020

@author: thakkarp
"""

import Dominion
import random
from collections import defaultdict

#Get player names
from projects.thakkarp.dominion import testUtility

player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Define box
box = {}
box["Woodcutter"]=[Dominion.Woodcutter()]*10
box["Smithy"]=[Dominion.Smithy()]*10
box["Laboratory"]=[Dominion.Laboratory()]*10
box["Village"]=[Dominion.Village()]*10
box["Festival"]=[Dominion.Festival()]*10
box["Market"]=[Dominion.Market()]*10
box["Chancellor"]=[Dominion.Chancellor()]*10
box["Workshop"]=[Dominion.Workshop()]*10
box["Moneylender"]=[Dominion.Moneylender()]*10
box["Chapel"]=[Dominion.Chapel()]*10
box["Cellar"]=[Dominion.Cellar()]*10
box["Remodel"]=[Dominion.Remodel()]*10
box["Adventurer"]=[Dominion.Adventurer()]*10
box["Feast"]=[Dominion.Feast()]*10
box["Mine"]=[Dominion.Mine()]*10
box["Library"]=[Dominion.Library()]*10
box["Gardens"]=[Dominion.Gardens()]*nV
box["Moat"]=[Dominion.Moat()]*10
box["Council Room"]=[Dominion.Council_Room()]*10
box["Witch"]=[Dominion.Witch()]*10
box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
box["Militia"]=[Dominion.Militia()]*10
box["Spy"]=[Dominion.Spy()]*10
box["Thief"]=[Dominion.Thief()]*10
box["Throne Room"]=[Dominion.Throne_Room()]*10

supply_order = testUtility.GetSupplyOrder()

#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list,[(k,box[k]) for k in random10])


#The supply always has these cards
supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
supply["Silver"]=[Dominion.Silver()]*40
supply["Gold"]=[Dominion.Gold()]*30
supply["Estate"]=[Dominion.Estate()]*nV
supply["Duchy"]=[Dominion.Duchy()]*nV
supply["Province"]=[Dominion.Province()]*nV
supply["Curse"]=[Dominion.Curse()]*nC

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.GetPlayers(player_names)

#Play the game
turn  = -6
while not Dominion.gameover(supply):
    turn += 1
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
