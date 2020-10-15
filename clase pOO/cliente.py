from menu import menu
from restaurante import Restaurante
import random

class Cliente:
    
    def __init__(self, nombre, direccion, dinero):
        self.nombre = nombre
        self.direccion = direccion
        self.dinero = dinero
        
    def __str__(self):
        return f'Cliente {self.nombre} vive en {self.direccion}'

    def hacer_pedido(self):
        self.pedido = [menu["comidas"][random.randint(0,2)], menu['bebidas'][random.randint(0,2)], menu['postres'][random.randint(0,2)]]
        self.restaurante = Restaurante('Danubio')
        self.pedir = self.restaurante.recibir_pedido(self.pedido)
        
    def pagar(self):
        self.dinero_restante = self.restaurante.recibir_pago(self.dinero)
        if isinstance(self.dinero_restante, int):
            print(f'Dinero luego de la compra {self.dinero_restante}')
            self.esperar()
        else:
            print(self.dinero_restante)


    def esperar(self):
        self.pedido_recibido = self.restaurante.preparar_pedido()
        print(f"Mi pedido llega en {self.pedido_recibido} minutos")
        if self.pedido_recibido <= 35:
            self.restaurante.recibe_calificacion(10)
        elif self.pedido_recibido >= 35 and self.pedido_recibido <= 45:
            self.restaurante.recibe_calificacion(5)
        else:
            self.restaurante.recibe_calificacion(1)

        



cliente = Cliente('Juan', 'Evergreen 742', 1250)

cliente.hacer_pedido()

cliente.pagar()





cliente = Cliente('Mariel', 'MujerSiempreviva 742', 2500)

cliente.hacer_pedido()

cliente.pagar()

#nueva rama
