"""
Flyweight é um padrão de projeto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades
de objetos de forma granular.

Só use o Flyweight quanto TODAS as condições
a seguir forem verdadeiras:

- uma aplicação utiliza uma grande quantidade de
objetos;
- os custos de armazenamento são altos por causa
da grande quantidade de objetos;
- a maioria dos estados de objetos podem se tornar
extrínsecos;
- muitos objetos podem ser substituídos por poucos
objetos compartilhados;
- a aplicação não depende da identidade dos objetos.

Importante:
- Estado intrínseco é o estado do objeto que não muda,
esse estado deve estar dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda,
esse estado pode ser movido para fora do objeto
flyweight;

Dicionário:
Intrínseco - que faz parte de ou que constitui a
essência, a natureza de algo; que é próprio de
algo; inerente.
Extrínseco - que não pertence à essência de algo;
que é exterior.
"""

from __future__ import annotations
from typing import Any

class Client:
    #context
    def __init__(self, name:str):
        self.name = name
        self._adresses: list[Adress] = []

        #Extrinsic adress data
        self.adress_number:str
        self.adress_detail:str

    def add_adress(self, adress:Adress)->None:
        self._adresses.append(adress)

    def list_adresses(self):
        for adress in self._adresses:
            adress.show_adress(self.adress_number, self.adress_detail)



class Adress:
    #FlyWeight
    def __init__(self, street:str, neighbourhood:str, zip_code:str):
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_adress(self, adress_number:str, adress_detail:str) -> None:
        print(self._street, adress_number, self._neighbourhood, adress_detail, self._zip_code)

class AdressFactory:
    _adresses: dict[Any, Adress] = {}

    def _get_key(self, **kwargs:Any):
        return ''.join(kwargs.values())
    
    def get_adresses(self, **kwargs:Any) -> Adress:
        key = self._get_key(**kwargs)
        try:
            adresses_flyweight = self._adresses[key]
            print('usando objeto ja criado ')
        except KeyError:
            adresses_flyweight = Adress(**kwargs)
            self._adresses[key] = adresses_flyweight
            print('criando novo objeto')
        return adresses_flyweight

if __name__ == '__main__':
    factory = AdressFactory()
    a1= factory.get_adresses(street='Av.Brasil', neighbourhood='Centro', zip_code='000-155-00')
    a2= factory.get_adresses(street='Av.Brasil', neighbourhood='Centro', zip_code='000-155-00')

    pedro = Client('Pedro')
    pedro.adress_number ='15'
    pedro.adress_detail ='Casa'
    pedro.add_adress(a1)
    pedro.list_adresses()

    joao = Client('Joao')
    joao.adress_number ='19'
    joao.adress_detail ='Apto.'
    joao.add_adress(a1)
    joao.list_adresses()