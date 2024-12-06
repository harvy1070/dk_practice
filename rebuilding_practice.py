import sys

# 입력
class GetInput:
    def __init__(self):
        self.n = 0
        self.m = 0

    def get_input(self):
        print("n(row)과 m(col)을 3 이상의 숫자로 입력 → ", end="", flush=True)
        self.n, self.m = map(int, sys.stdin.readline().split())

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