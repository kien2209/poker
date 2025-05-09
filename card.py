import random

colors = ["♣️", "♦️", "❤️", "♠️"]
numbers = [i for i in range(1,14)]
special_names = ["J", "Q", "K", "A"]
special_numbers = [11, 12, 13, 1]

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    
    def __str__(self):
        number = self.number
        if self.number in special_numbers:
            number = special_names[special_numbers.index(self.number)]
        return f"{self.color} {number}"

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


    random_card = deck.draw()
    print(random_card)
