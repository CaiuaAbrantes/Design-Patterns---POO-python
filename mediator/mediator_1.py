"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que
encapsula a forma como um conjunto de objetos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objetos se refiram uns aos
outros explicitamente e permite variar suas
interações independentemente.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Colleague(ABC):
    def __init__(self):
        self.name:str 
    @abstractmethod
    def broadcast(self, msg:str) -> None: pass

    @abstractmethod
    def direct(self, person:Colleague, msg:str) -> None: pass

class Person(Colleague):
    def __init__(self, name:str, mediator:Mediator):
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg:str):
        self.mediator.broadcast(self, msg)

    def direct(self, person:Colleague, msg:str):
        self.mediator.direct(self, person, msg)

class Mediator(ABC):
    @abstractmethod
    def broadcast(self, person:Colleague, msg:str) -> None:
        pass

    @abstractmethod
    def direct(self, sender:Colleague, receiver:Colleague, msg:str) -> None:
        pass

class ChatRoom(Mediator):
    def __init__(self):
        self.coleagues:list[Colleague] = []

    def is_coleague(self, coleague:Colleague) -> bool:
        return coleague in self.coleagues

    def add_coleagues(self, coleague:Colleague) -> None:
        if not self.is_coleague(coleague):
            self.coleagues.append(coleague)
            return None
        print('Ja esta na lista')

    def remove_coleague(self, coleague:Colleague) -> None:
        if not self.is_coleague(coleague):
            self.coleagues.remove(coleague)
            return None
        print('Nao esta na lista')
        
    def broadcast(self, person:Colleague, msg:str):
        if not self.is_coleague(person):
            print('nao esta no grupo')
        
        print(f'{person.name} enviu: {msg}')

    def direct(self, sender:Colleague, receiver:Colleague, msg:str):
        if not self.is_coleague(sender):
            print('pessoa que esta enviando invalida')

        if not self.is_coleague(receiver):
            print('pessoa que esta recebendo invalida')

        print(f'{sender.name} enviou {msg} para {receiver.name}')

if __name__ == '__main__':
    mediator= ChatRoom()
    pedro = Person('Pedro', mediator)
    maria = Person('Maria', mediator)
    mediator.add_coleagues(pedro)
    mediator.add_coleagues(maria)
    maria.direct(pedro, 'oi')
    pedro.broadcast('ola')

