import pygame

class Debug:
  def __init__(self):
      self.fps = 0
  def draw(self, screen):
    font = pygame.font.Font(None, 20)
    font_text = font.render(str(round(self.fps)),1,"Yellow")      
    screen.blit(font_text, (0,0))
  def update(self, clock):
    self.fps = clock.get_fps()
      