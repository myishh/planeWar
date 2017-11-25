# -*- coding:utf-8 -*-
# version 07, show enemy

import pygame
import time
from pygame.locals import *

class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 200
        self.y = 574
        self.screen = screen_temp
        self.image = pygame.image.load("./images/me1.png")
        self.bullet_list = []
    
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
        
    def move_left(self):
        self.x -= 10
        
    def move_right(self):
        self.x += 10
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

# [1] Enemy class
class EnemyPlane(object):
    def __init__(self, screen_temp):
        self.x = 300
        self.y = 10
        self.screen = screen_temp
        self.image = pygame.image.load("./images/enemy1.png")
        #self.bullet_list = []
    
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
'''        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()'''
        

    def move_left(self):
        self.x -= 10
        
    def move_right(self):
        self.x += 10
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 50 
        self.y = y - 10
        self.screen = screen_temp
        self.image = pygame.image.load("./images/bullet1.png")
        
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


    def move(self):
        self.y -= 15



def key_control(hero_temp):

    for event in pygame.event.get():
        if event.type == QUIT:                 
            print("I have to exit")
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
                hero_temp.fire()#[2] add fire() method



def main():
    screen = pygame.display.set_mode((480, 700), 0, 32)

    background = pygame.image.load("./images/background.png")
    
    hero = HeroPlane(screen)

    #[2]create a enemy object
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        hero.display()
        #[3]display the enemy plane
        enemy.display()
        key_control(hero)
        pygame.display.update()


        time.sleep(0.025)



if __name__ == "__main__":
    main()

