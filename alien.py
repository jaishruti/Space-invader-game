import pygame

class Alien(pygame.sprite.Sprite):
	def __init__(self,name,x,y):
		super().__init__()
		file_path = './assets/' + name + '.png'
		self.surf = pygame.image.load(file_path)
		self.surf = pygame.transform.scale(self.surf,(30,30))
		self.rect = self.surf.get_rect(topleft = (x,y))
		self.speed = 2
		if name == 'bug': self.value = 100
		elif name == 'Alien1': self.value = 200
		else: self.value = 300

	def update(self):
		self.rect.x += self.speed