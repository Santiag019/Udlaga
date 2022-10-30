from sky import Sky
from bullet import Bullet
from ship import Ship
import random
import pygame

class Game:
    
    def __init__(self):
        self.ship=Ship() 
        self.bullet=Bullet()
        self.width=800 
        self.height=800 
        self.mySky=Sky(self.width, self.height, 1600) 
        self.screen=pygame.display.set_mode((self.width,self.height)) 
        self.clock=pygame.time.Clock() 
        self.fps=60 
        self.sprites= pygame.image.load(r"C:\Users\MITROLON\Desktop\Udlaga/sprites.png") 
        self.shipsprite=pygame.Surface((64,64)).convert() 
        self.shipsprite.blit(self.sprites,(0,0),(250,436,64,64)) 
        self.bulletsprite = pygame.image.load(r"C:\Users\MITROLON\Desktop\Udlaga/bullet.png").convert() 
        self.bulletsprite.set_colorkey(0,0) 
        
    def checkKeys(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.ship.direction="RIGHT" 
        elif keys[pygame.K_LEFT]: self.ship.direction="LEFT"
        elif keys[pygame.K_w]: self.bullet.condition="DISPARADO"
        else: self.ship.direction="STOP"
        

    def run (self):
        pygame.init()
        
        control=True
        while control:
            self.screen.fill((0,0,0))
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()

            for star in self.mySky.stars:
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                pygame.draw.circle(self.screen, (r,g,b), star, 1)
            
            
            if self.ship.x > self.width-64: self.ship.x=self.width-64 
            if self.ship.x < 8: self.ship.x=8 
            
            if self.bullet.ybullet > self.height:
                self.bullet.ybullet =self.ship.y
            
            
            self.mySky.move() 
            self.ship.move() 
            self.bullet.shoot()
            x=self.ship.x 
            y=self.ship.y 
            self.screen.blit(self.shipsprite, (x,y)) 
            self.screen.blit(self.bulletsprite,(x,self.bullet.ybullet))
            self.clock.tick(self.fps) 
            self.checkKeys() 
            pygame.display.flip() 


myGame=Game() 
myGame.run() 