
import random
class Card:
    def __init__(self,rank,suit):
        self.suit=suit
        self.rank=rank
        self.hard, self.soft=self._points()
    def __str__(self):
        return "{0} of {1}".format(str(self.rank), str(self.suit))

class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)
class AceCard(Card):
    def _points(self):
        return 1, 11 
class FaceCard(Card):
    def _points(self):
        return 10, 10
class Suit:
    def __init__(self,name,symbol):
        self.name=name
        self.symbol=symbol
    def __str__(self):
        return "{0} {1}".format(str(self.name), str(self.symbol))
Diamonds, Spades, Hearts, Clubs=Suit('Diamonds','♢'), Suit('Spades', '♠'), Suit('Hearts', '♡'), Suit('Clubs', '♣')
def card1(rank, suit):
    if rank==1: return AceCard(rank, suit)
    elif 2<=rank<11: return NumberCard(rank,suit)
    elif rank==11: return FaceCard('J', suit)
    elif rank==12: return FaceCard('Q', suit)
    elif rank==13: return FaceCard('K', suit)
    else:
        raise IndexError("Rank out of range")
class Deck:
    def __init__(self):
        self._cards=[card1(r+1,s) for r in range(13) for s in (Clubs, Diamonds, Hearts, Spades)]
        random.shuffle(self._cards)
    def pop(self):
        return self._cards.pop()
class Hand(Deck):
    def __init__(self):
        d=Deck()
        self._cards=[d.pop(), d.pop()]
    def hard_total(self):
        return sum(c.hard for c in self._cards)
    def soft_total(self):
        return sum(c.soft for c in self._cards)
    def __str__(self):
        return str([str(c) for c in self._cards])
    def __len__(self):
        return len(self._cards)
    def append(self,value):
        self._cards.append(value)
    def __getitem__(self,i):
        return self._cards[i]
    def __eq__(self, other):
        return self.rank==other.rank
class Table(Hand):
    def __init__(self):
        self.deck=Deck()
#        self.player_list=[d,p]
#    def add_player(self):
#        self.player1=Player()
    def compare_hands(self):
        ranking={}
        for player in self.player_list:
            ranking.update({player.hard_total():player})
        return max(ranking)
                                 
class Player(Hand):
    def get_hand(self):
        self._cards=Hand()
        return self._cards
    def hit(self):
        self._cards.append(d.pop())
        return self._cards.hard_total(), self._cards.__str__()
    def stand(self):
        print(self._cards.hard_total())
    def bet_amount(self,amount):
        self.bet=amount
        print("Bet", self.bet)
    def split(self):
        if len(self._cards)==1:
            if self._cards[0]==self._cards[1]:
                self.hand1=Hand()
                self.hand1.append(self.hand.pop())
            else:
                raise Exception("Cards in hand must have same rank in order to be split.")
        else:
            raise Exception("You can only split your initial hand.")
    def double_down(self):
        if len(self._cards)==2:
            self.bet=self.bet*2
            print("Bet", self.bet)
        else: 
            raise Exception("Cannot double down.")
class Dealer(Player):
    def __init__(self):
        self._cards=self.get_hand()
        self.holecard=self._cards.pop()
    def hit(self):
        a=[int(card.hard) for card in self._cards]
        if len(self._cards)==1:
            self._cards.append(self.holecard)
            return self._cards
        else:
            if sum(a)<18:
                super().hit()
            else:
                self._cards.stand()
                return self._cards.hard_total()                                    
t=Table()
d=Dealer()
p=Player()        
        
            

