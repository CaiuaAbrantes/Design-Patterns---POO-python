"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: 
        pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de Luxo buscou o cliente')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro Popular buscou o cliente')

class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto buscou o cliente')


class VeiculoFactory(ABC):
    def __init__(self, tipo:str):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo:str) -> Veiculo:
        pass
    
    def buscar_cliente(self):
        self.carro.buscar_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo:str) -> Veiculo:
        carro = {
            'popular' : CarroPopular(),
            'luxo' : CarroLuxo(),
            'moto' : Moto()
        }
        if tipo not in carro:
            assert 0, 'Veiculo nao existe na zona Norte'
        return carro[tipo]


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo:str) -> Veiculo:
        carro = {
            'popular' : CarroPopular(),
        }
        if tipo not in carro:
            assert 0, 'Veiculo nao existe na zona Sul'
        return carro[tipo]



if __name__ == '__main__':
    #TESTE
    from random import choice
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto']
    veiculos_disponiveis_zona_sul = ['popular']

    for i in range(10):
        print('zona norte')
        veiculo1 = ZonaNorteVeiculoFactory.get_carro(choice(veiculos_disponiveis_zona_norte))
        veiculo1.buscar_cliente()


        print()


        print('zona sul')
        veiculo2 = ZonaNorteVeiculoFactory.get_carro(choice(veiculos_disponiveis_zona_sul))
        veiculo2.buscar_cliente()
        print()

