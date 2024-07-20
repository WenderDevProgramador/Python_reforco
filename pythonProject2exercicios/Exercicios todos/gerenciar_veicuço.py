class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def detalhes(self):
        return f"{super().detalhes()}, Número de portas: {self.numero_portas}"

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo_guidao):
        super().__init__(marca, modelo)
        self.tipo_guidao = tipo_guidao

    def detalhes(self):
        return f"{super().detalhes()}, Tipo de guidão: {self.tipo_guidao}"

# Criando instâncias das classes
carro1 = Carro("Toyota", "Corolla", 4)
moto1 = Moto("Yamaha", "MT-07", "Esportivo")

# Demonstrando polimorfismo
veiculos = [carro1, moto1]

for veiculo in veiculos:
    print(veiculo.detalhes())
