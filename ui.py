import pygame as pg
from settings import *


class UI:
    def __init__(self):
        """
            Basic UI Setting
            Settings are executed if it doesn't need to be modified
            All UIs use this class as parent class
        """

        self.screen = pg.display.set_mode(flags=pg.FULLSCREEN)

class InGameUI(UI):
    def __init__(self):
        
        """
            UI that used in the actual game playing

            Basic Settings
            - Full Screen
            - idk if needed add plz
        """

        super().__init__()

    def draw(self):
        self.screen.fill(BLACK)

        # Defence zone
        pg.draw.rect(self.screen, GRAY, (0, 0, 1620, 1080), 5)

        # Particle zone
        pg.draw.rect(self.screen, GRAY, (1620, 0, 300, 780), 5)

        # Object zone
        pg.draw.rect(self.screen, GRAY, (1620, 780, 300, 300), 5)


        # Settings

    def event_process(self):
        pass

    def update(self):
        pass