"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class Light:
    #Reciver: Luz
    def __init__(self, name:str, room_name:str):
        self.name = name
        self.room_name = room_name
        self.color = 'Default Color'

    def on(self) -> None:
        print(f'A luz {self.name} que esta no {self.room_name} agora esta ligada')

    def off(self) -> None:
        print(f'A luz {self.name} que esta no {self.room_name} agora esta desligada')

    def change_color(self, new_color:str) -> None:
        self.color = new_color
        print(f'A luz {self.name} que esta no {self.room_name} agora esta na cor {self.color}')

class ICommand(ABC):
    #Interface de comando
    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass

class LightOnCommand(ICommand):
    #Comando Concreto
    def __init__(self, light:Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightChangeColor(ICommand):
    #Comando Concreto
    def __init__(self, light:Light, color:str):
        self.light = light
        self.color = color

    def execute(self):
        self.light.change_color(self.color)

    def undo(self):
        self.light.change_color('Default Color')

class RemoteControler:
    #invoker
    def __init__(self):
        self._buttons: dict[str, ICommand] = {}

    def button_add_command(self, name:str, command: ICommand):
        self._buttons[name] = command


    def button_execute(self, name:str):
        if name in self._buttons:
            self._buttons[name].execute()

    def button_undo(self, name:str):
        self._buttons[name].undo()


if __name__ == '__main__':
    bedrom_light = Light('led', 'bedroom')
    home_light = Light('led', 'home')
    controler = RemoteControler()
    command1 = LightOnCommand(bedrom_light)
    controler.button_add_command('1', command1)
    command2 = LightOnCommand(home_light)
    controler.button_add_command('2', command2)
    command3 = LightChangeColor(home_light, 'red')
    controler.button_add_command('3', command3)
    controler.button_execute('1')
    controler.button_execute('2')
    controler.button_undo('1')
    controler.button_execute('3')
