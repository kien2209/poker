

from card import *

class Player:
  def __init__(self,name,chip):
    self.cards=[]
  def get_card(self,card):
    self.cards.append(card)
  def fold(self):
    self.cards = []
  def call(self):
    pass
  def raise_(self):
    pass



