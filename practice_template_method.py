from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self):
        self.driver = None
        self.model = None
    
    # 템플릿 메서드 - 차량 시동/주행(공통)
    def drive_process(self, driver):
        self.set_driver(driver)
        self.engine_start()
        self.accelerate()
        self.brake()
    
    def set_driver(self, driver): # 공통 동작
        self.driver = driver
    
    @abstractmethod
    def engine_start(self): # 개별 동작은 Pass로 각자 클래스에서 설정
        pass
    
    @abstractmethod
    def accelerate(self): # 개별 동작은 Pass로 각자 클래스에서 설정
        pass
    
    def brake(self):  # 공통 동작
        print("브레이크 밟기")

# 구체 클래스들
class Ferrari(Car):
    def __init__(self):
        super().__init__()
        self.model = "F8 Tributo"
    
    def engine_start(self):
        print("페라리 시동 걸림 ▶▶▶ 부릉부르릉")
    
    def accelerate(self):
        print("페라리 가속 ▶▶▶ 슈우우우웅")

class Porsche(Car):
    def __init__(self):
        super().__init__()
        self.model = "911 GT3"
    
    def engine_start(self):
        print("포르쉐 시동 걸림 ▶▶▶ 부아아아앙")
    
    def accelerate(self):
        print("포르쉐 가속 ▶▶▶ 부우우우우우웅")

class Driver:
    def __init__(self, name):
        self.name = name

ferrari = Ferrari()
porsche = Porsche()
driver = Driver("sh.kwon")

print("=== 페라리 주행 ===")
ferrari.drive_process(driver)
print("\n=== 포르쉐 주행 ===")
porsche.drive_process(driver)