

from card import *

class Player:
  def __init__(self,name,chips):
    self.cards=[]
    self.name = name
    self.chips = chips
  def get_card(self,card):
    self.cards.append(card)
  def fold(self):
    self.cards = []
  def call(self):
    pass
  def raise_(self):
    pass



