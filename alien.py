import pygame
speed = 2
class Alien(pygame.sprite.Sprite):
	def __init__(self,name,x,y):
		super().__init__()
		file_path = './assets/' + name + '.png'
		self.surf = pygame.image.load(file_path)
		self.surf = pygame.transform.scale(self.surf,(30,30))
		self.rect = self.surf.get_rect(topleft = (x,y))
		
		if name == 'bug': self.value = 100
		elif name == 'Alien1': self.value = 200
		else: self.value = 300

	def update(self):
		self.rect.x += speed

	def boundary(self):
		global speed
		if self.rect.x-20 < 0 or self.rect.x+60 > 800: 
			speed = -speed
