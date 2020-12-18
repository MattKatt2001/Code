def main():

    class Cup:
        def __init__(self, size, color):
            self.size = size
            self.color = color
        def drink(self):
            x = int(input("How much do you want to drink "))
            if (self.size - x == 0):
                print("You drank all of it")
            elif (self.size - x < 0):
                print("You can't drink that much")
            else:
                print("You drank " + str(x)+ "ml. There is " + str(self.size - x) + "ml left.")
        def look(self):
            print("This cup is " + self.color + " and is holding " + str(self.size) + "ml of water. ")

    cup1 = Cup(300,"Green")
    cup2 = Cup(200,"Red")
    cup3 = Cup(100, "Blue")

    c = str(input("Do you want to drink from the cup or look at it [Drink, Look, Exit] "))
    if (c == "Look"):
        cup3.look()
    elif (c == "Drink"):
        cup3.drink()
    elif (c == "Exit"):
        quit()
    else:
        print("Please enter a valid choice")

main()

#This is a simple example of oop in python
