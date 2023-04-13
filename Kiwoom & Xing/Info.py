# eBest Chart Data
ID = "" # 아이디 ex) abc1234
hts_pw = "" # 비밀번호 ex) a1b2c3
Cert_pw = "" # 인증서 비밀번호

# eBest 모의투자
demo_pw = ""
demo_acc_pw = "0000"

수량 = 4

# Dict
default_trendict = {'추세':0,'c시가고가':0,'p시가고가':0,'c손절':0,'p손절':0,'순매수량':0,'cCode':'','cPrice':0,'pCode':'','pPrice':0,'cTerms':0,'c26d':0,'pTerms':0,'p26d':0}
trendict = {'추세':0,'c시가고가':0,'p시가고가':0,'c손절':0,'p손절':0,'순매수량':0,'cCode':'','cPrice':0,'pCode':'','pPrice':0,'cTerms':0,'c26d':0,'pTerms':0,'p26d':0}
default_balance_dict = {'종목코드': '','구분':'','보유수량':0,'주문가능수량':0,'매입단가':0,'현재가':0,'약정금액':0,'평가금액':0,'수익률':0}
balance_dict = {'종목코드': '','구분':'','보유수량':0,'주문가능수량':0,'매입단가':0,'현재가':0,'약정금액':0,'평가금액':0,'수익률':0}
# 차트 옵션
n분 = "10" # n분 차트
when = "202305"
sigo_max = 11
sigo_min = 0.3

# 가격 범위
bas_max = 1.3
bas_min = 0.7

이익 = 30
손절 = -6

c호가 = 2000
p호가 = -2000

fCode = "101T6000"

Order_cancellation_range = 0.06

OCR = float(Order_cancellation_range)


# 손익율 = (평가금액 - 약정금액)/약정금액*100 -0.03%
