from os import *
import sys,time,pythoncom,threading,requests
import win32com.client as win32com
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from config.Info import *
from config.slack import *
from config.errorCode import *
from config.Option_Code import *
from playsound import playsound


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
    Call_일목 = None
    def OnReceiveChartRealData(self, trCode):
        현재가 = self.GetFieldChartRealData("ChartIndexOutBlock1", "close") # 현재가(종가)
        현재가 = float(현재가)

        기준선 = self.GetFieldChartRealData("ChartIndexOutBlock1", "value2") # 기준선
        기준선 = float(기준선)
        print(기준선)

        if 기준선 == 0:
            pass
        else:
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
    Put_일목 = None
    def OnReceiveChartRealData(self, trCode):
        
        현재가 = self.GetFieldChartRealData("ChartIndexOutBlock1", "close") # 현재가(종가)
        현재가 = float(현재가)

        기준선 = self.GetFieldChartRealData("ChartIndexOutBlock1", "value2") # 기준선
        기준선 = float(기준선)

        if 기준선 == 0:
            pass
        else:
            if 현재가 > 기준선 > 0:
                Put_일목균형표.P26d = 1
            elif 현재가 < 기준선 and 기준선 > 0:
                Put_일목균형표.P26d = -1
                Put_일목균형표.PB_terms = True
            else:
                Put_일목균형표.P26d = 0


