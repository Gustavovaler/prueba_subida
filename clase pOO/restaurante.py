import random
class Restaurante:    

    def __init__(self,nombre):
        self.reputacion = 0
        self.nombre = nombre
        # tiempos de preparacion
        self.comida = 25
        self.bebida =  3
        self.postre = 10 
        # cocineros de turno 
        self.cocineros = ['Josefa', 'Martin', 'Leo']     

    def __str__(self):
        return f'Restaurante {self.nombre}'

    def recibir_pedido(self, pedido):
        self.pedido = pedido
        for item in pedido:
            print(f"Item  {item['nombre']} - Precio $ {item['precio']}")
        self.cuenta = pedido[0]['precio']+pedido[1]['precio']+pedido[2]['precio']       
        return self.cuenta

    def recibir_pago(self, dinero):
        if dinero >= self.cuenta:
            self.preparar_pedido()
            print(f'Dinero del cliente $ {dinero}')
            print(f'Importe del pedido $ {self.cuenta}')
            return dinero - self.cuenta
        else:
            return 'Dinero Insuficiente'

    def preparar_pedido(self):

        self.tiempo_espera = 0

        self.cocinero = Cocinero(self.cocineros[0])

        for item in self.pedido:

            if item['tipo'] == "comida":
                self.tiempo_espera += self.comida

            elif item['tipo'] == "bebida":
                self.tiempo_espera += self.bebida

            else:
                self.tiempo_espera += self.postre
                
        velocidad = self.cocinero.velocidad()
        return self.tiempo_espera*velocidad

    def recibe_calificacion(self, puntaje):
        self.reputacion += puntaje
        print()
        print(f'La calificacion del restaurante es de {self.reputacion} puntos')


class Cocinero:

    def __init__(self, nombre):
        self.nombre = nombre     


    def velocidad(self):

        if self.nombre == 'Josefa':
            self.agilidad = 1

        elif self.nombre == 'Martin':
            self.agilidad = 1.5

        elif self.nombre == "Leo":
            self.agilidad = 0.9

        return self.agilidad
