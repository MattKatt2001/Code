class card:

    def __init__(self,num,s):
        self.num = num
        self.s = s
        self.deck = 52

    def __read_card(self):#private method so that you can't write to it
        print("The " + str(self.num) + " of " + self.s + " in a deck of " + str(self.deck))

    def read_card(self):#accsessor in python
        self.__read_card()

    def __draw(self):#doesnt really draw but just a test to -= deck
        self.deck -=1

    def draw(self):
        self.__draw()

card1 = card(10,"Hearts")
