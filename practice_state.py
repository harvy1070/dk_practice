from abc import ABC, abstractmethod

# 상태 인터페이스
class CarState(ABC):
    @abstractmethod
    def start_engine(self, car):
        pass

    @abstractmethod
    def accelerate(self, car):
        pass

    @abstractmethod
    def brake(self, car):
        pass

    @abstractmethod
    def park(self, car):
        pass

# 구체적 상태 클래스(Stop, Driving, Parking)
# 주차 상태
class ParkingState(CarState):
    def start_engine(self, car):
        print("시동이 걸림")
        car.change_state(StoppedState())

    def accelerate(self, car):
        print("WARNING! 주차 상태에서는 가속할 수 없음")

    def brake(self, car):
        print("WARNING! 주차 상태에서는 브레이크 작동을 하지 않음")

    def park(self, car):
        print("WARNING! 이미 주차 상태입니다.")

# 정차 상태
class StoppedState(CarState):
    def start_engine(self, car):
        print("WARNING! 이미 시동이 걸려있습니다.")

    def accelerate(self, car):
        print("차가 앞으로 감")
        car.change_state(DrivingState())


    def brake(self, car):
        print("파킹 시스템 작동(시동중)")

    def park(self, car):
        print("주차 모드로 전환")
        car.change_state(ParkingState())

class DrivingState(CarState):
    def start_engine(self, car):
        print("WARNING! 이미 주행 중 입니다.")

    def accelerate(self, car):
        print("가속 중입니다.")

    def brake(self, car):
        print("차량이 정지합니다.")
        car.change_state(StoppedState())

    def park(self, car):
        print("WARNING! 주행 중에는 주차할 수 없음")

# Car
class Car:
    def __init__(self, model):
        self.model = model
        # 초기 상태를 주차 상태로 설정
        self.state = ParkingState()

    def change_state(self, state):
        self.state = state

    def start_engine(self):
        print(f"{self.model} 시동 시도 ▶ ", end="")
        self.state.start_engine(self)

    def accelerate(self):
        print(f"{self.model} 가속 시도 ▶ ", end="")
        self.state.accelerate(self)

    def brake(self):
        print(f"{self.model} 정지 시도 ▶ ", end="")
        self.state.brake(self)

    def park(self):
        print(f"{self.model} 주차 시도 ▶ ", end="")
        self.state.park(self)

if __name__ == "__main__":
    ferrari = Car("Ferrari 812 SuperFast")

    # 시나리오 1 - 정상적 주행 순서
    print("=== 정상 주행 시나리오 ===")
    ferrari.start_engine()
    ferrari.accelerate()
    ferrari.brake()
    ferrari.park()

    # 시나리오 2- 잘못된 조작
    print("\n=== 잘못된 조작 시나리오 ===")

    # 엔진 시동을 걸지 않은 상태로 가속
    ferrari.accelerate()

    # 시동이 걸린 상태에서 한번 더 시동
    ferrari.start_engine() 
    ferrari.start_engine()

    # 시동상태에서 정지하지 않고 바로 주차
    ferrari.accelerate()
    ferrari.park()