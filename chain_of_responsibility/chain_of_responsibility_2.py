from __future__ import annotations
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self.sucessor : Handler
    @abstractmethod
    def handle(self, letra:str)->str:
        pass

class HandlerABC(Handler):
    def __init__(self, sucessor:Handler):
        self.sucessor = sucessor

    def handle(self, letra:str):
        lista = ['A', 'B', 'C']
        if letra in lista:
            return f'HandlerABC cuidou da letra'
        return self.sucessor.handle(letra)
    
class HandlerDEF(Handler):
    def __init__(self, sucessor:Handler):
        self.sucessor = sucessor

    def handle(self, letra:str):
        lista = ['D', 'E', 'F']
        if letra in lista:
            return f'HandlerDEF cuidou da letra'
        return self.sucessor.handle(letra)
    
class HandlerNone(Handler):
    def handle(self, letra:str):
        return f'Nao foi possivel cuidar da letra: {letra}'
    
if __name__ == '__main__':
    erro = HandlerNone()
    handlerdef = HandlerDEF(erro)
    handlerabc = HandlerABC(handlerdef)
    
    print(handlerabc.handle('A'))
    print(handlerabc.handle('B'))
    print(handlerabc.handle('D'))
    print(handlerabc.handle('E'))
    print(handlerabc.handle('J'))
