from __future__ import annotations
from abc import ABC, abstractmethod

class Sound:
    def __init__(self):
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0

    def change_mode(self, mode:PlayMode):
        self.playing =0
        self.mode = mode    
        print(f'estado atual: {self.mode}')

    def press_next(self):
        self.mode.press_next()
        print()

    def press_prev(self):
        self.mode.press_prev()
        print()

    def __str__(self):
        return str(self.playing)


class PlayMode(ABC):
    def __init__(self, sound:Sound):
        self.sound = sound

    @abstractmethod
    def press_next(self) ->None:
        pass

    @abstractmethod
    def press_prev(self) ->None:
        pass

    def __str__(self):
        return self.__class__.__name__

class RadioMode(PlayMode):
    def press_next(self) ->None:
        self.sound.playing += 1000
        print(f'radio atual e: {self.sound.playing}')

    def press_prev(self) ->None:
        if self.sound.playing >0:
            self.sound.playing -= 1000
            print(f'radio atual e: {self.sound.playing}')
        else:
            print('nao da pra fazer a acao')

class MusicMode(PlayMode):
    def press_next(self) ->None:
        self.sound.playing += 1
        print(f'musica atual e: {self.sound.playing}')

    def press_prev(self) ->None:
        if self.sound.playing >0:
            self.sound.playing -= 1
            print(f'musica atual e: {self.sound.playing}')
        else:
            print('nao da pra fazer a acao')



if __name__ == '__main__':
    som = Sound()
    som.press_next()
    som.press_prev()
    som.change_mode(MusicMode(som))
    som.press_next()
    som.press_prev()
    som.press_prev()
    
    