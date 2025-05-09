import random



colors = ["Spades", "Hearts", "Diamonds", "Clubs"]
numbers = [i for i in range(1,14)]



class Card:
  def __init__ (self,number,color):
      self.number=number
      self.color=color
  def __str__(self):
    return f"{self.color} {self.number}"

class Deck:
    def __init__(self):
      self.cards=[]
      for color in colors:
         for number in numbers:
            card=Card(color,number)
            self.cards.append(card)
    def shuffle(self):
      random.shuffle(self.cards)
    def draw(self):
       return self.cards.pop()

if __name__ == "__main__":    
  deck=Deck()
  deck.shuffle()


  random_card=deck.draw()

