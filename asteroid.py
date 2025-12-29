import pygame
import random

from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    
    def __init__(self,x,y,radius):
        CircleShape.__init__(self,x,y,radius)
        
    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        log_event("asteroid_split")
        theta = random.uniform(20,50)
        left_vector = self.velocity.rotate(theta)
        right_vector = self.velocity.rotate(-theta)
        new_radii = self.radius - ASTEROID_MIN_RADIUS
        ass_1 = Asteroid(self.position.x, self.position.y, new_radii)
        ass_2 = Asteroid(self.position.x, self.position.y, new_radii)
        ass_1.velocity = left_vector * 1.2
        ass_2.velocity = right_vector * 1.2
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white" ,self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity *dt)
        
        
