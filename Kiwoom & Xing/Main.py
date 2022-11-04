from os import *
import sys,time,pythoncom,threading
import win32com.client as win32com
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from config.Info import *
from config.errorCode import *
from config.Option_Code import *
from playsound import playsound


class A:
    Call_일목 = None
    Put_일목 = None
    Call_이평 = None
    Put_이평 = None
    
    n분 = "10" # n분봉차트


class Snd: # Sound files
    매수신호발생 = 'E:\Program\Python\FaO\config\sound\Kiwoom\매수신호발생1.wav'
    매도신호발생 = 'E:\Program\Python\FaO\config\sound\Kiwoom\매도신호발생1.wav'
    

class HTS: # HTS 로그인
    login_state = 0
    def OnLogin(self, szCode, szMsg):
        if szCode == "0000":
            HTS.login_state = 1
        else:
            print("[X] HTS Login failed !!! [%s]\n" % szCode)


class Call_일목균형표:
    C26d = 0
    CB_terms = False
    def OnReceiveChartRealData(self, trCode):
        현재가 = self.GetFieldChartRealData("ChartIndexOutBlock1", "close") # 현재가(종가)
        현재가 = float(현재가)

        기준선 = self.GetFieldChartRealData("ChartIndexOutBlock1", "value2") # 기준선
        기준선 = float(기준선)
        
        if 현재가 > 기준선 > 0:
            Call_일목균형표.C26d = 1
        elif 현재가 < 기준선 and 기준선 > 0:
            Call_일목균형표.C26d = -1
            Call_일목균형표.CB_terms = True
        else:
            Call_일목균형표.C26d = 0


class Put_일목균형표:
    P26d = 0
    PB_terms = False
    def OnReceiveChartRealData(self, trCode):
        
        현재가 = self.GetFieldChartRealData("ChartIndexOutBlock1", "close") # 현재가(종가)
        현재가 = float(현재가)

        기준선 = self.GetFieldChartRealData("ChartIndexOutBlock1", "value2") # 기준선
        기준선 = float(기준선)

        if 현재가 > 기준선 > 0:
            Put_일목균형표.P26d = 1
        elif 현재가 < 기준선 and 기준선 > 0:
            Put_일목균형표.P26d = -1
            Put_일목균형표.PB_terms = True
        else:
            Put_일목균형표.P26d = 0


class Call_가격이동평균(A):
    def OnReceiveChartRealData(self, trCode):
        현재가 = self.GetFieldChartRealData("ChartIndexOutBlock1", "close") # 현재가(종가)
        현재가 = float(현재가)

        value = self.GetFieldChartRealData("ChartIndexOutBlock1", "value1")
        value = float(value)
        print(value)


class Put_가격이동평균(A):
    def OnReceiveChartRealData(self, trCode):
        
        현재가 = self.GetFieldChartRealData("ChartIndexOutBlock1", "close") # 현재가(종가)
        현재가 = float(현재가)

        value = self.GetFieldChartRealData("ChartIndexOutBlock1", "value1")
        value = float(value)
        print(value)


