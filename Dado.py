import random 

class Dado:

    caras=0
    
    def __init__(self, numCaras):
        self.caras=numCaras
    
    def lanzar(self):
        return random.randint(1, self.caras)
