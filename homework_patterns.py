#NOTIFICATION(BRIDGE)
from abc import ABC, abstractmethod

class Notification_sender(ABC):
    @abstractmethod
    def send(self, message): ...
#Realisation of interface
class EmailNotif(Notification_sender):
    def send(self, message):
        return f"[email] sending: {message}"
     
class SMSNotif(Notification_sender):
    def send(self, message):
        return f"[number] sending: {message}"
    
class Notification(ABC):
    def __init__(self,sender):
        self.sender = sender

    def notify(self, message:str): ...


class AlertNotification(Notification):
    def notify(self, message: str):
        return self.sender.send(message)

email = EmailNotif()
sms = SMSNotif()

alert = AlertNotification(email)
print(alert.notify("система перегружена"))


alert.sender = sms
print(alert.notify("Низкий уровень заряда"))


class PushNotification:
    def push(self, content:str):
        return f"[push] sending {content}"
    
class PushNotificationAdapter(Notification_sender):
    def __init__(self, adaptee: PushNotification):
        self.adaptee = adaptee
    
    def send(self, message):
        return self.adaptee.push(message)
    


push = PushNotification()
adapter = PushNotificationAdapter(push)
alert = AlertNotification(adapter)
print(alert.notify("Новый способ сообщения"))


class BaseNotification(ABC):
    @abstractmethod
    def notify(self, message): ...

class SimpleNotification(BaseNotification):
    def __init__(self, sender: BaseNotification):
        self.sender = sender

    def notify(self, message):
        return self.sender.send(message)
    
class UrgentNotification(BaseNotification):
    def __init__(self, wrapped: BaseNotification):
        self.wrapped = wrapped

    def notify(self, message):
        return "[URGENT]" + " " + self.wrapped.notify(message)
    
email = EmailNotif()
simple = SimpleNotification(email)

urgent = UrgentNotification(simple)
urgent.notify("Сервер упал")