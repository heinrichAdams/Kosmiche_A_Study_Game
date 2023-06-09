import pygame


# <<<<<<<<<<<<<<<<<< TIMER CLASS

class Timer:

    def __init__(self, duration, function=None, end_function=None):
        self.duration = duration
        self.function = function
        self.end_function = end_function
        self.start_time = 0
        self.active = False

    def start(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def end(self):
        if self.end_function != None:
            self.end_function()
        self.active = False
        self.start_time = 0
        return True

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.function and self.active:
            self.function()
        if current_time - self.start_time >= self.duration:
            self.end()

# >>>>>>>>>>>>>>>>>> TIMER CLASS
