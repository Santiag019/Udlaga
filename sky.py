import random

class Sky:
    def __init__(self,width,height,quantity):
        self.stars=[]
        self.width=width
        self.height=height
        
        for i in range(quantity):
            x=random.randint(0,height)
            y=random.randint(0,height)
            self.stars.append([x,y])
    
    def move(self):
        for star in self.stars:
            star[1]+=1
            if star[1] > self.height:
                star[1]=0
        