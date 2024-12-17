from abc import ABC, abstractmethod

class CarCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver
class Car:
    def __init__(self, model):
        self.model = model
        self.engine_on = False
        self.speed = 0

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            return f"{self.model} 시동 걸림 ▶ 부르릉"
        return f"{self.model} 시동이 이미 걸려있음"
    
    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return f"{self.model} 시동 꺼짐"
        return f"{self.model} 이미 시동이 꺼져있음"
    
    def accelerate(self):
        if self.engine_on:
            self.speed += 10
            return f"악셀레이터 작동, {self.model} 가속 ▶ 현재 속도 {self.speed}km/h"
        return f"WARNING!! {self.model}의 시동이 꺼져있어서 가속할 수 없음"
    
    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            return f"브레이크 작동, {self.model} 감속 ▶ 현재 속도 {self.speed}km/h"
        return f"{self.model} 차량 정지됨(Parking)"
    
# Concrete Commmands
# 엔진 시동
class SE_Command(CarCommand):
    def __init__(self, car):
        self.car = car

    def execute(self):
        return self.car.start_engine()
    
    def undo(self):
        return self.car.stop_engine()
    
# 악셀 작동
class AC_Command(CarCommand):
    def __init__(self, car):
        self.car = car

    def execute(self):
        return self.car.accelerate()
    
    def undo(self):
        return self.car.brake()
    
# 명령 실행 객체
class Driver:
    def __init__(self):
        self.command_his = []

    def ex_command(self, command):
        result = command.execute()
        self.command_his.append(command)
        return result
    
    def undo_command(self):
        if self.command_his:
            last_com = self.command_his.pop()
            return last_com.undo()
        return "실행 취소할 명령 없음"
    
# Client 부분
if __name__ == "__main__":
    Mercedes = Car("Mercedes AMG GT 63")
    driver = Driver()
    
    start_engine = SE_Command(Mercedes)
    accelerate = AC_Command(Mercedes)

    print("=== 정상 시나리오 ===")
    print(driver.ex_command(start_engine))
    print(driver.ex_command(accelerate))
    print(driver.ex_command(accelerate))
    
    print("=== 명령 취소 시나리오 ===")
    print(driver.undo_command())
    print(driver.undo_command())
    print(driver.undo_command())
    