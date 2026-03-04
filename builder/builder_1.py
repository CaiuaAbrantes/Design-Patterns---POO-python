"""
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos
(method chaining).
"""
from abc import ABC, abstractmethod



class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()

class User(StringReprMixin):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.adresses = []

class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self)->User: pass

    @abstractmethod
    def add_firstname(self, firstname: str): pass

    @abstractmethod
    def add_lastname(self, lastname: str): pass

    @abstractmethod
    def add_age(self, firstname: int): pass

    @abstractmethod
    def add_phone(self, phone: str): pass

    @abstractmethod
    def add_adress(self, adress: str): pass


class UserBuilder(IUserBuilder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self) -> User:
        return_data = self._result
        self.reset()
        return return_data


    def add_firstname(self, firstname: str):
        self._result.firstname = firstname

    def add_lastname(self, lastname: str): 
        self._result.lastname = lastname

    def add_age(self, age: int): 
        self._result.age = age

    def add_phone(self, phone: str): 
        self._result.phone_numbers.append(phone)

    def add_adress(self, adress: str): 
        self._result.adresses.append(adress)

class UserDirector:
    def __init__(self, builder:UserBuilder):
        self._builder: UserBuilder = builder


    def with_age(self, firstname:str, lastname:str, age:int):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(age)
        return self._builder.result
    
    def with_adress(self, firstname:str, lastname:str, adress:str):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_adress(adress)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Pedro', 'Raul', 15)
    print(user1)
    user2 = user_director.with_adress('Pedro', 'Raul', 'Rua 15')
    print(user2)
    


