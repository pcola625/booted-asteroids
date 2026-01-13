import random, glob, pygame
from constants import PEWPEW_SOUND_LOCATION, SOUND_DIR

class AssNoisesGen():
    def __init__(self):
        self.wavfiles = []
        self.init_assfile_list()
        self.die_noise = pygame.mixer.Sound(random.choice(self.wavfiles))
        self.die_noise.set_volume(1)

    def init_assfile_list(self):
        directory = SOUND_DIR  # set directory path
        for filename in glob.iglob(f"{directory}/asteroid_*.wav"):  
            
            self.wavfiles.append(filename) 
    def select_random_ass(self):
        selected_sound = random.choice(self.wavfiles)
        
        self.die_noise = pygame.mixer.Sound(selected_sound)
        self.die_noise.set_volume(1)
    def play_current(self):
        self.die_noise.play()

    def return_random_ass(self):
        selected_sound = random.choice(self.wavfiles)
        return_random_ass = pygame.mixer.Sound(selected_sound)
        return_random_ass.set_volume(random.uniform(0.5,1))
        return return_random_ass
class PewPewGen():
    def __init__(self):
        self.pewpew = pygame.mixer.Sound(PEWPEW_SOUND_LOCATION) 
    def play(self):
        self.pewpew.play()