class KXing(QAxWidget):
    
    def __init__(self):
        super().__init__()

        self.매수 = True
        self.qty = 1 # 주문 수량
        self.n분 = "30" # n분봉차트
        
        self.login_event_loop = QEventLoop()

        self.not_account_option_dict = {}
        self.jango_dict = {}
        
        self.get_ocx_instance()

        self.event_slots()
        self.real_event_slot()
        self.signal_login_commConnect()
        self.get_account_info()

        self.dynamicCall("SetRealReg(QString, QString, QString, QString)", "5000", '', 215, "0")
        for code in (cCode,pCode):
            self.dynamicCall("SetRealReg(QString, QString, QString, QString)", "6000", code, 20, "1")

        Xing = win32com.DispatchWithEvents("XA_Session.XASession", HTS)

        Call_일목균형표.Call_일목 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", Call_일목균형표)
        Call_일목균형표.Call_일목.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"

        Put_일목균형표.Put_일목 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", Put_일목균형표)
        Put_일목균형표.Put_일목.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"


        # HTS 로그인
        Xing.ConnectServer("hts.ebestsec.co.kr", 20001)
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
        while True:
            pythoncom.PumpWaitingMessages()


    @staticmethod
    def Msg(text=None):
        Slack.post_message(slack,"#message",text)


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
        self.accno = accno
        user_name = self.dynamicCall("GetLoginInfo(QString)", "USER_NAME")
        print("%s님의 계좌번호: %s" %(user_name,self.accno))
        KXing.Msg(text="%s님의 계좌번호: %s" %(user_name,계좌번호))


    def Call_일목균형표요청(self):
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "indexid", 0, "") # 지표ID
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "indexname", 0, "일목균형표") # 지표명
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "indexparam", 0, "") # 지표조건설정
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "market", 0, "5") # 시장구분
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "period", 0, "1") # 주기 구분 # 분:1 / 일:2
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "shcode", 0, cCode) # 종목코드
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500") # 요청 건수 (최대 500개) 1일=39개
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "ncnt", 0, self.n분) # 단위 n 틱/분 만 해당
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "sdate", 0, "") # 시작 일자
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "edate", 0, "") # 종료 일자
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1") # 수정주가반영여부
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0") # 갭보정 여부
        Call_일목균형표.Call_일목.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1") # 실시간자동등록 여부
        err = Call_일목균형표.Call_일목.RequestService("ChartIndex", 0)
        print(err)


    def Put_일목균형표요청(self):
        time.sleep(1.1)
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "indexid", 0, "") # 지표ID
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "indexname", 0, "일목균형표") # 지표명
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "indexparam", 0, "") # 지표조건설정
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "market", 0, "5") # 시장구분
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "period", 0, "1") # 주기 구분 # 분:1 / 일:2
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "shcode", 0, pCode) # 종목코드
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500") # 요청 건수 (최대 500개) 1일=39개
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "ncnt", 0, self.n분) # 단위 n 틱/분 만 해당
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "sdate", 0, "") # 시작 일자
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "edate", 0, "") # 종료 일자
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1") # 수정주가반영여부
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0") # 갭보정 여부
        Put_일목균형표.Put_일목.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1") # 실시간자동등록 여부
        err = Put_일목균형표.Put_일목.RequestService("ChartIndex", 0)
        print(err)


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


        elif sRealType == "옵션시세":

            a = self.dynamicCall("GetCommRealData(QString, int)", oCode, 10) # 현재가
            a = abs(float(a))

            b = self.dynamicCall("GetCommRealData(QString, int)", oCode, 27) # (최우선)매도호가
            b = abs(float(b))

            c = self.dynamicCall("GetCommRealData(QString, int)", oCode, 28) # (최우선)매수호가
            c = abs(float(b))

            if oCode == cCode:
                # 콜 매수
                if self.매수 == False and (Call_일목균형표.CB_terms == True) and (Call_일목균형표.C26d == 1) and (cCode and pCode) not in self.jango_dict.keys():
                    self.매수 = True
                    Call_일목균형표.CB_terms = False
                    print("Call 매수 주문 시작")
                    order_success = KXing.OrderFO(self,RQName="매수",oCode=cCode,주문종류="1",매매구분='2',거래구분='1',Price=c,OrgOrdNo="")
                    if order_success == 0:
                        print("Call 매수주문 성공")
                    else:
                        print("Call 매수주문 실패")
                

                # 콜 매도
                if cCode in self.jango_dict.keys():
                    jd = self.jango_dict[cCode]
                    매입가 = jd['매입단가']
                    수익률 = ((a - 매입가) / 매입가) * 100
                    수익률 = float(수익률)
                    구분 = jd['매매구분']
                    KXing.Msg(text="Call 수익률: %s" % 수익률)

                    if 구분 == "2" and ((수익률 <= -5) or (수익률 >= 25)):
                        Call_일목균형표.CB_terms = False
                        print("Call 매도 주문 시작")
                        order_success = KXing.OrderFO(self,RQName="매도",oCode=cCode,주문종류='1',매매구분='1',거래구분='3',Price="0",OrgOrdNo="")
                        if order_success == 0:
                            print("Call 매도주문 성공 / 수익률:%s" % 수익률)
                            self.매수 = False
                            if cCode in self.jango_dict:
                                del self.jango_dict[cCode]
                        else:
                            print("Call 매도주문 실패")

                else:
                    not_meme_list = list(self.not_account_option_dict)
                    for order_num in not_meme_list:
                        mCode = self.not_account_option_dict[order_num]["종목코드"]
                        mQuan = self.not_account_option_dict[order_num]["미체결수량"]
                        mOnum = self.not_account_option_dict[order_num]["원주문번호"]
                        mOrnum = self.not_account_option_dict[order_num]["주문번호"]
                        mOrder_Pri = self.not_account_option_dict[order_num]["주문가격"]
                        mguboon = self.not_account_option_dict[order_num]["주문구분"]
                        if mCode == cCode and int(mQuan) > 0 and float(mOrder_Pri) < b:
                            print("Call 매수 정정 주문 시작")
                            order_success = KXing.OrderFO(self,RQName="정정",oCode=cCode,주문종류='2',매매구분='2',거래구분='1',Price=c, OrgOrdNo=mOnum)
                            if order_success == 0:
                                print("Call 매수 정정 주문 성공")
                            else:
                                print("Call 매수 정정 주문 실패")

            
            if oCode == pCode:
                # 풋 매수
                if self.매수 == False and (Put_일목균형표.PB_terms == True) and (Put_일목균형표.P26d == 1) and ((cCode and pCode) not in self.jango_dict.keys()):
                    self.매수 = True
                    Put_일목균형표.PB_terms = False
                    print("Put 매수 주문 시작")
                    order_success = KXing.OrderFO(self,RQName="매수",oCode=pCode,주문종류='1',매매구분='2',거래구분='1',Price= c, OrgOrdNo="")
                    if order_success == 0:
                        print("Put 매수주문 성공")
                    else:
                        print("Put 매수주문 실패")

                # 풋 매도
                elif pCode in self.jango_dict.keys():
                    jd = self.jango_dict[pCode]
                    풋매입가 = jd['매입단가']
                    풋수익률 = ((a - 풋매입가) / 풋매입가) * 100
                    풋수익률 = float(풋수익률)
                    풋매매구분 = jd['매매구분']
                    print("Put 수익률: %s" % 풋수익률)
                    KXing.Msg(text="Put 수익률: %s" % 풋수익률)

                    if 풋매매구분 == "2" and ((풋수익률 <= -5) or (풋수익률 >= 25)):
                        Put_일목균형표.PB_terms = False
                        print("Put 매도 주문 시작 %s" % Put_일목균형표.PB_terms)
                        order_success = KXing.OrderFO(self,RQName="매도",oCode=pCode,주문종류='1',매매구분='1',거래구분='3',Price="0",OrgOrdNo="")
                        if order_success == 0:
                            print("Put 매도 주문 성공 / 수익률:%s" % 풋수익률)
                            self.매수 = False
                            if pCode in self.jango_dict:
                                del self.jango_dict[pCode]
                        else:
                            print("Put 매도주문 실패")
                        
                not_meme_list = list(self.not_account_option_dict)
                for order_num in not_meme_list:
                    mCode = self.not_account_option_dict[order_num]["종목코드"]
                    mQuan = self.not_account_option_dict[order_num]["미체결수량"]
                    mQuan = int(mQuan)
                    mOnum = self.not_account_option_dict[order_num]["원주문번호"]
                    mOrnum = self.not_account_option_dict[order_num]["주문번호"]
                    mOrder_Pri = self.not_account_option_dict[order_num]["주문가격"]
                    mguboon = self.not_account_option_dict[order_num]["주문구분"]
                    if mCode == pCode and mQuan > 0 and mOrder_Pri < b:
                        print("Put 매수 정정 주문 시작")
                        order_success = KXing.OrderFO(self,RQName="정정",oCode=pCode,주문종류='2',매매구분='2',거래구분='1',Price=c, OrgOrdNo=mOnum)
                        if order_success == (0 or None):
                            print("Put 매수 정정 주문 성공")
                        else:
                            print("Put 매수 정정 주문 실패")


    @staticmethod
    def OrderFO(self,RQName=None,oCode=None,주문종류=None,매매구분=None,거래구분=None,Price=None,OrgOrdNo=None):
        self.dynamicCall("SendOrderFO(QString,QString,QString,QString,int,QString,QString,int,QString,QString)",[RQName, "2000", 계좌번호, oCode, 주문종류, 매매구분 , 거래구분, '1', Price, OrgOrdNo])
        '''
        SendOrderFO(
            BSTR sRQName,     // 사용자 구분명
            BSTR sScreenNo,   // 화면번호
            BSTR sAccNo,      // 계좌번호 10자리
            BSTR sCode,       // 종목코드
            LONG lOrdKind,    // 주문종류 1:신규매매, 2:정정, 3:취소
            BSTR sSlbyTp,     // 매매구분 1: 매도, 2:매수
            BSTR sOrdTp,      // 거래구분(혹은 호가구분)은 아래 참고
            LONG lQty,        // 주문수량
            BSTR sPrice,      // 주문가격
            BSTR sOrgOrdNo    // 원주문번호
            
            [거래구분]
            1 : 지정가
            2 : 조건부지정가 = 정규시장(09:30 ~ 15:20)까지는 지정가 주문,장 종료때는 시장가 주문
            3 : 시장가
            4 : 최유리지정가
            5 : 지정가(IOC)
            6 : 지정가(FOK)
            7 : 시장가(IOC)
            8 : 시장가(FOK)
            9 : 최유리지정가(IOC)
            A : 최유리지정가(FOK)
            장종료 후 시간외 주문은 지정가 선택
        '''


    def chejan_slot(self, Gubun):

        if int(Gubun) == 0: # 접수 & 체결 
            oCode = self.dynamicCall("GetChejanData(int)", 9001) # 종목코드

            un_quan = self.dynamicCall("GetChejanData(int)", 902) # 미체결수량

            one_order_number = self.dynamicCall("GetChejanData(int)", 904) # 원주문번호

            jumoon_gubun = self.dynamicCall("GetChejanData(int)", 905) # 주문구분
            jumoon_gubun = jumoon_gubun.strip().lstrip('+').lstrip('-')

            order_number = self.dynamicCall("GetChejanData(int)", 9203) # 주문번호

            order_price = self.dynamicCall("GetChejanData(int)", 901) # 주문가격


            print("종목코드:%s, 주문구분:%s 미체결수량:%s,원주문번호:%s, 주문번호:%s" % (oCode,jumoon_gubun,un_quan,one_order_number,order_number))
            KXing.Msg(text="종목코드:%s, 주문구분:%s 미체결수량:%s,원주문번호:%s, 주문번호:%s" % (oCode,jumoon_gubun,un_quan,one_order_number,order_number))

            if order_number not in self.not_account_option_dict.keys():
                self.not_account_option_dict.update({order_number:{}})

            nod = self.not_account_option_dict[order_number]
            nod.update({"종목코드":oCode})
            nod.update({"미체결수량":un_quan})
            nod.update({"주문구분":jumoon_gubun})
            nod.update({"주문번호":order_number})
            nod.update({"주문가격":order_price})
            nod.update({"원주문번호":one_order_number})


        elif int(Gubun) == 4: # 파생잔고 / 잔고변경은 '1'값

            oCode = self.dynamicCall("GetChejanData(int)", 9001) # 종목코드

            quantity = self.dynamicCall("GetChejanData(int)", 930) # 보유수량
            quantity = int(quantity)

            like_quan = self.dynamicCall("GetChejanData(int)", 933) # 주문가능수량
            like_quan = int(like_quan)

            buy_price = self.dynamicCall("GetChejanData(int)", 931) # 매입단가
            buy_price = abs(float(buy_price))

            meme_gubun = self.dynamicCall("GetChejanData(int)", 946) # 매매구분

            print("oCode:%s,보유수량:%s, 주문가능수량:%s,매입단가:%s" % (oCode,quantity,like_quan,buy_price))
            KXing.Msg(text="oCode:%s,보유수량:%s, 주문가능수량:%s,매입단가:%s" % (oCode,quantity,like_quan,buy_price))

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
        KXing.Msg(text="Screen Number: %s, Request: %s, TrCode: %s --- %s" %(sScrNo, sRQName, sTrCode, msg))