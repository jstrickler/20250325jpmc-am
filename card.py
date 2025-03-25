class  Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
        self.color = "Blue"

    def get_rank(self):  # unpopular :-(
        return self._rank

    @property
    def rank(self):  # getter property
        return self._rank
    
    @rank.setter
    def rank(self, value): # setter property
        #  can validate/modify value here ....
        if isinstance(value, str):
            self._rank = value   #  used with  x.rank = VALUE
        else:
            raise ValueError("rank must be a string")

    @property
    def suit(self):
        return self._suit
    
    # rank = property(rank)

    # human-friendly representation
    def __str__(self):   # str(x)
        return f"{self.rank}-{self.suit}"
    
    # reproducible code
    def __repr__(self):   # repr(x)
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":   # if run as main script, NOT imported
    #  python card.py    NOT    import card
    c1 = Card("8", "Diamonds")
    print(f"{c1.get_rank() = }")
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    
    print(f"{type(Card.get_rank) = }")
    print(f"{type(Card.rank) = }")
    c1.rank = "9"
    print(f"{c1.rank = }")
    
    print(c1)  #  print(str(c1))  str()->repr()
    print(repr(c1))

    print(f"{dir(object) = }")
    print(f"{c1.color = }")
    

