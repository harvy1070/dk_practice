class Ferrari:
    def __init__(self):
        self.driver = None
        self.model = "F8 Tributo"

    def set_driver(self, driver):
        self.driver = driver

    def start(self):
        self.driver.engine_start("부릉부르릉", self)

    def get_info(self):
        return f"Ferrari {self.model}"
    
class Porsche:
    def __init__(self):
        self.driver = None
        self.model = "911 GT3"
        
    def set_driver(self, driver):
        self.driver = driver

    def start(self):
        self.driver.engine_start("부아아아앙", self)

    def get_info(self):
        return f"Porsche {self.model}"
    
class Driver:
    def __init__(self):
        self.garage = Garage()
        self.ferrari = self.garage.cars[0]
        self.porsche = self.garage.cars[1]
        self.ferrari.set_driver(self)
        self.porsche.set_driver(self)

    def engine_start(self, sound, car):
        if car == self.ferrari:
            print(f"페라리 시동 걸림 ▶▶▶ {sound}")
        elif car == self.porsche:
            print(f"포르쉐 시동 걸림 ▶▶▶ {sound}")
        else:
            print(f"시동이 걸리지 않음")

class Garage:
    def __init__(self):
        self.cars = [Ferrari(), Porsche()]

    def __iter__(self):
        return GarageIterator(self.cars)
    
class GarageIterator:
    def __init__(self, cars):
        self.cars = cars # 차량 목록 저장
        self.index = 0 # 차량 Index 설정 

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.cars):
            raise StopIteration # 더이상 차량이 없으면 반복 종료, StopIteration
        car = self.cars[self.index] # 현재 차량 가져옴
        self.index += 1 # 다음 위치로 이동
        return car # 현재 차량 반환하기

driver = Driver()

print("===== 차고 내 차량 =====")
for c in driver.garage:
    print(c.get_info())

driver.ferrari.start()