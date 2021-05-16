import pygame


class Input(object):

    def __init__(self):

        # has the user quit the app?
        self.quit = False

        # lists to store key states
        #   down, up: discrete events, last for one iteration
        #   pressed:  continuous event, between down and up events
        self.keyDownList    = []
        self.keyPressedList = []
        self.keyUpList      = []

    def update(self):

        # iterate over all user inputs events

        # reset discrete key states
        self.keyDownList = []
        self.keyUpList   = []

        for event in pygame.event.get():
            # quit vent occurs by clicking button to close window
            if event.type == pygame.QUIT:
                self.quit = True
            # check for keydown and keyup events
            # get name of key from event
            # and append to or remove from corresponding lists
            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                self.keyDownList.append(keyName)
                self.keyPressedList.append(keyName)
            if event.type == pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                self.keyPressedList.remove(keyName)
                self.keyUpList.append(keyName)
            if self.isKeyPressed("escape"):
                self.quit = True


    # function to query key states
    def isKeyDown(self, keyName):
        return keyName in self.keyDownList

    def isKeyPressed(self, keyName):
        return keyName in self.keyPressedList

    def isKeyUp(self, keyName):
        return keyName in self.keyUpList