import pygame
from pygame.locals import *

class App:
    
    # initializes all PyGame modules. 
    # then it creates the main display
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 1600, 800
    
    # calls pygame.init() & sets _running to true 
    def on_init(self):    
        pygame.init()
        self._display_surf= pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    # check if use has quit (clicked close) 
    # if so sets _running to False breaking the game loop
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    # calls pygame.quit() to quit all pygame modules
    def on_cleanup(self):
        pygame.quit()

    # initialize pygame then enter the main game loop
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        # main game loop (while the game is running)
        while( self._running ):

            # check event calls
            for event in pygame.event.get():
                self.on_event(event)

            # compute & render everything
            self.on_loop()
            self.on_render()
            
        # will clean up before quitting
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()