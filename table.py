from card import * 
from player import *  

class Table: 
    def __init__(self):
        self.deck = Deck()
        self.cards = []
        self.players = []
        self.pot = 0
        self.folds = []
    
    def print_cards(self):
        s = ""
        for card in self.cards: 
            s += f"{str(card)} "
        print(s)
    
    def print_players(self):
        s = ""
        for player in self.players: 
            s += f"{player.name}: ${player.chips}      "
        print(s)
        
    def add_player(self, name, chips):
        player = Player(name, chips)
        self.players.append(player)
        self.print_players()
    
    def setup(self):
        print(f"Setup, press F to finish")
        while True:
            name = input("Player name: ")
            if name == 'F':
                print("\n \n \n")
                print("Table")
                print("\n \n")
                self.print_players()
                return                      # TODO: change to button 
            
            chips = int(input(f"{name}'s chip: ")) 
            self.add_player(name, chips)

    def round1(self):
        random_card=self.deck.draw()
        self.folds.append(random_card)
        for i in range (3):
              random_card=self.deck.draw()
              self.cards.append(random_card)
    def round2(self):
        random_card=self.deck.draw()
        self.folds.append(random_card)
        random_card=self.deck.draw()
        self.cards.append(random_card)
    def round3(self):
        random_card=self.deck.draw()
        self.folds.append(random_card)
        random_card=self.deck.draw()
        self.cards.append(random_card)
        

    def start(self):
        pass

def main():
    table = Table()
    table.setup()
    table.round1()
    table.print_cards()


if __name__ == "__main__":
    main()