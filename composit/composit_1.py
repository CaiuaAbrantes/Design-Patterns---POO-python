"""
Composite é um padrão de projeto estrutural que permite que
você utilize a composição para criar objetos em estruturas
de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de
objetos (Composite).

IMPORTANTE: só aplique este padrão em uma estrutura que possa
ser representada em formato hierárquico (árvore).

No padrão composite, temos dois tipos de objetos:
Composite (que representa nós internos da árvore) e Leaf
(que representa nós externos da árvore).

Objetos Composite são objetos mais complexos e com filhos.
Geralmente, eles delegam trabalho para os filhos usando
um método em comum.
Objetos Leaf são objetos simples, da ponta e sem filhos.
Geralmente, são esses objetos que realizam o trabalho
real da aplicação.
"""

from __future__ import annotations
from abc import ABC, abstractmethod

#Component
class BoxStructure(ABC):
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_total_price(self) -> float : pass

    def add(self, child:BoxStructure) -> None: pass
    def remove(self, child:BoxStructure) -> None: pass

class Box(BoxStructure):
    def __init__(self, name:str):
        self.name = name
        self._children: list[BoxStructure] =[]

    def print_content(self) -> None: 
        print(f'{self.name} tem os produtos: ')
        for child in self._children:
            child.print_content()
        print('---------------')
    def get_total_price(self) -> float :
        print(f'{self.name} custa no total: ')
        return sum(
            [child.get_total_price() for child in self._children]
        )

    def add(self, child:BoxStructure) -> None: 
        self._children.append(child)
    def remove(self, child:BoxStructure) -> None: 
        if child in self._children:
            self._children.remove(child)
            return
        print('Child is not there')

#leaf
class Product(BoxStructure):
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_total_price(self):
        return self.price
    
if __name__ == '__main__':
    #leaf
    camiseta1 = Product('camiseta1', 49.90)
    camiseta2 = Product('camiseta2', 39.90)
    camiseta3 = Product('camiseta3', 69.90)
    camiseta4 = Product('camiseta4', 29.40)

    #Composit
    box1 = Box('Caixa de camisetas')

    box1.add(camiseta1)
    box1.add(camiseta2)
    box1.add(camiseta3)
    box1.add(camiseta4)

    print(box1.get_total_price())
    box1.print_content()

    bermuda1 = Product('bermuda1', 19.90)
    bermuda2= Product('bermuda1', 39.90)
    box2 = Box('Caixa de bermudas')
    box2.add(bermuda1)
    box2.add(bermuda2)
    print(box2.get_total_price())
    box2.print_content()

    box3 = Box('Caixa com tudo')
    box3.add(box1)
    box3.add(box2)
    print(box3.get_total_price())
    box3.print_content()
        