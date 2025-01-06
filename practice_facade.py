# 서브 시스템들
class Movie:
    pass

class Payment:
    pass

class Seat:
    pass

class Notification:
    pass

# Facade 클래스
class MovieFacade:
    def __init__(self):
        self.movie = Movie()
        self.payment = Payment()
        self.seat = Seat()
        self.notification = Notification()

    def MovieProcess(self, user_id, movie_id, seat_id, amount):
        """
        영화 예매를 위한 단순화된 인터페이스 생성해보기
        """

        print("\n === 영화 예매 시작 === ")

        # 가능 여부 확인
        # 좌석 예약
        # 결제 처리
        # 예매 확인 알람

# 유저 입장
if __name__ == "__main__":
    movie_system = MovieFacade()

    movie_system.MovieProcess(
        user_id = "harvy",
        movie_id = "범죄도시5",
        seat_id = "J12",
        amount = 15000
    )