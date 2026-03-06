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
    def __init__(self, hotdog: Hotdog, ingridient:Ingredient):
        self.hotdog = hotdog
        self._ingridient = ingridient
        self._ingridients = deepcopy(self.hotdog._ingridients)
        self._ingridients.append(self._ingridient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingridient.__class__.__name__}'
    

if __name__ =='__main__':
    simple_hotdog = SimpleHotDog()

    print(simple_hotdog)

    bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())
    egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog, Egg())

    mashed_potato_egg_bacon_simple_hotdog = HotdogDecorator(
        egg_bacon_simple_hotdog,
        MashedPotatoes()
    )

    print(mashed_potato_egg_bacon_simple_hotdog)