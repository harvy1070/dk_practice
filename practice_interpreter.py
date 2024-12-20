from abc import ABC, abstractmethod

# 추상 클래스 설정
class CarExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# 기본 명령어