from ship import Ship

class Bullet:
    def __init__(self):
        self.ship=Ship()
        self.condition = "STOP" 
        self.ybullet=self.ship.y
    
    
        
    def shoot (self):
        if self.condition == "DISPARADO": 
            self.ybullet -= 5
        elif self.ship.direction == "STOP": 
            pass   
    