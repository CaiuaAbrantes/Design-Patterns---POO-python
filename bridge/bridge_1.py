"""
Bridge é um padrão de projeto estrutural que
tem a intenção de desacoplar uma abstração
da sua implementação, de modo que as duas
possam variar e evoluir independentemente.

Abstração é uma camada de alto nível para algo.
Geralmente, a abstração não faz nenhum trabalho
por conta própria, ela delega parte ou todo o
trabalho para a camada de implementação.

RELEMBRANDO: Adapter é um padrão de projeto
estrutural que tem a intenção de permitir
que duas classes que seriam incompatíveis
trabalhem em conjunto através de um "adaptador".

Diferença (GOF pag. 208) - A diferença chave
entre esses padrões está nas suas intenções...
...O padrão Adapter faz as coisas funcionarem
APÓS elas terem sido projetadas; o Bridge as
faz funcionar ANTES QUE existam...
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self):pass

    @abstractmethod
    def decrease_volume(self):pass

    @abstractmethod
    def power(self):pass

class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice):
        self._device = device

    def increase_volume(self):
        self._device.volume += 10

    def decrease_volume(self):
        self._device.volume -= 10

    def power(self):
        self._device.power = not self._device.power

class RemoteControlWithMute(IRemoteControl):
    def __init__(self, device: IDevice):
        self._device = device

    def increase_volume(self):
        self._device.volume += 10

    def decrease_volume(self):
        self._device.volume -= 10

    def power(self):
        self._device.power = not self._device.power

    def mute(self):
        self._device.volume = 0

class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int:
        pass
    
    @volume.setter
    @abstractmethod
    def volume(self, value:int):
        pass

    @property
    @abstractmethod
    def power(self) ->bool:pass

    @power.setter
    @abstractmethod
    def power(self, value:bool):
        pass

class TV(IDevice):
    def __init__(self):
        self._volume = 0
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume
    
    @volume.setter
    def volume(self, value:int):
        if not self.power:
            print(f'{self._name} esta desligada')
            return
        
        backup = self._volume
        self._volume = value
        if self._volume <0 or self._volume > 100:
            self._volume = backup
        print(f'volume : {self._volume}')

    @property
    def power(self) ->bool:
        return self._power

    @power.setter
    def power(self, value:bool):
        self._power = value
        power_status = 'ON' if self.power else 'OFF' 
        print(f'A {self._name} agora esta {power_status}')

class Radio(IDevice):
    def __init__(self):
        self._volume = 0
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume
    
    @volume.setter
    def volume(self, value:int):
        if not self.power:
            print(f'{self._name} esta desligada')
            return
        
        backup = self._volume
        self._volume = value
        if self._volume <0 or self._volume > 30:
            self._volume = backup
        print(f'volume : {self._volume}')

    @property
    def power(self) ->bool:
        return self._power

    @power.setter
    def power(self, value:bool):
        self._power = value
        power_status = 'ON' if self.power else 'OFF' 
        print(f'A {self._name} agora esta {power_status}')


if __name__ == '__main__':
    tv = TV()
    radio = Radio()
    remote = RemoteControl(tv)
    remote1 = RemoteControlWithMute(radio)
    remote1.power()
    remote1.increase_volume()
    remote1.mute()
    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.power()
    remote2 = RemoteControl(radio)
    remote2.power()
    remote2.increase_volume()
    remote2.increase_volume()
    remote2.increase_volume()
    remote2.increase_volume()