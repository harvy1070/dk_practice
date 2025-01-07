from abc import ABC, abstractmethod

# 추상 클래스 설정
class CarExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# 기본 명령어
class ActionExpression(CarExpression):
    def __init__(self, action):
        self.action = action

    def interpret(self, context):
        if self.action == "START":
            return f"{context} 시동 걸림"
        elif self.action == "STOP":
            return f"{context} 시동 꺼짐"
        elif self.action == "ACCELERATOR":
            return f"{context} 가속 중"
        elif self.action == "BRAKE":
            return f"{context} 감속 중"
        return f"알 수 없는 작동 명령어 ▶ {self.action}"
    
# 모드 설정
class ModeExpression(CarExpression):
    def __init__(self, mode):
        self.mode = mode

    def interpret(self, context):
        if self.mode == "SPORT":
            return f"{context} 스포츠 모드 설정"
        elif self.mode == "ECHO":
            return f"{context} 에코 모드 설정"
        elif self.mode == "COMPORT":
            return f"{context} 컴포트 모드 설정"
        return f"WARNING!!! {context} 모드는 지원되지 않는 모드임"
    
# 복합 명령어 설정
class SeqExpression(CarExpression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def interpret(self, context):
        return f"{self.exp1.interpret(context)} → {self.exp2.interpret(context)}"
    
# 명령어 해석기
class CarCommandInterpreter:
    def __init__(self, car_model):
        self.car_model = car_model
        self.exps = {}
        self.basic_command()

    def basic_command(self):
        # 기본 명령어
        self.exps["시동켜기"]

        # 모드 명령어