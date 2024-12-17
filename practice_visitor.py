from abc import ABC, abstractmethod

# Element 인터페이스
class CarElement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# 실제 부품들(engine, tire, body)
class Engine(CarElement):
    def __init__(self, condition):
        self.condition = condition

    def accept(self, visitor):
        return visitor.visit_engine(self)
    
class Tire(CarElement):
    def __init__(self, pressure):
        self.pressure = pressure

    def accept(self, visitor):
        return visitor.visit_tire(self)
        
class Body(CarElement):
    def __init__(self, paint):
        self.paint = paint

    def accept(self, visitor):
        return visitor.visit_body(self)


# 기본 Visitor 인터페이스 정의
class CarInspector(ABC):
    @abstractmethod
    def visit_engine(self, engine):
        pass

    @abstractmethod
    def visit_tire(self, tire):
        pass

    @abstractmethod
    def visit_body(self, body):
        pass

# 안전 점검
class SafetyInspect(CarInspector):
    def visit_engine(self, engine):
        sf_score = ""

        if engine.condition > 80: sf_score = "양호"
        else: sf_score = "점검 필요"
        
        return f"엔진 안전 점검 : {sf_score}"
    
    def visit_tire(self, tire):
        if tire.pressure < 30: return "WARNING!! 타이어 공기압 부족"
        elif tire.pressure > 35: return "WARNING!! 타이어 공기압 과다"
        else: return "타이어 공기압 정상"

    def visit_body(self, body):
        sf_score = ""
        if body.paint > 70: sf_score = "양호"
        else: sf_score = "도색 필요"
        return f"도색 점검 : {sf_score}"
    
# 메인 안전 진단
class MainInspector(CarInspector):
    def visit_engine(self, engine):
        if engine.condition < 90:
            return f"엔진 상태 ▶ 점검 필요, {engine.condition}"
        return "엔진 상태 정상"

    def visit_tire(self, tire):
        tire_status = []
        if tire.pressure < 32: tire_status.append("공기압 보충")
        elif tire.pressure > 34: tire_status.append("공기압 조정")
        
        if tire_status:
            return f"타이어 상태 ▶ {tire_status}"
        else:
            return "타이어 상태 정상"

    def visit_body(self, body):
        if body.paint < 95:
            return "광택 작업 권장"
        return "외관 상태 정상"

# Car 클래스
class Car(CarElement):
    def __init__(self, model):
        self.model = model
        self.elements = [
            Engine(90),
            Tire(32),
            Body(95)
        ]

    def accept(self, visitor):
        result = []
        for e in self.elements:
            result.append(e.accept(visitor))
        return f"{self.model} 점검 결과 ▶ {result}"
    
if __name__ == "__main__":
    ferrari = Car("Ferrari 812 SuperFast")

    sf_inspector = SafetyInspect()
    print("=== 안전 검사 결과 ===")
    print(ferrari.accept(sf_inspector))

    print("=== 유지보수 점검 결과 ===")
    main_inspector = MainInspector()
    print(ferrari.accept(main_inspector))