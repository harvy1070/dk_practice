from abc import ABC, abstractmethod

class DriveStrategy(ABC):
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

class NormalStrategy(DriveStrategy):
    def accelerate(self):
        return "일반 모드 가속, +10km/h"
    
    def brake(self):
        return "일반 모드 감속 -10km/h"
    
class SportStrategy(DriveStrategy):
    def accelerate(self):
        return "스포츠 모드 가속 +20km/h"
    
    def brake(self):
        return "스포츠 모드 감속 -20km/h"
    
class EchoStrategy(DriveStrategy):
    def accelerate(self):
        return "에코 모드 가속 +5km/h"
    
    def brake(self):
        return "에코 모드 감속 -5km/h"
    
class Car:
    def __init__(self, model):
        self.model = model
        self.drive_strategy = NormalStrategy() # 기본 전략

    def set_drive_mode(self, strategy: DriveStrategy):
        self.drive_strategy = strategy

    def accelerate(self):
        return f"{self.model} ▶ {self.drive_strategy.accelerate()}"
    
    def brake(self):
        return f"{self.model} ▶ {self.drive_strategy.brake()}"

if __name__ == "__main__":
    mercedes = Car("Mercedes AMG E53")

    # Comport
    print(" === Comport 주행 === ")
    print(mercedes.accelerate())
    print(mercedes.brake())

    # Sport
    print(" === Sport 주행 === ")
    mercedes.set_drive_mode(SportStrategy())
    print(mercedes.accelerate())
    print(mercedes.brake())

    # Echo
    print(" === Echo 주행 === ")
    mercedes.set_drive_mode(EchoStrategy())
    print(mercedes.accelerate())
    print(mercedes.brake())