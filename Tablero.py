from traceback import print_tb
from Ficha import *

class Tablero:
    
    #Defina aquí los atributos de Tablero
    jugadores=[]    
    


   

    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self,cantidad_casiilas):
        self.cantidad_casillas=cantidad_casiilas
        self.jugador_actual=0
    
    def agregar_jugador(self):
        color=input("Ingrese el color de la nueva ficha: ")
        self.jugadores+=[Ficha(color)]
    
    def mostrar_orden(self):
        print("\nLa meta esta en la posición: "+str(self.cantidad_casillas))
        for player in self.jugadores:
            print("El jugador: "+player.color+" está en la casilla: "+str(player.posicion+"\n"))
        print("")
        
        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase


    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self
