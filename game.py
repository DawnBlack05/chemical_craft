from ui import InGameUI
import pygame as pg
from objects import Object
from typing import TypedDict, Dict, List

class gamedata(TypedDict):
    Deck : List[int]
    Possessed_particles : Dict[int, int]
    Objects : List[Object]

class Game:
    def __init__(self):
        self.ui = InGameUI()
        self.clock = pg.time.Clock()

        self.data : gamedata = {
            'Deck' : [],                                            # particles in deck
            'Possessed_particles' : {                               # particles : particles_count which are in deck
                particle : 0 for particle in self.data['Deck']
            },
            'Objects' : []                                          # objects that should be drawn in 'Object Zone'
        }


        # data - object updating
        total = 0
        for particle, count in self.data['Possessed_particles'].items()[::-1] :
            total += count
            if total < 40:
                self.data['Objects'].extend([Object(particle)] * count)
            elif total - count < 40:
                self.data['Objects'].extend([Object(particle)] * 40 - total)
            else:
                break

    def step(self):
        """This function is used to show the game's states in the screen"""
        self.ui.draw()

    def update(self):
        """This function is used to update the game's states"""


        """
            time to particles.

            variables
            - particle_summon_time : time to stay until next particle summoning

            algorithm

            <In Game Situation>
            1. if particle_summon_time is passed, add particle in data-Possessed_particles.
            2. if request to craft something given, check if it's available.
                if it is, send InGameUI to choose some particles to be crafted and vacuum them.
                    if vacuumming ended, delete the vacuummed ones and add the crafted one in data-Possessed_particles.
                if it isn't, order InGameUi to inform that it's not available with sound and actual message.
            3. check the craftings' availablity.
            4. update data-Objects; just copy the data-Possessed_particles.
            5. idk something else?

        """
        


        pg.display.update()
        self.clock.tick(60)

    def end(self):
        """This functions check whether to finish the game"""
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return True