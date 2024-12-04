from abc import ABC, abstractmethod

# 옵저버 인터페이스
class Observer(ABC):
    @abstractmethod
    def update(self, message: str, m_type: str):
        pass

# 구체적인 옵저버들
class Mechanic(Observer):
    def update(self, message: str, m_type: str):
        if m_type == "car_status":
            print(f"정비사의 차량 상태 확인 : {message}")

class Owner(Observer):
    def update(self, message: str, m_type: str):
        if m_type == 'driver_status':
            print(f"차 주인 확인 : {message}")

class Car(ABC):
    def __init__(self):
        self.driver = None
        self.model = None
        self.observers = [] # 옵저버들 저장 리스트
    
    # 옵저버를 관리하는 메서드들
    def attach(self, observer:Observer):
        self.observers.append(observer)

    def detach(self, observer:Observer):
        self.observers.remove(observer)

    def notice(self, message: str, m_type: str):
        for ob in self.observers:
            ob.update(message, m_type)

    # 기존 템플릿 메서드 부분은 그대로 내비둠
    def drive_process(self, driver):
        self.set_driver(driver)
        self.engine_start()
        self.accelerate()
        self.brake()
    
    def set_driver(self, driver): 
        self.driver = driver
        self.notice(f"{driver.name}가 운전을 시작함", 'driver_status')
    
    @abstractmethod
    def engine_start(self): 
        pass
    
    @abstractmethod
    def accelerate(self): 
        pass
    
    def brake(self):  
        print("브레이크 밟기")
        self.notice("차량이 정지함", 'car_status')


class Ferrari(Car):
    def __init__(self):
        super().__init__()
        self.model = "F8 Tributo"
    
    def engine_start(self):
        print("페라리 시동 걸림 ▶▶▶ 부릉부르릉")
        self.notice("페라리가 시동이 걸렸습니다.", 'car_status')
    
    def accelerate(self):
        print("페라리 가속 ▶▶▶ 슈우우우웅")
        self.notice("페라리가 가속중입니다.", 'car_status')

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

if __name__ == "__main__":
    ferrari = Ferrari()
    porsche = Porsche()
    owner = Owner()
    mechanic = Mechanic()
    driver = Driver("sh.kwon")
    
    # 옵저버 등록
    ferrari.attach(mechanic)
    ferrari.attach(owner)

    print("=== 페라리 주행(고급 옵션 적용) ===")
    ferrari.drive_process(driver)
    print("\n=== 포르쉐 주행(옵션 없음) ===")
    porsche.drive_process(driver)