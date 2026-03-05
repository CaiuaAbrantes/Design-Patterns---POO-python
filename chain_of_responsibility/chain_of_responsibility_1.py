"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""

#Implementando com funcoes
from __future__ import annotations
def HandlerABC(letter:str)->str:
    letters =['A', 'B', 'C']
    if letter in letters:
        return f'hendlerABC tratou a {letter}'
    return handler_DEF(letter)

def handler_DEF(letter:str)->str:
    letters =['D', 'E', 'F']
    if letter in letters:
        return f'hendlerDEF tratou a {letter}'
    return handler_unsolved(letter)
    
def handler_unsolved(letter:str) -> str:
    return f'handler unsolved problem: nao sei tratar a letra {letter}'


if __name__ == '__main__':
    print(HandlerABC('A'))
    print(HandlerABC('B'))
    print(HandlerABC('C'))
    print(HandlerABC('D'))
    print(HandlerABC('F'))
    print(HandlerABC('S'))