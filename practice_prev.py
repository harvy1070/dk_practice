import sys

class Practice:
    @staticmethod
    def get_input():
        n, m = map(int, sys.stdin.readline().split())
        return n, m

    def solution1(self):
        n, m = self.get_input()
        x, y = 0, 0  # start
        dir = 0  # 시작 방향 초기화
        num = 1  # 채워갈 숫자

        # 맵 생성
        board = [[0] * m for _ in range(n)]

        # 우하좌상
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        while num <= m * n:
            board[x][y] = num  # 현재 위치에 num으로 현재 숫자 채움

            # 다음 위치 계산
            nx = x + dx[dir]
            ny = y + dy[dir]

            # 배열 범위를 벗어나거나, 숫자가 이미 채워진 경우 방향 전환
            if (nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != 0):
                dir = (dir + 1) % 4  # 0 1 2 3 순으로 방향 전환을 하기 위해 % 4(우하좌상)
                nx = x + dx[dir]
                ny = y + dy[dir]

                # 반복
            x, y = nx, ny  # 다음 위치로 이동
            num += 1  # 채울 숫자를 1씩 증가시킴

        return board


    def solution2(self):
        n, m = self.get_input()
        board = [[0] * m for _ in range(n)]

        num = 1
        # 총 대각선 길이 구하기
        tot_diag = n + m - 1

        for diag in range(tot_diag):
            # 좌표 저장 리스트
            fill = []

            # 각 행마다 해당 대각선에 포함되는 위치 찾기
            for r in range(n): # 우측부터 진행하기에 row값부터 시작
                # row + col = 현재 대각선 번호라는 성질을 활용
                # col = 현재 대각선 번호(diag) - row 성립
                c = diag - r

                # 열 번호가 0 이상이고 m 미만일 때만 진행
                if 0 <= c < m:
                    fill.append((r, c))

            # 대각선이 홀수번째일 때
            if diag % 2 != 0:
                fill.sort() # 오름차순 정렬
            # 대각선이 짝수번째 일때
            else:
                fill.sort(reverse=True) # 내림차순 정렬

            # 순서대로 채우기
            for r, c in fill:
                board[r][c] = num
                num += 1 # 다음 번호를 위해 숫자 1 증가

        return board

practice = Practice()
print(practice.solution1())
print(practice.solution2())