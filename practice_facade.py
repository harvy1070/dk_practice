import sys

# 서브 시스템들
class Movie:
    def checkmovie(self, movie_id):
        if movie_id == "종영영화":
            print(f"{movie_id}는 상영이 종료된 상태입니다.")
            return False
        print(f"영화 {movie_id}의 상영 가능 여부 확인")
        return True

class Payment:
    def checkpayment(self, amount):
        if amount > 20000:
            print(f"{amount}원은 한도 초과입니다.")
            return False
        print(f"{amount}원 결제 완료")
        return True

class Seat:
    def checkseat(self, seat_id):
        if seat_id == "A1":
            print((f"{seat_id}는 이미 예약된 좌석입니다."))
            return False
        print(f"{seat_id} 좌석 예약 완료")
        return True

class Notification:
    def checkNotification(self, user_id):
        print(f"{user_id} 예매 확인 알림 전송")

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
        if not self.movie.checkmovie(movie_id):
            print("해당 영화는 예매할 수 없습니다.")
            return False
        
        # 좌석 예약
        if not self.seat.checkseat(seat_id):
            print("해당 좌석은 예매할 수 없습니다.")
            return False
        
        # 결제 처리
        if not self.payment.checkpayment(amount):
            print("잔액이 부족하여 결제가 되지 않았습니다.")
            return False

        # 예매 확인 알람
        self.notification.checkNotification(user_id)
        print(" === 예매 완료 === ")
        return True


# 유저 입장
if __name__ == "__main__":
    movie_system = MovieFacade()

    print("\n === 영화 예매 시스템 시작 === ")
    
    print("사용자 ID 입력 ▶ ", end = '', flush=True)
    user_id = sys.stdin.readline().strip()
    print(f"입력된 아이디 ▶ {user_id}")

    print("영화 제목 입력 ▶ ", end = '', flush=True)
    movie_id = sys.stdin.readline().strip()

    print("좌석 번호 입력(A1 ~ Z12) ▶ ", end = '', flush=True)
    seat_id = sys.stdin.readline().strip()

    print("결제 금액 입력 ▶ ", end = '', flush=True)
    amount = int(sys.stdin.readline().strip())

    movie_system.MovieProcess(
        user_id=user_id,
        movie_id=movie_id,
        seat_id=seat_id,
        amount=amount
    )