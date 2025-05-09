import random

colors = ["Club", "Diamond", "Heart", "Spade"]
numbers = [i for i in range(1,14)]

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    
    def __str__(self):
        return f"{self.color} {self.number}"

class Deck: 
    def __init__(self):
        self.cards = []
        for color in colors: 
            for number in numbers:
                card = Card(color, number)
                self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    for card in deck.cards:
        print(card.number, card.color)


    random_card = deck.draw()
    print(len(deck.cards))
    print(random_card)
