import sys

# 입력
class GetInput:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.p_type = ""

    def get_board_size(self):
        print("n(row)과 m(col)을 3 이상의 숫자로 입력 → ", end="", flush=True)
        self.n, self.m = map(int, sys.stdin.readline().split())
        return self.n, self.m
        
    def get_p_type(self):
        print("solution 타입을 영어로 입력(spiral, diag) → ", end="", flush=True)
        self.p_type = sys.stdin.readline().strip()
        return self.p_type

# n, m 값 검증(3 이상)
class B_Validator:
    min_size = 3
    
    @classmethod
    # @staticmethod
    def val_size(cls, n, m):
        if n < cls.min_size or m < cls.min_size:
            raise ValueError("보드 크기(n, m)는 {cls.min_size} 이상을 입력해야 함")
        return True

# 패턴 검증(유효한 패턴)
class P_Validator:
    val_pattern = ['spiral', 'diag']
    
    # cls로 클래스를 참조(val_pattern)하여 비교
    @classmethod
    def val_p(cls, p_type):
        if p_type not in cls.val_pattern:
            raise ValueError(f"유효한 패턴 타입이 아님, 가능한 패턴 => {cls.val_pattern}")
        return True
        
# n x m 크기의 보드 생성
class BoardGen:
    pass

# 패턴 관리
class PatternAd:
    pass

# 패턴 생성(나선형)
class SpiralGen:
    pass

# 패턴 생성(대각선)
class DiagGen:
    pass

# 출력
class OutputHandler:
    pass

def main():
    # 보드 크기 입력
    input_handler = GetInput()
    n, m = input_handler.get_board_size()
    
    # 보드 숫자 검증
    B_Validator.val_size(n, m)
    
    # 패턴 타입 입력
    p_handler = PatternAd(n, m)
    
    # 패턴 타입 검증
    P_Validator.val_pattern(p_handler)
    
    # 패턴 생성
    
    # 결과 출력
        
if __name__ == "__main__":
    main()