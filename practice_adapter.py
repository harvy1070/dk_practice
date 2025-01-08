# 본사 시스템의 결제 인터페이스
class PaymentInterface:
    def process_payment(self, amount):
        pass
    
    def refund_payment(self, trans_id):
        pass

'''
카카오사와 Toss사의 다른 네이밍을 사용한 동일 기능일 때에 대한 상황에 맞게 코드 작성(코드와 받는 변수명도 다르게)
- 카카오 : send_payment1, Toss : send_payment2
'''
# 카카오사 PG
class Kakao:
    # 결제 요청
    def send_payment1(self, amount):
        pass

    # 취소 요청
    def cancel_payment(self, tid):
        pass

# 토스사 PG
class Toss:
    # 결제 요청
    def send_payment2(self, amount, curr):
        pass
    
    # 취소 요청
    def cancel_payment(self, payment_id, reason):
        pass

# 카카오 어댑터
class KakaoAdapter:
    def __init__(self):
        pass

    def process_payment(self, amount):
        pass

    def refund_payment(self, transaction_id):
        pass

# 토스 어댑터
class TossAdapter:
    def __init__(self):
        pass

    def process_payment(self, amount):
        pass

    def refund_payment(self, transaction_id):
        pass

# 결제 처리 클래스
class PaymentProcess:
    def __init__(self):
        pass

    def make_payment(self, amount):
        pass

if __name__ == "__main__":
    # Kakao
    kakao_payment = PaymentProcess(KakaoAdapter())
    kakao_payment.make_payment(50000)

    # TOss
    toss_payment = PaymentProcess(TossAdapter())
    toss_payment.make_payment(30000)
