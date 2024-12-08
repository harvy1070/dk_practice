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
    pass

# 패턴 검증(유효한 패턴)
class P_Validator:
    pass

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