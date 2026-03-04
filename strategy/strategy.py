"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algorítmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value:float) -> float:
        pass



class Order:
    def __init__(self, total:float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total
    
    @property
    def total_with_discount(self):
        count =  self._discount.calculate(self.total)
        return count
    

class TwentyPercent(DiscountStrategy):
    def calculate(self, value:float):
        return value - (value * 0.2)
    
class FifityPercent(DiscountStrategy):
    def calculate(self, value:float):
        return value - (value * 0.5)
    
    
class NoDiscount(DiscountStrategy):
    def calculate(self, value:float):
        return value 
    
class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: float):
        self.discount = discount/100
        
    def calculate(self, value:float) -> float:
        return value - (value *self.discount)

    

if __name__ == '__main__':

    strategy1 = TwentyPercent()
    order1 = Order(1000,strategy1)
    print(order1.total, order1.total_with_discount)

    strategy2 = FifityPercent()
    order2 = Order(1000,strategy2)
    print(order2.total, order2.total_with_discount)

    strategy3 = CustomDiscount(12)
    order3 = Order(1000,strategy3)
    print(order3.total, order3.total_with_discount)