class KXing(QAxWidget,A):
    
    def __init__(self):
        super().__init__()

        self.매수 = False
        self.qty = 4 # 주문 수량

        self.login_event_loop = QEventLoop()

        self.실시간미체결딕셔너리 = {}
        self.jango_dict = {}
        
        self.get_ocx_instance()

        self.event_slots()
        self.real_event_slot()
        self.signal_login_commConnect()
        self.get_account_info()

        self.dynamicCall("SetRealReg(QString, QString, QString, QString)", "5000", '', 215, "0")
        self.dynamicCall("SetRealReg(QString, QString, QString, QString)", "9000", fCode, 10, "0")
        for code in (cCode,pCode):
            self.dynamicCall("SetRealReg(QString, QString, QString, QString)", "6000", code, 20, "1")

        Xing = win32com.DispatchWithEvents("XA_Session.XASession", HTS)

        A.Call_일목 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", Call_일목균형표)
        A.Call_일목.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"

        A.Put_일목 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", Put_일목균형표)
        A.Put_일목.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"

        A.Call_이평 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", Call_일목균형표)
        A.Call_이평.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"

        A.Put_이평 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", Put_일목균형표)
        A.Put_이평.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"


        # HTS 로그인
        Xing.ConnectServer(hts_IP, Port)
        if Xing.Login(ID, hts_pw, Cert_pw, 0, True) is True:
            pass
        else:
            nErrCode = Xing.GetLastError()
            strErrMsg = Xing.GetErrorMessage(nErrCode)
            print("\n[X] HTS Server Connection Failed !!! [%s] %s" % (nErrCode, strErrMsg))
        while HTS.login_state == 0:
            pythoncom.PumpWaitingMessages()

        self.Call_일목균형표요청()
        self.Put_일목균형표요청()
        time.sleep(1.1)
        self.Call_이평선요청()
        self.Put_이평선요청()
        while True:
            pythoncom.PumpWaitingMessages()


    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")


    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)
        self.OnReceiveMsg.connect(self.msg_slot)


    def real_event_slot(self):
        self.OnReceiveRealData.connect(self.realdata_slot)
        self.OnReceiveChejanData.connect(self.chejan_slot)


    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop.exec_()


    def login_slot(self, err_code):
        print(errors(err_code)[1])
        self.login_event_loop.exit()


    def get_account_info(self):
        accno = self.dynamicCall("GetLoginInfo(QString)", "ACCNO")
        accno = accno.split(';')[0]
        self.accno = accno
        user_name = self.dynamicCall("GetLoginInfo(QString)", "USER_NAME")
        print("%s님의 계좌번호: %s" %(user_name,accno))


    def Call_일목균형표요청(self):
        A.Call_일목.SetFieldData("ChartIndexInBlock", "indexid", 0, "") # 지표ID
        A.Call_일목.SetFieldData("ChartIndexInBlock", "indexname", 0, "일목균형표") # 지표명
        A.Call_일목.SetFieldData("ChartIndexInBlock", "indexparam", 0, "") # 지표조건설정
        A.Call_일목.SetFieldData("ChartIndexInBlock", "market", 0, "5") # 시장구분
        A.Call_일목.SetFieldData("ChartIndexInBlock", "period", 0, "1") # 주기 구분 # 분:1 / 일:2
        A.Call_일목.SetFieldData("ChartIndexInBlock", "shcode", 0, cCode) # 종목코드
        A.Call_일목.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500") # 요청 건수 (최대 500개) 1일=39개
        A.Call_일목.SetFieldData("ChartIndexInBlock", "ncnt", 0, A.n분) # 단위 n 틱/분 만 해당
        A.Call_일목.SetFieldData("ChartIndexInBlock", "sdate", 0, "") # 시작 일자
        A.Call_일목.SetFieldData("ChartIndexInBlock", "edate", 0, "") # 종료 일자
        A.Call_일목.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1") # 수정주가반영여부
        A.Call_일목.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0") # 갭보정 여부
        A.Call_일목.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1") # 실시간자동등록 여부
        A.Call_일목.RequestService("ChartIndex", 0)


    def Put_일목균형표요청(self):
        time.sleep(1.1)
        A.Put_일목.SetFieldData("ChartIndexInBlock", "indexid", 0, "") # 지표ID
        A.Put_일목.SetFieldData("ChartIndexInBlock", "indexname", 0, "일목균형표") # 지표명
        A.Put_일목.SetFieldData("ChartIndexInBlock", "indexparam", 0, "") # 지표조건설정
        A.Put_일목.SetFieldData("ChartIndexInBlock", "market", 0, "5") # 시장구분
        A.Put_일목.SetFieldData("ChartIndexInBlock", "period", 0, "1") # 주기 구분 # 분:1 / 일:2
        A.Put_일목.SetFieldData("ChartIndexInBlock", "shcode", 0, pCode) # 종목코드
        A.Put_일목.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500") # 요청 건수 (최대 500개) 1일=39개
        A.Put_일목.SetFieldData("ChartIndexInBlock", "ncnt", 0, A.n분) # 단위 n 틱/분 만 해당
        A.Put_일목.SetFieldData("ChartIndexInBlock", "sdate", 0, "") # 시작 일자
        A.Put_일목.SetFieldData("ChartIndexInBlock", "edate", 0, "") # 종료 일자
        A.Put_일목.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1") # 수정주가반영여부
        A.Put_일목.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0") # 갭보정 여부
        A.Put_일목.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1") # 실시간자동등록 여부
        A.Put_일목.RequestService("ChartIndex", 0)


    def Call_이평선요청(self):
        A.Call_이평.SetFieldData("ChartIndexInBlock", "indexid", 0, "") # 지표ID
        A.Call_이평.SetFieldData("ChartIndexInBlock", "indexname", 0, "가격 이동평균") # 지표명
        A.Call_이평.SetFieldData("ChartIndexInBlock", "indexparam", 0, "") # 지표조건설정
        A.Call_이평.SetFieldData("ChartIndexInBlock", "market", 0, "5") # 시장구분
        A.Call_이평.SetFieldData("ChartIndexInBlock", "period", 0, "1") # 주기 구분 # 분:1 / 일:2
        A.Call_이평.SetFieldData("ChartIndexInBlock", "shcode", 0, cCode) # 종목코드
        A.Call_이평.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500") # 요청 건수 (최대 500개) 1일=39개
        A.Call_이평.SetFieldData("ChartIndexInBlock", "ncnt", 0, A.n분) # 단위 n 틱/분 만 해당
        A.Call_이평.SetFieldData("ChartIndexInBlock", "sdate", 0, "") # 시작 일자
        A.Call_이평.SetFieldData("ChartIndexInBlock", "edate", 0, "") # 종료 일자
        A.Call_이평.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1") # 수정주가반영여부
        A.Call_이평.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0") # 갭보정 여부
        A.Call_이평.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1") # 실시간자동등록 여부
        A.Call_이평.RequestService("ChartIndex", 0)
        

    def Put_이평선요청(self):
        time.sleep(1.1)
        A.Put_이평.SetFieldData("ChartIndexInBlock", "indexid", 0, "") # 지표ID
        A.Put_이평.SetFieldData("ChartIndexInBlock", "indexname", 0, "가격 이동평균") # 지표명
        A.Put_이평.SetFieldData("ChartIndexInBlock", "indexparam", 0, "") # 지표조건설정
        A.Put_이평.SetFieldData("ChartIndexInBlock", "market", 0, "5") # 시장구분
        A.Put_이평.SetFieldData("ChartIndexInBlock", "period", 0, "1") # 주기 구분 # 분:1 / 일:2
        A.Put_이평.SetFieldData("ChartIndexInBlock", "shcode", 0, pCode) # 종목코드
        A.Put_이평.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500") # 요청 건수 (최대 500개) 1일=39개
        A.Put_이평.SetFieldData("ChartIndexInBlock", "ncnt", 0, A.n분) # 단위 n 틱/분 만 해당
        A.Put_이평.SetFieldData("ChartIndexInBlock", "sdate", 0, "") # 시작 일자
        A.Put_이평.SetFieldData("ChartIndexInBlock", "edate", 0, "") # 종료 일자
        A.Put_이평.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1") # 수정주가반영여부
        A.Put_이평.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0") # 갭보정 여부
        A.Put_이평.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1") # 실시간자동등록 여부
        A.Put_이평.RequestService("ChartIndex", 0)


    def realdata_slot(self, oCode, sRealType):
        

        if sRealType == "장시작시간":

            self.value = self.dynamicCall("GetCommRealData(QString, int)", oCode, 215)
            
            if self.value == '0':
                print("장 시작 전")

            elif self.value == '2':
                print("장종료전(3:20 ~ 3:30)")
                    
            elif self.value == '3':
                print("장 시작")

            elif self.value == '4':
                print("3시30분 장 종료")
                sys.exit()


        elif sRealType == "선물시세":

            fclose = self.dynamicCall("GetCommRealData(QString, int)", oCode, 10) # 현재가
            fclose = abs(float(fclose))

            fopen = self.dynamicCall("GetCommRealData(QString, int)", oCode, 16) # 시가
            fopen = abs(float(fopen))

            fhigh = self.dynamicCall("GetCommRealData(QString, int)", oCode, 17) # 고가
            fhigh = abs(float(fhigh))

            flow = self.dynamicCall("GetCommRealData(QString, int)", oCode, 18) # 저가
            flow = abs(float(flow))


        elif sRealType == "옵션시세":

            a = self.dynamicCall("GetCommRealData(QString, int)", oCode, 10) # 현재가
            a = abs(float(a))

            if oCode == cCode:

                # 콜 매수
                if self.매수 == False and (Call_일목균형표.CB_terms == True) and (Call_일목균형표.C26d == 1) and (cCode and pCode) not in self.jango_dict.keys():
                    self.매수 = True
                    Call_일목균형표.CB_terms = False
                    print("Call 매수 주문 시작 %s %s" % (Call_일목균형표.CB_terms,Call_일목균형표.C26d))
                    order_success = KXing.OrderFO(self,ScreenNo="2000",Accno=self.accno,oCode=cCode,매매구분='2',quantity=self.qty)
                    if order_success == (0 or None):
                        print("Call 매수주문 성공")
                    else:
                        print("Call 매수주문 실패")
                    

                # 콜 매도
                if cCode in self.jango_dict.keys():
                    jd = self.jango_dict[cCode]
                    매입가 = jd['매입단가']
                    수익률 = ((a - 매입가) / 매입가) * 100
                    수익률 = float(수익률)
                    가능수 = jd['주문가능수량']
                    구분 = jd['매매구분']

                    if 가능수 == self.qty and 구분 == "2" and ((수익률 <= -10) or (수익률 >= 30)):
                        Call_일목균형표.CB_terms = False
                        print("Call 매도 주문 시작 / CB_terms:%s" % Call_일목균형표.CB_terms)
                        order_success = KXing.OrderFO(self,ScreenNo="2000",Accno=self.accno,oCode=cCode,매매구분='1',quantity=가능수)
                        if order_success == (0 or None):
                            print("Call 수익률:%s, I.C26d:%s, CB_terms:%s 매도주문 성공" % (수익률,Call_일목균형표.C26d,Call_일목균형표.CB_terms))
                            self.매수 = False
                            if cCode in self.jango_dict:
                                del self.jango_dict[cCode]
                        else:
                            print("Call 매도주문 실패")

            
            if oCode == pCode:
                # 풋 매수
                if self.매수 == False and (Put_일목균형표.PB_terms == True) and (Put_일목균형표.P26d == 1) and ((cCode and pCode) not in self.jango_dict.keys()):
                    self.매수 = True
                    Put_일목균형표.PB_terms = False
                    print("Put 매수 주문 시작 / PB_terms: %s %s" % (Put_일목균형표.PB_terms,Put_일목균형표.P26d))
                    order_success = KXing.OrderFO(self,ScreenNo="3000",Accno=self.accno,oCode=pCode,매매구분='2',quantity=self.qty)
                    if order_success == (0 or None):
                        print("Put 매수주문 성공")
                    else:
                        print("Put 매수주문 실패")
                   
                # 풋 매도
                elif pCode in self.jango_dict.keys():
                    jd = self.jango_dict[pCode]
                    풋매입가 = jd['매입단가']
                    풋수익률 = ((a - 풋매입가) / 풋매입가) * 100
                    풋수익률 = float(풋수익률)
                    풋가능수 = jd['주문가능수량']
                    풋매매구분 = jd['매매구분']

                    if 풋가능수 == self.qty and 풋매매구분 == "2" and ((풋수익률 <= -10) or (풋수익률 >= 30)):
                        Put_일목균형표.PB_terms = False
                        print("Put 매도 주문 시작 %s" % Put_일목균형표.PB_terms)
                        order_success = KXing.OrderFO(self,ScreenNo="3000",Accno=self.accno,oCode=pCode,매매구분='1',quantity=풋가능수)
                        if order_success == (0 or None):
                            print("Put수익률:%s I.P26d:%s 매도주문 성공, PB_terms: %s" % (풋수익률,Put_일목균형표.P26d,Put_일목균형표.PB_terms))
                            self.매수 = False
                            if pCode in self.jango_dict:
                                del self.jango_dict[pCode]
                        else:
                            print("Put 매도주문 실패")
                        

    @staticmethod
    def OrderFO(self,ScreenNo=None,Accno=None,oCode=None,매매구분=None,quantity=None): # 1:매도, 2:매수
        self.dynamicCall("SendOrderFO(QString,QString,QString,QString,int,QString,QString,int,QString,QString)",["신규매수", ScreenNo, Accno, oCode, '1', 매매구분 , '3', quantity, "0", ""])


    def chejan_slot(self, sGubun):

        if int(sGubun) == 4: # 파생잔고 / 접수와 체결시 '0'값, 잔고변경은 '1'값

            oCode = self.dynamicCall("GetChejanData(int)", 9001) # 종목코드

            quantity = self.dynamicCall("GetChejanData(int)", 930) # 보유수량
            quantity = int(quantity)

            like_quan = self.dynamicCall("GetChejanData(int)", 933) # 주문가능수량
            like_quan = int(like_quan)

            buy_price = self.dynamicCall("GetChejanData(int)", 931) # 매입단가
            buy_price = abs(float(buy_price))

            meme_gubun = self.dynamicCall("GetChejanData(int)", 946) # 매매구분
            print("oCode:%s,보유수량:%s, 주문가능수량:%s,매입단가:%s" % (oCode,quantity,like_quan,buy_price))
            if oCode not in self.jango_dict.keys():
                self.jango_dict.update({oCode:{}})

            jd = self.jango_dict[oCode]
            jd.update({"종목코드": oCode})
            jd.update({"보유수량": quantity})
            jd.update({"주문가능수량": like_quan})
            jd.update({"매입단가": buy_price})
            jd.update({"매매구분": meme_gubun})

            if quantity == 0:
                del self.jango_dict[oCode]

    def msg_slot(self, sScrNo, sRQName, sTrCode, msg):
        print("Screen Number: %s, Request: %s, TrCode: %s --- %s" %(sScrNo, sRQName, sTrCode, msg))