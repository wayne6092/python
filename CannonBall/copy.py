import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = True
		self.sprites = []
		self.sprites.append(pygame.image.load('explosion1.bmp'))
		self.sprites.append(pygame.image.load('explosion2.bmp'))
		self.sprites.append(pygame.image.load('explosion3.bmp'))
		self.sprites.append(pygame.image.load('explosion4.bmp'))
		self.sprites.append(pygame.image.load('explosion5.bmp'))
		self.sprites.append(pygame.image.load('explosion6.bmp'))
		self.sprites.append(pygame.image.load('explosion7.bmp'))
		self.sprites.append(pygame.image.load('explosion8.bmp'))
		self.sprites.append(pygame.image.load('explosion9.bmp'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.image.set_colorkey(self.image.get_at((0,0)))
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 10
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			player.attack()

	# Drawing
	screen.fill((0,0,0))
	moving_sprites.draw(screen)
	moving_sprites.update(0.25)
	pygame.display.flip()
	clock.tick(60)
