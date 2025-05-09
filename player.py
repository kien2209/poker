

from card import *

class Player:
  def __init__(self,name,chips):
    self.cards=[]
    self.name = name
    self.chips = chips
    self.role = "None"        # Role can be None (usual player) Dealer, Small Blind, Big Blind
    

  def get_card(self,card):
    self.cards.append(card)
  def fold(self):
    self.cards = []
  def call(self):
    pass
  def raise_(self):
    pass



