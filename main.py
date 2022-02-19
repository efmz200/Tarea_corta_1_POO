from Tablero import *
class Main:

    def __init__(self, cantidad_casillas ) :
        self.tablero=Tablero(cantidad_casillas)
        
    def jugar(self):
        #loop de agregado de jugadores
        while True:
            opcion=1
            opcion=input("ingrese 1 para agregar otro jugador o presione enter para continuar ")
            if opcion=="1":
                self.tablero.agregar_jugador()
            else:
                break
        self.tablero.mostrar_orden()
        #loop del juego
        while True:
            turno=self.tablero.jugador_actual
            if(turno>len(self.tablero.jugadores)-1):
                self.tablero.mostrar_orden()  
                self.tablero.jugador_actual=0
                continue
            else:
                print("Es turno de la ficha color: "+self.tablero.jugadores[turno].color)
                
                opcion=input("ingrese 1 para lanzar el dado o presione enter para continuar: ")
                if opcion=="1":
                    self.tablero.jugadores[turno].avanzar()
                self.tablero.jugador_actual+=1



juego=Main(30)
juego.jugar()