from ship import Ship

class Bullet:
    def __init__(self):
        self.ship=Ship()
        self.condition = "STOP" #Dirección de la nave
        self.ybullet=self.ship.y
    
    
        
    def shoot (self):
        if self.condition == "DISPARADO": 
            self.ybullet -= 5
        elif self.ship.direction == "STOP": #Si la nave no se mueve no hacer nada
            pass   
    