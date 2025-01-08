# 본사 시스템의 결제 인터페이스

class PaymentInterface:
    def process_payment(self, amount):
        pass
    def refund_payment(self, trans_id):
        pass

# 카카오사 PG
class Kakao:
    # 결제 요청
    def send_payment(self, amount):
        pass
    # 취소 요청
    def cancel_payment(self, tid):
        pass

# 토스사 PG
class Toss:
    