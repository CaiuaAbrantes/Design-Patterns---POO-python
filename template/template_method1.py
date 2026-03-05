"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""

from abc import ABC, abstractmethod

class Abstract(ABC):
    def templateMethod(self):
        self.hook()
        self.operation1()
        self.operation2()

    def hook(self): pass

    @abstractmethod
    def operation1(self):pass

    @abstractmethod
    def operation2(self):pass

class ConcreteClass1(Abstract):
    def operation2(self):
        print('operation 2')

    def operation1(self):
        print('operation 1')

class ConcreteClass2(Abstract):
    def operation2(self):
        print('operation 2 diferente')

    def operation1(self):
        print('operation 1 diferente')

    def hook(self):
        print('vou usar o hook')


if __name__ == '__main__':

    c1 = ConcreteClass1()
    c1.templateMethod()

    print()
    
    c2 = ConcreteClass2()
    c2.templateMethod()