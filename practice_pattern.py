import sys
class GetInput:
    @staticmethod
    def get_input():
        n, m = map(int, sys.stdin.readline().split())
        sol_type = sys.stdin.readline().strip()
        board = [[0] * m for _ in range(n)]
        return n, m, sol_type, board

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
    n, m, sol_type, board = GetInput.get_input()
    
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