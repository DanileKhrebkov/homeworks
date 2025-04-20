from abc import ABC, abstractmethod
from dataclasses import dataclass
class Order(ABC):
    @abstractmethod
    def processorder(self):
        pass


class RegularOrder(Order):
    def processorder(self):
        return "Обычный заказ обрабатывается стандартным способом"
    

class UrgentOrder(Order):
    def processorder(self):
        return "Срочный заказ, проиоритетное задание"
    


class InternationalOrder(Order):
    def processorder(self):
        return "международный заказ обрабатывается с учетом таможни"
    

class OrderFactory(ABC):
    @abstractmethod
    def create_order(self):
        pass



class RegularOrderFactory(OrderFactory):
    def create_order(self):
        return RegularOrder()
    
class UrgentOrderFactory(OrderFactory):
    def create_order(self):
        return UrgentOrder()
    
class InternationalOrderFactory(OrderFactory):
    def create_order(self):
        return InternationalOrder()
    
def work_order(factory: OrderFactory):
    order = factory.create_order()
    print(order.processorder())

regularorderfactory = RegularOrderFactory()
urgentorderfactory = UrgentOrderFactory()
internationalorderfactory = InternationalOrderFactory()

work_order(regularorderfactory)
work_order(urgentorderfactory)
work_order(internationalorderfactory)