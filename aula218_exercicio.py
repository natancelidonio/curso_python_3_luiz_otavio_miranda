"""Exercício com classes
1- Crie uma classe Carro (Nome)
2- Crie uma classe Motor (Nome)
3- Crie uma classe Fabricante (Nome)
4- Faça a ligação entre Carro tem um Motor
Obs.: Um motor pode ser de vários carros
5- Faça a ligação entre Carro e Fabricante
Obs.: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricante na tela
"""

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None    
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, modelo):
        self._motor = modelo
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    def listar_caracteristicas(self):
        print(self.nome, f'- Motor: {self.motor} /', self._fabricante)
        print()
        
class Motor:
    def __init__(self, modelo):
        self.modelo = modelo
    
    def exibe_modelo(self):
        return self.modelo

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

    def exibe_fabricante(self):
        return self.nome

motor_1_0 = Motor('1.0').exibe_modelo()
motor_v8 = Motor('V8').exibe_modelo()
fiat = Fabricante('Fiat').exibe_fabricante()
volks = Fabricante('Volkswagem').exibe_fabricante()

print()

car1 = Carro('Fusca')
car1.motor = motor_v8
car1.fabricante = volks
car1.listar_caracteristicas()

car2 = Carro('Palio')
car2.motor = motor_1_0
car2.fabricante = fiat
car2.listar_caracteristicas()