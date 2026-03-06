"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalhem em conjunto
através de um "adaptador".
"""

from abc import ABC, abstractmethod

class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass

class Control(IControl):
    def top(self) -> None: 
        print('moveu pra cima')

    def right(self) -> None: 
        print('moveu pra direita')
    
    def down(self) -> None: 
        print('moveu pra baixo')

    def left(self) -> None: 
        print('moveu pra esquerda')

class NewControl:
    def move_top(self) -> None: 
        print('moveu pra cima')

    def move_right(self) -> None: 
        print('moveu pra direita')
    
    def move_down(self) -> None: 
        print('moveu pra baixo')

    def move_left(self) -> None: 
        print('moveu pra esquerda')

class ControlAdapter:
    def __init__(self, new_control: NewControl):
        self.new_control = new_control

    def top(self) -> None: 
        self.new_control.move_top()

    def right(self) -> None: 
        self.new_control.move_right()
    
    def down(self) -> None: 
        self.new_control.move_down()

    def left(self) -> None: 
        self.new_control.move_left()

class ControlAdapter2(Control, NewControl):
    def top(self) -> None: 
        self.move_top()

    def right(self) -> None: 
        self.move_right()
    
    def down(self) -> None: 
        self.move_down()

    def left(self) -> None: 
        self.move_left()

if __name__ == '__main__':
    new_control = NewControl()
    c1 = ControlAdapter(new_control)
    c2 = ControlAdapter2()
    c1.down()
    c1.left()
    c2.right()
    c2.top()