"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from __future__ import annotations
from time import sleep
from abc import abstractmethod, ABC
from typing import Any

#subject interface
class IUser(ABC):

    first_name:str
    last_name:str

    @abstractmethod
    def get_adresses(self) -> list[dict[object,object]]:
        pass

    @abstractmethod
    def get_all_user_data(self) -> dict[Any,Any]:
        pass

#real subject
class RealUser(IUser):
    def __init__(self, firstname:str, lastname:str):
        sleep(2) #Simulando requisicao
        self.first_name = firstname
        self.last_name = lastname
    
    def get_adresses(self) -> list[dict[object,object]]:
        sleep(2)
        return [
            {'rua': 'avenida Brasil'}
        ]

    def get_all_user_data(self) -> dict[Any,Any]:
        sleep(2)
        return {'rua': 'avenida Brasil'}


#Proxy
class ProxyUser(IUser):
    def __init__(self, firstname:str, lastname:str):
        self.first_name = firstname
        self.last_name = lastname
        self._real_user: RealUser
        self._chached_adresses: list[dict[Any, Any]] # Ainda nao existem nesse ponto
        self._all_user_data: dict[Any, Any]

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.first_name, self.last_name)

    def get_adresses(self) -> list[dict[object,object]]:
        self.get_real_user()
        if not hasattr(self, '_chached_adresses'):
            self._chached_adresses = self._real_user.get_adresses()
        return self._chached_adresses
    
    def get_all_user_data(self) -> dict[Any,Any]:
        self.get_real_user()
        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()
        return self._all_user_data


if __name__ == '__main__':
    luiz = ProxyUser('luiz', 'silva')
    print(luiz.first_name)

    print(luiz.get_all_user_data())
    print(luiz.get_all_user_data())
    print(luiz.get_adresses())