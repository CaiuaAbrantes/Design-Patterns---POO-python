"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.

When discussing which patterns to drop, we found
that we still love them all.
(Not really—I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""
from typing import Any

class AppSettings:
    _instance = None
    _initialized = False

    def __new__(cls, *args:Any, **kwargs:Any):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._initialized: #Resolve o problema do init
            return
        self._initialized = True

    

if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()
    print(as1 == as2)

