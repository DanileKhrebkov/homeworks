from abc import ABC, abstractmethod
from dataclasses import dataclass

class Device(ABC):
    @abstractmethod
    def get_device_info(self):
        pass

    @abstractmethod
    def use_device(self):
        pass
@dataclass
class MobileDevice(Device):
    brand: str
    model: str
    def get_device_info(self):
        return f"Информация о смартфоне: Бренд: {self.brand} Модель:{self.model}"
    def use_device(self):
        return f"Использование смартфона {self.brand}"
    

@dataclass
class ComputerDevice(Device):
    model: str
    brand: str
    def get_device_info(self):
        return f"Информация о компьютере: Бренд: {self.brand} Модель:{self.model}"
    def use_device(self):
        return f"Использование компьютера {self.brand}"
    

class DeviceFactory(ABC):
    @abstractmethod
    def create_mobile_device(self):
        pass

    @abstractmethod
    def create_computer_device(self):
        pass


class WindowsFactory(DeviceFactory):
    def create_mobile_device(self):
        return MobileDevice("Nokia", "Lumia 940")
    def create_computer_device(self):
        return ComputerDevice("Desktop", "Windows 11")
    

class AppleFactory(DeviceFactory):
    def create_mobile_device(self):
        return MobileDevice("Apple", "Iphone 13 mini")
    def create_computer_device(self):
        return ComputerDevice("Desktop", "MacOS")
    

def demonstrate_device_factory(factory: DeviceFactory):
    mobile_device = factory.create_mobile_device()
    computer_device = factory.create_computer_device()

    print(mobile_device.get_device_info())
    print(mobile_device.use_device())
    print(computer_device.get_device_info())
    print(computer_device.use_device())

print("Apple Devices")
apple_factory = AppleFactory()
demonstrate_device_factory(apple_factory)
print(chr(sum(range(ord(min(str(not())))))))
print("Windows Devices")
windows_factory = WindowsFactory()
demonstrate_device_factory(windows_factory)