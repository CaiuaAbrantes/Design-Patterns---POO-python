"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""
from typing import List
from copy import deepcopy

class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()

class Adress(StringReprMixin):
    def __init__(self, street:str, number:int):
        self.street = street
        self.number = number

class Person(StringReprMixin):
    def __init__(self, firstname:str, lastname:str):
        self.firstname = firstname
        self.lastname = lastname    
        self.adresses:List[Adress] = []

    def add_adress(self, adress:Adress) -> None:
        self.adresses.append(adress)

    def clone(self):
        return deepcopy(self)



if __name__ == '__main__':



    luiz = Person('Luiz', 'Miranda')
    adress = Adress('Av.Brasil', 105)
    luiz.add_adress(adress)
    print(luiz)

    esposa_luiz = luiz.clone()
    esposa_luiz.firstname ='Leticia'
    print(esposa_luiz)



    