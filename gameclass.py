from Functions import refresh, Natural, All
#Game Class (gc)
class Game():

    global Multiplesss
    Multiplesss = input("\n\nWhat multiples do you want to learn? \n 1. Refresh (2's through 5's Tables) \n 2. Natural (2's through 10's Tables) \n 3. All (2's through 15's Tables)\n Or Press enter 0 to quit\n > ")
    Multiplesss = int(Multiplesss)

    @classmethod
    def Start(int):
        if(Multiplesss == 1):
            while(refresh() != 0):
                refresh()
        if(Multiplesss == 2):
            while(Natural() != 0):
                Natural()
        if(Multiplesss == 3):
            while(All() != 0):
                All()
        else:
             print("That's not an option. Retry")