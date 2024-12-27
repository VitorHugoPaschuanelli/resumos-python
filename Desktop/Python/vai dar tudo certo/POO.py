#Criar classes
#Cosntrutores
#Instanciar objetos
#Herança
#Polimorfismo

#PRECISO ESTUDAR 
#-ENCAPSULAMENTO
#-CLASSES ABSTRATAS
#-INTERFACES
#-SOBRESCRITA
#-SOBRECARGA
#-EXCESSÕES

class Veiculo:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def acelerar(self):
        print("Seu veículo está acelerando")

class Carro(Veiculo):
    def __init__(self, modelo, cor, tipo):
        super().__init__(modelo, cor)
        self.tipo = tipo

    def acelerar(self):
        print(f"Seu {self.modelo} está acelerando")

class Moto(Veiculo):
    def __init__(self, modelo, cor, tipo):
        super().__init__(modelo, cor)
        self.tipo = tipo

    def acelerar(self):
        print(f"Sua {self.modelo} está acelerando")

v0 = Moto("Yamaha", "Vermelha", "Esportiva")
v1 = Carro("Chevrolet", "Azul", "Esportivo")
v2 = Veiculo("Veiculo", "Verde")

v0.acelerar()
v1.acelerar()
v2.acelerar()

