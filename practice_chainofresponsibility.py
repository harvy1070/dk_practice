from abc import ABC, abstractmethod

# 차량 점검 인터페이스(핸들러)
class CarInspectionHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        # 체이닝을 하기 위해 핸들러 반환
        return handler
    
    def handle(self, car, issue):
        # 현재 핸들러에서 처리 시도
        result = self.process_inspection(car, issue)

        # 처리되지 않았고, 다음 핸들러가 있다면 전달
        if not result and self.next_handler:
            return self.next_handler.handle(car, issue)
        return result
    
    @abstractmethod
    def process_inspection(self, car, issue):
        pass

# 구체적인 핸들러 파트
class BasicInspectionHandler(CarInspectionHandler):
    def process_inspection(self, car, issue):
        if issue in ['oil', 'filter', 'battery']:
            return f"{car} - 기본 점검 처리 ▶ {issue} 문제 해결"
        return None
    
class SafetyInspectionHandler(CarInspectionHandler):
    def process_inspection(self, car, issue):
        if issue in ["brake", "tire", "light"]:
            return f"{car} - 안전 점검 처리 ▶ {issue} 문제 해결"
        return None
    
class PerformanceInspectionHandler(CarInspectionHandler):
    def process_inspection(self, car, issue):
        if issue in ["engine", "transmission", "suspension"]:
            return f"{car} - 성능 점검 처리 ▶ {issue} 문제 해결"
        return None
    
# 정비소 파트
class ServiceCenter:
    def __init__(self):
        # 체인 생성 및 연결
        self.basic = BasicInspectionHandler()
        self.safety = SafetyInspectionHandler()
        self.performance = PerformanceInspectionHandler()

        # 체인 연결
        self.basic.set_next(self.safety).set_next(self.performance)

    def inspect_car(self, car, issue):
        result = self.basic.handle(car, issue)
        if result:
            return result
        return f"{car} - {issue} 문제는 처리가 불가능함"
    
if __name__ == "__main__":
    service_center = ServiceCenter()

    # 정비 테스트
    print(" === 차량 점검 시작 === ")
    print(service_center.inspect_car("Ferrari 812", "oil"))
    print(service_center.inspect_car("Ferrari 812", "brake"))
    print(service_center.inspect_car("Ferrari 812", "engine"))
    print(service_center.inspect_car("Ferrari 812", "paint"))
    print(service_center.inspect_car("Ferrari 812", "light"))