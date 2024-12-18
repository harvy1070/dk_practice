# 상태 저장
class CarMemento:
    def __init__(self, speed: int):
        self._speed = speed

# 상태를 가지는 객체
class Car:
    def __init__(self, model: str):
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        return f"{self.model}의 가속, 현재 속도 ▶ {self.speed}km/h"
    
    def brake(self):
        self.speed = max(0, self.speed - 10)
        return f"{self.model}의 감속, 현재 속도 ▶ {self.speed}km/h"
    
    # 상태 저장
    def save_state(self):
        return CarMemento(self.speed)
    
    # 상태 복원
    def res_state(self, memento: CarMemento):
        self.speed = memento._speed
        return f"{self.model}의 상태 복원, 현재 속도 ▶ {self.speed}km/h"

# Memento 관리하는 클래스 설정
class CarStateManager:
    def __init__(self):
        self._memento = [] # 상태를 저장하는 리스트를 설정해둠

    def backup(self, car: Car):
        self._memento.append(car.save_state())
        return "현재 상태 저장 성공"

    def undo(self, car: Car):
        if not self._memento:
            return "복원할 상태가 없음"
        
        memento = self._memento.pop()
        return car.res_state(memento)
    
if __name__ == "__main__":
    car = Car("BMW M5")
    state_manager = CarStateManager()

    # 초기 상태 저장
    print(" === 초기 상태 === ")
    print(state_manager.backup(car))

    # 가속 후 상태 저장
    print(" === 가속 상태 === ")
    print(car.accelerate())
    print(car.accelerate())
    print(state_manager.backup(car))

    # 추가 가속 후 저장
    print(" === 추가 가속 === ")
    print(car.accelerate())
    print(car.accelerate())

    # 이전 상태로 복원
    print(" === 이전 상태 === ")
    print(state_manager.undo(car))