from bai import *
from nguoichoi import *

class Table:
  def __init__(self):
    self.deck=Deck()
    self.cards=[]
    self.players=[]
    self.pot=0
    self.folds=[]

  def add_player(self,name,chip):
    player=Player(name,chip)
    self.players.append(player)


  def setup(self):
    pass
  def start(self):
    pass
  def luot1(self):
        random_card=self.deck.draw()
        self.folds.append(random_card)
        for i in range (3):
              random_card=self.deck.draw()
              self.cards.append(random_card)
  def luot2(self):
        random_card=self.deck.draw()
        self.folds.append(random_card)
        random_card=self.deck.draw()
        self.cards.append(random_card)
  def luot3(self):
        random_card=self.deck.draw()
        self.folds.append(random_card)
        random_card=self.deck.draw()
        self.cards.append(random_card)

def main():
    table =Table()
    print(table.folds)
    print(table.cards)
    table.luot1()
    print(table.cards)
main()