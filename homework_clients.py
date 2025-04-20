from dataclasses import dataclass
@dataclass
class ClientNode:
    name:str
    acc_number:int
    balance:float
    next = None
    prev = None


class BankClientList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_client(self, name, acc_number, balance):
        new_client = ClientNode( name, acc_number, balance)
        if not self.head:
            self.head = self.tail = new_client
        else:
            self.tail.next = new_client
            new_client.prev = self.tail
            self.tail = new_client
    
    def remove_client(self, acc_number):
        current = self.head

        while current and current.acc_number != acc_number:
            current = current.next

        if not current:
            return False
        
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
            return True
        


    def find_client(self, acc_number):
        current = self.head
        while current:
            if current.acc_number == acc_number:
                return True
            current = current.next
        return False
        
    
    def list_clients(self):
        current = self.head
        while current:
            print(f"Имя: {current.name}, Номер: {current.acc_number}, баланс: {current.balance}")
            current = current.next
    def update_balance(self, acc_number, balance):
        current = self.head
        while current:
            if current.acc_number == acc_number:
                current.balance = balance
            current = current.next
bank_list = BankClientList()
bank_list.add_client("Кристофер", 123, 1000)
bank_list.add_client("John", 124, 1311.11)
bank_list.add_client("Куин", 126, 55555)
bank_list.list_clients()
print(f"Был удален клиент с номером 124")
bank_list.remove_client(126)
bank_list.list_clients()