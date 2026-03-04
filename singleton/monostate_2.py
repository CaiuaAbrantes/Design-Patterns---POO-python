class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()   
    

class MonoState(StringReprMixin):
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome = None, sobrenome = None):
        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome

class A(MonoState):
    pass

m1 = MonoState('Pedro')
m2 = A(sobrenome='Raul')



print(m1)   
