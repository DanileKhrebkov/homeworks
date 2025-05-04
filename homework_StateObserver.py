from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, state: str):
        pass

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
        self._state = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self.notify()

class State(ABC):
    @abstractmethod
    def handle(self):
        pass

class OnlineState(State):
    def handle(self):
        return "Online"

class AwayState(State):
    def handle(self):
        return "Away"

class DoNotDisturbState(State):
    def handle(self):
        return "Do Not Disturb"

class UserStatus:
    def __init__(self):
        self._state = None
        self.subject = Subject()

    def change_state(self, state: State):
        self._state = state
        status = state.handle()
        if status != "Do Not Disturb":
            self.subject.state = status

class StatusObserver(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, state: str):
        print(f"{self.name} received update: User is now {state}")

if __name__ == "__main__":
    user_status = UserStatus()
    observer1 = StatusObserver("Observer 1")
    observer2 = StatusObserver("Observer 2")

    user_status.subject.attach(observer1)
    user_status.subject.attach(observer2)

    user_status.change_state(OnlineState())
    user_status.change_state(AwayState())
    user_status.change_state(DoNotDisturbState())