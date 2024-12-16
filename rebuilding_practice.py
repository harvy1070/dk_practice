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
            raise ValueError(f"보드 크기(n, m)는 {cls.min_size} 이상을 입력해야 함")
        return True

# 패턴 검증(유효한 패턴)
class P_Validator:
    all_pattern = ['spiral', 'diag']
    
    # cls로 클래스를 참조(val_pattern)하여 비교
    @classmethod
    def val_pattern(cls, p_type):
        if p_type not in cls.all_pattern:
            raise ValueError(f"유효한 패턴 타입이 아님, 가능한 패턴 => {cls.all_pattern}")
        return True
    
    @classmethod
    def get_val_pattern(cls):
        return cls.all_pattern
        
# n x m 크기의 보드 생성
class BoardGen:
    @staticmethod
    def create_board(n, m):
        return [[0] * m for _ in range(n)]

# 패턴 관리
class PatternAd:
    def __init__(self, n, m, board):
        self.n = n
        self.m = m
        self.board = board
        
    def gen_pattern(self, p_type):
        if p_type == 'spiral':
            return SpiralGen(self.n, self.m, self.board).spiral_al()
        elif p_type == 'diag':
            return DiagGen(self.n, self.m, self.board).diag_al()
        # 여기에 계속 추가

# 패턴 생성(나선형)
class SpiralGen:
    def __init__(self, n, m, board):
        self.n = n
        self.m = m
        self.board = board
    
    def spiral_al(self):
        x, y = 0, 0
        dir = 0
        num = 1  

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        while num <= self.m * self.n:
            self.board[x][y] = num
            nx = x + dx[dir]
            ny = y + dy[dir]

            if (nx < 0 or nx >= self.n or ny < 0 or ny >= self.m or self.board[nx][ny] != 0):
                dir = (dir + 1) % 4
                nx = x + dx[dir]
                ny = y + dy[dir]

            x, y = nx, ny
            num += 1

        return self.board

# 패턴 생성(대각선)
class DiagGen:
    def __init__(self, n, m, board):
        self.n = n
        self.m = m
        self.board = board

    def diag_al(self):
        num = 1
        tot_diag = self.n + self.m - 1

        for diag in range(tot_diag):
            fill = []

            for r in range(self.n):
                c = diag - r

                if 0 <= c < self.m:
                    fill.append((r, c))

            if diag % 2 != 0:
                fill.sort()
            else:
                fill.sort(reverse=True)

            for r, c in fill:
                self.board[r][c] = num
                num += 1
        return self.board

# 출력
class OutputHandler:
    @staticmethod
    def print_result(n, m, p_type, board):
        print(f"입력값 → n : {n} m : {m}, 패턴 타입 → {p_type}")
        print("======== 결과 출력 ========")
        for row in board:
            print(' '.join(f'{r:3}' for r in row))
        print("===========================")

# 메인 함수
def main():
    try:
        # 보드 크기 입력
        input_handler = GetInput()
        n, m = input_handler.get_board_size()
        
        # 보드 숫자 검증
        B_Validator.val_size(n, m)
        
        # 보드 생성
        board = BoardGen.create_board(n, m)

        # 패턴 타입 입력
        p_type = input_handler.get_p_type()
        
        # 패턴 타입 검증
        P_Validator.val_pattern(p_type)
        
        # 패턴 생성
        p_created = PatternAd(n, m, board)
        
        # 결과 저장
        result = p_created.gen_pattern(p_type)
        # print(result)

        # 결과 출력
        OutputHandler.print_result(n, m, p_type, result)
        
    except ValueError as e:
        print(e)
        
if __name__ == "__main__":
    main()