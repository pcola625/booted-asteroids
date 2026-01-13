"""
//  shot.py
//  
//
//  Created by Pete Colasacco on 12/28/25.
//  but filled in from details on boot.dev
"""
import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        shot_fired = pygame.mixer.Sound("sounds/pew-pew.wav")
        shot_fired.set_volume(1)
        shot_fired.play()
    def draw(self, screen):
        pygame.draw.circle(screen, "white" ,self.position, self.radius, LINE_WIDTH)
    
    def update(self,dt):
        self.position += (self.velocity *dt)
    


