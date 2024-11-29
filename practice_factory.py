import sys
from abc import ABC, abstractmethod

# 추상 클래스 생성
# 입력은 n, m, type을 고정으로 해도될 것 같기에 삭제
# class Factory(ABC):
#     @abstractmethod
#     def create_solution(self, n, m, board, sol_type):
#         pass

class GetInput:
    def __init__(self):
        self.n = 0
        self.m = 0

    def get_input(self):
        print("n(row)과 m(col)을 숫자로 입력 → ", end="", flush=True)
        self.n, self.m = map(int, sys.stdin.readline().split())
        print("solution 타입을 영어로 입력(spiral, diag) → ", end="", flush=True)
        sol_type = sys.stdin.readline().strip()
        board = self.created_map()

        solution = self.create_solution(self.n, self.m, board, sol_type)
        return solution
    
    def created_map(self):
        board = [[0] * self.m for _ in range(self.n)]
        return board

    def create_solution(self, n, m, board, sol_type):
        if sol_type == 'spiral':
            return "spiral", solution1(n, m, board).spiral_al()
        elif sol_type == 'diag':
            return "diag", solution2(n, m, board).diag_al()
        else:
            raise ValueError("아직 생성되지 않은 타입")

class solution1: # spiral
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

class solution2: # diag
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

def main():
    try:
        input_handler = GetInput()
        sol_type, solution = input_handler.get_input()

        # if isinstance(solution, solution1):
        #     print("===== Spiral =====")
        #     print(solution.spiral_al())

        # elif isinstance(solution, solution2):
        #     print("=====  Diag  =====")
        #     print(solution.diag_al())

        if sol_type == "spiral":
            print("===== Spiral =====")
        elif sol_type == "diag":
            print("=====  Diag  =====")
        print(solution)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()