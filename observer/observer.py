"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.
"""
from __future__ import annotations
from abc import abstractmethod, ABC
from typing import List


class IObservable(ABC):

    
    @property
    @abstractmethod
    def state(self)-> dict[object, object]:pass
    
    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observer(self) -> None: pass


class WeatherStation(IObservable):
    #Observable
    def __init__(self):
        self._observers: List[IObserver] = []
        self._state: dict[object, object] = {}

    @property
    def state(self):
        return self._state
    
    
    @state.setter
    def state(self, state_update:dict[object, object]):
        new_state:dict[object, object] = {**self._state, **state_update}
        if new_state != self._state:
            self._state = new_state
            self.notify_observer()
        
    def reset_state(self):
        self._state = {}
        self.notify_observer()
        

    def add_observer(self, observer: IObserver) -> None: 
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observer(self) -> None:
        for observer in self._observers:
            observer.update()

class IObserver(ABC):
    @abstractmethod
    def update(self)-> None: pass

class Smartphone(IObserver):
    def __init__(self, name:str, observable: IObservable):
        self.name = name
        self.observable = observable
    def update(self):
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} '
              f'acabou de ser atualizado => {self.observable.state}')


if __name__ =='__main__':
    wearher_station = WeatherStation()

    phone1 = Smartphone('IPhone_10', wearher_station)
    phone2 = Smartphone('Iphone_SE', wearher_station)

    wearher_station.add_observer(phone1)
    wearher_station.add_observer(phone2)

    wearher_station.state = {'tempo': 30}
    wearher_station.state = {'tempo': 32, 'humidade': '90%'}

    wearher_station.remove_observer(phone2)
    print()
    wearher_station.reset_state()



