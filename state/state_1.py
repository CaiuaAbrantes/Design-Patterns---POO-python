"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class Order:
    #context
    def __init__(self):
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        self.state.pending()
        print()
    
    def aprove(self):
        self.state.approve()
        print()

    def reject(self):
        self.state.reject()
        print()

    def atual_state(self):
        print(f'state: {self.state}')
        print()


class OrderState(ABC):
    def __init__(self, order:Order):
        self.order = order

    @abstractmethod
    def pending(self)->None:
        pass

    @abstractmethod
    def approve(self)->None:
        pass

    @abstractmethod
    def reject(self)->None:
        pass

    def __str__(self):
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self)->None:
        print('pagamento ja pendente')

    def approve(self)->None:
        print('pagamento aprovado')
        self.order.state = PaymentApproved(self.order)

    def reject(self)->None:
        print('pagamento rejeitado')
        self.order.state = PaymentRejected(self.order)

class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente')

    def approve(self) -> None:
        print('Pagamento já aprovado, não posso fazer nada.')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado')

class PaymentRejected(OrderState):
    def pending(self) -> None:
        print('Pagamento recusado. Não vou mover para pendente.')

    def approve(self) -> None:
        print('Pagamento recusado. Não vou recusar novamente.')

    def reject(self) -> None:
        print('Pagamento recusado. Não vou recusar novamente.')

if __name__ == "__main__":
    order = Order()
    order.aprove()
    order.aprove()
    order.pending()
    order.pending()
    order.reject()
    order.reject()
    order.pending()
    order.aprove()
    order.atual_state()
  