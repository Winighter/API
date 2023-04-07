import pythoncom,threading,datetime,time
import win32com.client as win32com


# 주간 야간 구분 세팅 -----------------------------------------------
ac = None
야간 = False
days = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
d = datetime.datetime.today().weekday()
h = time.localtime().tm_hour
m = time.localtime().tm_min
if 0 <= d <= 4:
    if (h >= 18) or (h <= 5):
        야간 = True
        ac = "야간 시장 시간 입니다"
    elif (15 >= h >= 9) or (h==15 and m <= 30):
        야간 = False
        ac = "정규 시장 시간 입니다"
    else:
        ac = "장 시장 시간 아닙니다"
    print("\n%s 접속 시간: %s시 %s분 / %s\n" % (days[d],h,m,ac))
else:
    print("\n장 날 아님\n")
# ------------------------------------------------------------------

선옵계좌 = 20572106402


class Info:
    # Real Info
    ID = "ypeace20"
    PW = "yw2603@@"
    Cert_PW = "c3484758!@"

    # Demo Info
    dPW = "yw2603"

class XAQuery:
    매수 = False
    t0441 = None
    cexaq = None
    cexaq_ok = None
    t0441_ok = False
    order = None
    orderNi = None

    if 야간 == True:
        def OnReceiveData(self, trCode):
            if trCode == "CEXAQ31100": # 실계좌 야간 잔고
                cnt = self.GetBlockCount("CEXAQ31100OutBlock3")

                if int(cnt) == 0:
                    if self.매수 == False:
                        if Call_일목균형표.CB_terms == True and Call_일목균형표.C26d == 1:
                            self.매수 = True
                            Call_일목균형표.CB_terms = False
                            print("콜 매수 시작")
                            Main.Order_Night(oCode=cCode,BnsTpCode="2",일시이지="2",OrdPrc="1.0",OrdQty=1)
                            

                        if Put_일목균형표.PB_terms == True and Put_일목균형표.P26d == 1:
                            self.매수 = True
                            Put_일목균형표.PB_terms = False
                            print("풋 매수 시작 %s" % Put_W.PB_terms)
                            Main.Order_Night(oCode=pCode,BnsTpCode="2",일시이지="2",OrdPrc="1.0",OrdQty=1) 

                elif int(cnt) > 0:
                    for i in range(cnt):
                        FnoIsuNo = self.GetFieldData("CEXAQ31100OutBlock3", "FnoIsuNo", i) # 종목번호
                        PnlRat = self.GetFieldData("CEXAQ31100OutBlock3", "PnlRat", i) # 손익율

                        if ((PnlRat <= -5) or (PnlRat >= 30)):
                            Call_일목균형표.CB_terms = False
                            Put_일목균형표.PB_terms = False
                            Call_W.CB_terms = False
                            Put_W.PB_terms = False
                            print("%s 매도 주문 시작 %s" % (FnoIsuNo,PnlRat))
                            Main.Order_Night(Accno=선옵계좌,PW=Info.PW,oCode=FnoIsuNo,BnsTpCode="1",일시이지="1",OrdPrc="0",OrdQty=1)
                            self.매수 = False

                        print("보유한 잔고 조회 - 종목번호: %s, 손익율: %s" % (FnoIsuNo,PnlRat))

                if self.IsNext is True:
                    threading.Timer(2, Main.야간옵션잔고, args=[선옵계좌, Info.PW, self.IsNext]).start()
                else:
                    XAQuery.t0441_ok = True
                    threading.Timer(2, Main.야간옵션잔고, args=[선옵계좌, Info.PW, False]).start()

            elif trCode == "CEXAT11100": # 야간 주문
                print



    # 야간장
    @staticmethod
    def 야간옵션잔고(Accno=None,PW=None,IsNext=False):
        XAQuery.cexaq.SetFieldData("CEXAQ31100InBlock1", "RecCnt", 0, "0") # 레코드 수
        XAQuery.cexaq.SetFieldData("CEXAQ31100InBlock1", "AcntNo", 0, Accno) # 계좌번호
        XAQuery.cexaq.SetFieldData("CEXAQ31100InBlock1", "InptPwd", 0, PW) # 아이디 비밀번호
        XAQuery.cexaq.SetFieldData("CEXAQ31100InBlock1", "IsuCode", 0, "") # 종목코드
        XAQuery.cexaq.SetFieldData("CEXAQ31100InBlock1", "BalEvalTp", 0, "1")
        XAQuery.cexaq.SetFieldData("CEXAQ31100InBlock1", "FutsPrcEvalTp", 0, "2")
        XAQuery.cexaq.Request(IsNext)
        XAQuery.cexaq_ok = False
        while XAQuery.cexaq_ok == False:
            pythoncom.PumpWaitingMessages()

  
    @staticmethod
    def Order_Night(oCode=None, BnsTpCode=None, 일시이지=None,OrdPrc=None,OrdQty=None):
        XAQuery.orderNi.SetFieldData("CEXAT11100InBlock1", "AcntNo", 0, 선옵계좌) # 계좌번호
        XAQuery.orderNi.SetFieldData("CEXAT11100InBlock1", "Pwd", 0, Info.PW) # 아이디 비밀번호
        XAQuery.orderNi.SetFieldData("CEXAT11100InBlock1", "FnoIsuNo", 0, oCode) # 종목코드
        XAQuery.orderNi.SetFieldData("CEXAT11100InBlock1", "BnsTpCode", 0, BnsTpCode) # 매매구분 1:매도 / 2:매수
        XAQuery.orderNi.SetFieldData("CEXAT11100InBlock1", "ErxPrcCndiTpCode", 0, 일시이지) # 1:시장가 / 2:지정가
        XAQuery.orderNi.SetFieldData("CEXAT11100InBlock1", "OrdPrc", 0, OrdPrc) # 주문가격
        XAQuery.orderNi.SetFieldData("CEXAT11100InBlock1", "OrdQty", 0, OrdQty) # 주문수량
        XAQuery.orderNi.Request(False)


if __name__ == "__main__":
    Main()