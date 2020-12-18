class card:
    def __init__(self,num,s):
        self.num = num
        self.s = s
        self.deck = 52
    def read_card(self):
        print("The " + str(self.num) + " of " + self.s + " in a deck of " + str(self.deck))
