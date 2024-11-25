import sys
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
        return self.n, self.m, sol_type, board
    
    def created_map(self):
        board = [[0] * self.m for _ in range(self.n)]
        return board

class solution1:
    def __init__(self, n, m, board):
        self.n = n
        self.m = m
        self.board = board
    
    def sol1(self):
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

class solution2:
    def __init__(self, n, m, board):
        self.n = n
        self.m = m
        self.board = board

    def sol2(self):
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
    # n, m, sol_type, board = GetInput.get_input() 
    input_handler = GetInput() # 인스턴스를 생성해야함
    n, m, sol_type, board = input_handler.get_input()
    
    spiral = solution1(n, m, board)
    diag = solution2(n, m, board)

    if sol_type == 'spiral':
        print("===== Spiral =====")
        print(spiral.sol1())
    elif sol_type == 'diag':
        print("=====  Diag  =====")
        print(diag.sol2())

if __name__ == "__main__":
    main()