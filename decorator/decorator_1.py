"""
Decorator é um padrão de projeto estrutural que permite que você
adicione novos comportamentos em objetos ao colocá-los dentro de
um "wrapper" (decorador) de objetos.
Decoradores fornecem uma alternativa flexível ao uso de subclasses
para a extensão de funcionalidades.

Decorator (padrão de projeto) != Decorator em Python

Python decorator -> Um decorator é um callable que aceita outra
função como argumento (a função decorada). O decorator pode
realizar algum processamento com a função decorada e devolvê-la
ou substituí-la por outra função ou objeto invocável.
Do livro "Python Fluente", por Luciano Ramalho (pág. 223)
"""
from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

# INGREDIENTS
@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    price: float = 0.99

# Hotdogs

class Hotdog:
    _name:str
    _ingridients: list[Ingredient]

    @property
    def price(self) -> float: 
        return round(sum(
            [ingridient.price for ingridient in self._ingridients]
        ), 2)

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def ingridients(self) -> list[Ingredient]:
        return self._ingridients
    
    def __repr__(self) -> str:
        return f'{self.name}, {self.price}, {self.ingridients}'
    

class SimpleHotDog(Hotdog):
    def __init__(self):
        self._name = 'SimpleHotDog'
        self._ingridients: list[Ingredient] = [
            Bread(), Sausage(), PotatoSticks()
        ]

class SpecialHotDog(Hotdog):
    def __init__(self):
        self._name = 'SpecialHotDog'
        self._ingridients: list[Ingredient] = [
            Bread(), Sausage(), PotatoSticks(), Cheese(), Egg(), MashedPotatoes(), PotatoSticks()
        ]

#Decorators
class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog):
        self.hotdog = hotdog

    @property
    def price(self) -> float: 
        return self.hotdog.price
    @property
    def name(self) -> str:
        return self.hotdog.name
    
    @property
    def ingridients(self) -> list[Ingredient]:
        return self.hotdog.ingridients
    
class BaconDecorator(HotdogDecorator):
    def __init__(self, hotdog: Hotdog):
        super().__init__(hotdog)
        self._ingridient = Bacon()
        self._ingridients = deepcopy(self.hotdog._ingridients)
        self._ingridients.append(self._ingridient)

    @property
    def price(self) -> float: 
        return round(sum(
            [ingridient.price for ingridient in self._ingridients]
        ), 2)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingridient.__class__.__name__}'
    
    @property
    def ingridients(self) -> list[Ingredient]:
        return self.hotdog.ingridients


if __name__ == '__main__':
    simple = SimpleHotDog()
    decorated_simple_hotdog = HotdogDecorator(simple)

    print(simple)
    print(decorated_simple_hotdog)
    bacon_simple_decorated = BaconDecorator(simple)
    print(bacon_simple_decorated)
    bacon_simple_decorated = BaconDecorator(bacon_simple_decorated)
    print(bacon_simple_decorated)