# -*- coding:utf-8 -*-
# version 06 let plane fire bullets(ignore the version 5)
    
import pygame
from pygame.locals import *
import time

class HeroPlane(object):
	def __init__(self, screen_temp): 
		self.x = 200
		self.y = 574
		self.screen = screen_temp
		self.image = pygame.image.load("./images/me1.png")	
	
	def display(self):
		self.screen.blit(self.image, (self.x, self.y))

	def move_left(self):
		self.x -= 5

	def move_right(self):
		self.x += 5
    
    
    def fire():
        pass

'''
class Bullet(object):
    def __init__(self, screen_temp):
		self.x = 200
		self.y = 300
		self.screen = screen_temp
		self.image = pygame.image.load("./images/bullet1.png")	
'''


def key_control(hero_temp):
	for event in pygame.event.get():

		if event.type == QUIT:
			print("exit")
			exit()
		
		elif event.type == KEYDOWN:
			if event.key == K_a or event.key == K_LEFT:
				print("left")
				hero_temp.move_left()
			elif event.key == K_d or event.key == K_RIGHT:
				print("right")
				hero_temp.move_right()
			elif event.key == K_SPACE:	
				print("space")
                hero_temp.fire()

def main():
	screen = pygame.display.set_mode((480, 700), 0, 32)
	
	background = pygame.image.load("./images/background.png")
	
	hero = HeroPlane(screen)	


	while True:
		screen.blit(background, (0,0))
		hero.display()
		key_control(hero)
		pygame.display.update()
		
	
		time.sleep(0.02)

if __name__ == "__main__":
	main()
