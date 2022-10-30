class Ship:
    def __init__(self):
        self.direction = "STOP" 
        self.x=368 
        self.y=710 
    
    def move(self):
        if self.direction == "LEFT": 
            self.x -= 5
        elif self.direction == "RIGHT": 
            self.x += 5
        elif self.direction == "STOP": 
            pass    
            