class Ship:
    def __init__(self):
        self.direction = "STOP" #Dirección de la nave
        self.x=368 #Posición x de la nave
        self.y=710 #Posición y de la nave
    
    def move(self):
        if self.direction == "LEFT": #Disminuir en 5 si la nave se mueve a la izquierda
            self.x -= 5
        elif self.direction == "RIGHT": #Aumentar en 5 si la nave se mueve a la derecha
            self.x += 5
        elif self.direction == "STOP": #Si la nave no se mueve no hacer nada
            pass    
            