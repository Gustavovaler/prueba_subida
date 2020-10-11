from random import randint
import time

class Player:

    def __init__(self, nombre, weapon):
        self.nombre = nombre
        self.weapon = weapon        

    def calc_attrs(self):
        self.vida = self.vida*(self.defense/self.lvl)

    def beat(self, player):
        golpe = player.rcv_damage(self.attack)
        return golpe

    def rcv_damage(self, damage):
        ran = randint(0,10)
        if ran == 5:
            damage = damage*((self.lvl*randint(5,10))*(self.lvl/10))*(self.defense/(self.lvl*self.weapon))+self.attack+self.weapon
            print(f"Golpe crítico")
        else:
            damage = damage*((self.lvl*randint(1,5))*(self.lvl/10))*(self.defense/(self.lvl*self.weapon))
        self.vida -= damage
        return damage

    def run(self):
        pass

class Orco(Player):
    def __init__(self, nombre, weapon):
        super().__init__(nombre, weapon)
        self.lvl = 5
        self.attack = 15
        self.defense = 20
        self.velocidad = 150
        self.att_sp = 10
        self.vida = 120
        self.calc_attrs()

class Humano(Player):
    def __init__(self, nombre, weapon):
        super().__init__(nombre, weapon)
        self.lvl = 5
        self.attack = 17
        self.defense = 20
        self.velocidad = 150
        self.att_sp = 12
        self.vida = 120
        self.calc_attrs()


def combat(player1, player2):
    while True:
        if player1.vida >=1:
            time.sleep(0.5)
            golpe = player1.beat(player2)
            print(f"Pega {player1.nombre} con {int(golpe)} de poder. A {player2.nombre} le queda { round(player2.vida,0)} de vida")
        else:
            break
        if player2.vida >=1:
            time.sleep(0.5)
            golpe = player2.beat(player1)
            print(f"Pega {player2.nombre} con {int(golpe)} de poder. A {player1.nombre} le queda { round(player1.vida, 0)} de vida")
        else:
            break

p1 = Orco("gus",14)
p2 = Humano ("Oter", 14)

combat(p1,p2)




