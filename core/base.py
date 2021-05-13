import pygame
import sys
from core.input import Input

class Base(object):

    def __init__(self):
        # initialize all pygame modules
        pygame.init()

        # width and height of window
        screenSize = (512,512)

        # indicate rendering options
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

        # create and display the window
        self.screen = pygame.display.set_mode(screenSize, displayFlags)

        # set the title of window
        pygame.display.set_caption("Graphics Window")

        # determine if main loop still active
        self.running = True

        # manage time-related data and operations
        self.clock = pygame.time.Clock()

        # manage user input
        self.input = Input()

    # implement by extending class
    def initialize(self):
        pass

    #implement by extending class
    def update(self):
        pass

    def run(self):

        ## startup ##
        self.initialize()

        ## main loop ##
        while self.running:

            ## proccess input ##
            self.input.update()

            if self.input.quit:
                self.running = False

            ## update ##
            self.update()

            ## render ##

            # display image on screen
            pygame.display.flip()

            # pause if necessary to achieve 60 fps
            self.clock.tick(60)

        ## shutdown ##
        pygame.quit()
        sys.exit()
