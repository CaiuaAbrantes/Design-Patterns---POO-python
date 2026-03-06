"""
Iterator é um padrão comportamental que tem a
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objeto
agregado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna
- Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos
- Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais
tarefas para um objeto iterador.
"""
from collections.abc import Iterable, Iterator

#from abc import ABC, abstractmethod

class MyIterator(Iterator[object]):
    def __init__(self, collection:list[object]):
        self._collection = collection
        self._index = 0
        self._len = len(collection)

    def __next__(self):
        if self._index > self._len:
            self._index = 0 
            raise StopIteration
        item = self._collection[self._index]
        self._index +=1
        return item


class MyList(Iterable[object]):
    def __init__(self):
        self._items: list[object] = []
        self._my_iterator = MyIterator(self._items)
    
    def add(self, value:object):
        self._items.append(value)


    def __iter__(self):
        return self._my_iterator
    def __str__(self):
        return f'{self.__class__.__name__}, ({self._items})'

if __name__ == '__main__':
    mylist = MyList()
    mylist.add('Luiz')
    mylist.add(2)
    print(mylist)

    print('ROUBEI UM VALOR', next(iter(mylist)))
