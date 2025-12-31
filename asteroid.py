import pygame
import random

from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    
    def __init__(self,x,y,radius):
        CircleShape.__init__(self,x,y,radius)
        self.vertices = []
        
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
        ass_1.set_shape()
        ass_2.set_shape()
        
    def set_shape(self):
        list_of_vertices = []
        # so I'll go with 6-9 points
        # each point after the first like.. 360/n +/- 60/n degrees rotated from the others
        # and between 0.5 -0.9 of the radius?
        num_points = random.randint(6,10)
        cumulative_angle = 0
        for i in range (0, num_points):
            scalar =  random.uniform(0.5,1) * self.radius
            
            list_of_vertices.append(pygame.Vector2(0, 1).rotate(cumulative_angle) * scalar)
            rand_angle = random.uniform((360/num_points)-(60/num_points),(360/num_points)+(60/num_points))
            cumulative_angle += rand_angle
        self.vertices = list_of_vertices
        
    def asteroid_shape(self):
        
        draw_points = []
        for i in range (1, len(self.vertices)):
            next_point = self.position + self.vertices[i]
            #print(f"{next_point}")
            draw_points.append(next_point)
        #print(f"{draw_points}")
        point_list_xy = [(vector.x, vector.y) for vector in draw_points]
        #print(f"{point_list_xy}")
        return point_list_xy
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white" , self.asteroid_shape(), LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity *dt)
        
        
