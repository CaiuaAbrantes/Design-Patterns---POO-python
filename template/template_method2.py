from abc import ABC, abstractmethod

class Pizza(ABC):
    def prepare(self):
        #Template Method
        self.adicionar_ingredientes()
        self.cozinhar()
        self.cortar()
        self.massa_diferente()#Hook 
        print('pizza finalizada')

    @abstractmethod
    def adicionar_ingredientes(self): pass

    @abstractmethod
    def cozinhar(self): pass

    def cortar(self): 
        print(f'cortando pizza {self.__class__.__name__}')

    def massa_diferente(self):
        pass


class Mussarela(Pizza):
    def __init__(self):
        self.ingredientes = ['tomate', 'queijo', 'massa']
        self.tempo = '50 minutos'
    
    def adicionar_ingredientes(self):
        for ingrediente in self.ingredientes:
            print(f'adicionado o ingrediente {ingrediente}')

    def cozinhar(self):
        print(f'cozinhou por {self.tempo}')


class MussarelaComBorda(Pizza):
    def __init__(self):
        self.ingredientes = ['tomate', 'queijo', 'massa', 'chocolate']
        self.tempo = '45 minutos'
    
    def adicionar_ingredientes(self):
        for ingrediente in self.ingredientes:
            print(f'adicionado o ingrediente {ingrediente}')

    def cozinhar(self):
        print(f'cozinhou por {self.tempo}')

    def massa_diferente(self):
        print('colocou borda de chocolate')
        

if __name__ == '__main__':
    mussarela = Mussarela()
    mussarela.prepare()

    print()
    print('outra pizza')
    print()

    mussarelacomborda = MussarelaComBorda()
    mussarelacomborda.prepare()
    