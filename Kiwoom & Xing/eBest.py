import pythoncom,threading,time
import win32com.client as win32com
from Info import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from errorCode import *

class XASession:
    login_state = 0
    def OnLogin(self, szCode, szMsg):
        if szCode == "0000":
            XASession.login_state = 1
        else:
            print("[X] Login failed !!! {%s: %s}\n" % (szCode,szMsg))


class HTS:
    login_state = 0
    def OnLogin(self, szCode, szMsg):
        if szCode == "0000":
            HTS.login_state = 1
        else:
            print("[X] HTS Login failed !!! {%s: %s}\n" % (szCode,szMsg))


class MyBalance:
    매수 = False
    test = False
    t0441_ok = False
    chooose = 0

    def OnReceiveData(self, trCode):
        cnt0441 = self.GetBlockCount("t0441OutBlock1")
        cnt0441 = int(cnt0441)
        
        if MyBalance.test == True:
            Main.order_option(Code=Main.oCode['cCode'],BnsTpCode="2")
            MyBalance.test = False
        else:
            if self.매수 == False:
                if int(cnt0441) == 0:
                    
                    if (MyBalance.chooose != 2) and (Chart1.CB_terms == 1) and (Chart1.C26d == 1) and (Hoka.호가C매수 == 1):
                        self.매수 = True
                        Chart1.CB_terms = 0
                        Hoka.호가C매수 = 0
                        print("Call 매수 시작")
                        Main.order_option(Code=Main.oCode['cCode'],BnsTpCode="2")
                    if (MyBalance.chooose != 1) and (Chart2.PB_terms == 1) and (Chart2.P26d == 1) and (Hoka.호가P매수 == 1):
                        self.매수 = True
                        Chart2.PB_terms = 0
                        Hoka.호가P매수 = 0
                        print("Put 매수 시작")
                        Main.order_option(Code=Main.oCode['pCode'],BnsTpCode="2")

                elif cnt0441 != 0:
                    self.매수 = True
                    Main.request_balance()
                
            else:
                for i in range(cnt0441):
                    expcode = self.GetFieldData("t0441OutBlock1", "expcode", i) # 종목번호
                    sunikrt = self.GetFieldData("t0441OutBlock1", "sunikrt", i) # 수익률
                    sunikrt = float(sunikrt)
                    print("[%s] 수익률:%s"%(expcode,sunikrt)+"%")
                    CP = expcode[0:1]
                    if self.매수 == True:
                        if ((sunikrt <= -6) or (sunikrt >= 30)):# 수익률에 의한 매도 및 손절
                            if CP == "2": # Call 매도
                                self.매수 = False
                                Chart1.CB_terms = 0
                                print("[%s] Call 수익률: %s 매도 주문 시작" % (expcode,sunikrt))
                                Main.order_option(Code=expcode,BnsTpCode="1")
        
                            elif CP == "3": # Put 매도
                                self.매수 = False
                                Chart2.PB_terms = 0
                                print("[%s] Put 수익률: %s 매도 주문 시작" % (expcode,sunikrt))
                                Main.order_option(Code=expcode,BnsTpCode="1")


                        # 시가 고가에 의한 손절(매도)
                        if T2301.disaprng1 == 1 and T2301.sigo2 == 0 and T2301.sigo1 > 0 and CP == "2": # Call 매도
                            self.매수 = False
                            Chart1.CB_terms = 0
                            print("[%s] Put 가격 변동 확인됨 --- Call 손절 주문 수익률: %s" % (expcode,sunikrt)+"%")
                            Main.order_option(Code=expcode,BnsTpCode="1")
                    
                        elif (T2301.disaprng2 == 1) and (T2301.sigo1 == 0) and (T2301.sigo2 > 0) and (CP == "3"): # Put 매도
                            self.매수 = False
                            Chart2.PB_terms = 0
                            print("[%s] Call 가격 변동 확인됨 --- Put 손절 주문 수익률: %s" % (expcode,sunikrt)+"%")
                            Main.order_option(Code=expcode,BnsTpCode="1")
                        threading.Timer(2,Main.request_balance).start()


class T2301: # 옵션 전광판
    cnt_dict = {}
    price1_dict = {}
    price2_dict = {}
    price1_list = []
    price2_list = []


    t2301 = None
    cnt1 = 0
    cnt2 = 0
    sigo1 = 0
    sigo2 = 0
    choose = 0 # C이면 1 P이면 2
    disaprng1 = 0
    disaprng2 = 0

    def OnReceiveData(self,trCode):

        cnt2301 = self.GetBlockCount("t2301OutBlock1")

        for i in range(cnt2301):
            optcode1 = self.GetFieldData("t2301OutBlock1", "optcode", i) # Call 행사가
            optcode2 = self.GetFieldData("t2301OutBlock2", "optcode", i) # Put 행사가

            open1 = self.GetFieldData("t2301OutBlock1", "open", i) # 시가
            open1 = float(open1)

            high1 = self.GetFieldData("t2301OutBlock1", "high", i) # 고가
            high1 = float(high1)

            price1 = self.GetFieldData("t2301OutBlock1", "price", i) # 현재가(종가)
            price1 = float(price1)

            open2 = self.GetFieldData("t2301OutBlock2", "open", i) # 시가
            open2 = float(open2)

            high2 = self.GetFieldData("t2301OutBlock2", "high", i) # 고가
            high2 = float(high2)

            price2 = self.GetFieldData("t2301OutBlock2", "price", i) # 현재가(종가)
            price2 = float(price2)


            if (int(cnt2301)-1) != i:
                # 시가-고가 받아오는 부분
                if (sigo_max > (open1 and high1) > sigo_min) and (open1 == high1):
                    T2301.cnt1 += 1
                    T2301.disaprng1 = 1
                    T2301.sigo1 = T2301.cnt1
                    
                elif (sigo_max > (open2 and high2) > sigo_min) and (open2 == high2):
                    T2301.cnt2 += 1
                    T2301.disaprng2 = 1
                    T2301.sigo2 = T2301.cnt2

                if (bas_max > int(price1) > bas_min):
                    T2301.price1_dict[optcode1] = price1
                    T2301.price1_list = list(T2301.price1_dict.keys())

                elif (bas_max > int(price2) > bas_min):
                    T2301.price2_dict[optcode2] = price2
                    T2301.price2_list = list(T2301.price2_dict.keys())

            else: # 종목코드 받아오는 부분
                cCode = T2301.price1_list[0]
                pCode = T2301.price2_list[-1]
                
                if Main.oCode == {}:
                    Main.oCode = {'cCode':cCode,'pCode':pCode}
                    Main.request_Chart1(Code=Main.oCode['cCode'])
                    time.sleep(2)
                    Main.request_Chart2(Code=Main.oCode['pCode'])
                
                if (cCode or pCode) not in Main.oCode.values():
                    Main.oCode.update({'cCode':cCode,'pCode':pCode})
                    Main.request_Chart1(Code=Main.oCode['cCode'])
                    time.sleep(2)
                    Main.request_Chart2(Code=Main.oCode['pCode'])
                    
                
                if T2301.cnt_dict == {}:# 시가-고가 확인하는 부분
                    T2301.sigo1 = T2301.cnt1
                    T2301.sigo2 = T2301.cnt2
                    T2301.cnt_dict = {"CK":T2301.sigo1,"PK":T2301.sigo2}
                else:
                    T2301.cnt_dict.update({"CK":T2301.sigo1,"PK":T2301.sigo2})

                    if (T2301.sigo1) < (T2301.sigo2):
                        T2301.choose = 1
                        MyBalance.chooose = 1
                    elif (T2301.sigo1) > (T2301.sigo2):
                        T2301.choose = 2
                        MyBalance.chooose = 2
                    else:
                        T2301.choose = 0
                T2301.cnt1 = 0
                T2301.cnt2 = 0

                threading.Timer(2,Main.request_option_table,args=[when]).start()
                print("%s[%s] %s %s --- %s %s (%s %s)" % (MyBalance.매수,
                    MyBalance.chooose,Chart1.CB_terms,Chart1.C26d,Chart2.PB_terms,Chart2.P26d,Hoka.호가C매수,Hoka.호가P매수))
                if MyBalance.chooose != 2 and Chart1.CB_terms == 1 and Chart1.C26d == 1:
                    Main.request_balance()

                if MyBalance.chooose != 1 and Chart2.PB_terms == 1 and Chart2.P26d == 1:
                    Main.request_balance()                   


class Hoka: # 호가 잔량 요청
    t = None
    vol = 0
    호가C매수 = 0
    호가P매수 = 0

    def OnReceiveData(self, trCode):
        dvol = self.GetFieldData("t2105OutBlock", "dvol", 0) # 매도 호가 총 잔량
        svol = self.GetFieldData("t2105OutBlock", "svol", 0) # 매수 호가 총 잔량
        Hoka.vol = int(svol) - int(dvol)
        print(Hoka.vol)
        if (Hoka.호가C매수 == 0) and (Hoka.vol > 2000):
            Hoka.호가C매수 = 1
            Hoka.호가P매수 = 0
            Main.request_balance()
            
        if (Hoka.호가P매수 == 0) and (Hoka.vol < -2000):
            Hoka.호가P매수 = 1
            Hoka.호가C매수 = 0
            Main.request_balance()
        threading.Timer(2,Main.request_hoka).start()


class Chart1:
    C26d = 0
    CB_terms = 0
    Call_일목 = None

    def OnReceiveChartRealData(self, trCode):
        현재가 = self.GetFieldChartRealData("ChartIndexOutBlock1", "close") # 현재가(종가)
        현재가 = float(현재가)

        기준선 = self.GetFieldChartRealData("ChartIndexOutBlock1", "value2") # 기준선
        기준선 = float(기준선)
        
        if 기준선 != 0:
            if 현재가 > 기준선:
                Chart1.C26d = 1
            elif 현재가 < 기준선:
                Chart1.C26d = 0
                Chart1.CB_terms = 1


class Chart2:
    P26d = 0
    Put_일목 = None
    PB_terms = 0
    
    def OnReceiveChartRealData(self, trCode):
        현재가 = self.GetFieldChartRealData("ChartIndexOutBlock1", "close") # 현재가(종가)
        현재가 = float(현재가)

        기준선 = self.GetFieldChartRealData("ChartIndexOutBlock1", "value2") # 기준선
        기준선 = float(기준선)

        if 기준선 != 0:
            if 현재가 > 기준선:
                Chart2.P26d = 1
            elif 현재가 < 기준선:
                Chart2.P26d = 0
                Chart2.PB_terms = 1
                

# class CFOAT010: # 주문
#     def OnReceiveData(self, trCode):
#         FnoIsuNo = self.GetFieldData("CFOAT00100OutBlock1", "FnoIsuNo", 0) # 종목번호
#         OrdQty = self.GetFieldData("CFOAT00100OutBlock1", "OrdQty", 0) # 주문수량
#         OrdNo = self.GetFieldData("CFOAT00100OutBlock2", "OrdNo", 0) # 주문번호
#         print("주문 체결: 종목번호:%s, 주문수량:%s, 주문번호:%s" % (FnoIsuNo,OrdQty,OrdNo))


class Main(QAxWidget):
    check = 0
    tt = None
    oo = None
    cCode = ""
    pCode = ""
    oCode = {}
    Number = ""

    def __init__(self):
        self.app = QApplication(sys.argv)
        
        super().__init__()
        
        self.login_event_loop = QEventLoop()
        
        self.get_ocx_instance()
        self.event_slots()
        
        self.request_login_kiwoom()
        self.request_logininfo()

        Xing_hts = win32com.DispatchWithEvents("XA_Session.XASession", HTS)
        # Xing = win32com.DispatchWithEvents("XA_Session.XASession", XASession)
        
        Main.tt = win32com.DispatchWithEvents("XA_DataSet.XAQuery", MyBalance)
        Main.tt.ResFileName = "C:/eBEST/xingAPI/Res/t0441.res"

        Hoka.t = win32com.DispatchWithEvents("XA_DataSet.XAQuery", Hoka)
        Hoka.t.ResFileName = "C:/eBEST/xingAPI/Res/t2105.res"
        
        T2301.t2301 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", T2301)
        T2301.t2301.ResFileName = "C:/eBEST/xingAPI/Res/t2301.res"

        Chart1.Call_일목 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", Chart1)
        Chart1.Call_일목.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"

        Chart2.Put_일목 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", Chart2)
        Chart2.Put_일목.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"

        # CFOAT010.order = win32com.DispatchWithEvents("XA_DataSet.XAQuery", CFOAT010)
        # CFOAT010.order.ResFileName = "C:/eBEST/xingAPI/Res/CFOAT00100.res"
        
        Xing_hts.ConnectServer("hts.ebestsec.co.kr", 20001)

        if Xing_hts.Login(ID, hts_pw, Cert_pw, 0, True) is True:
            pass
        else:
            nErrCode = Xing_hts.GetLastError()
            strErrMsg = Xing_hts.GetErrorMessage(nErrCode)
            print("\n[X] HTS Server Connection Failed !!! {%s: %s}" % (nErrCode, strErrMsg))
        while HTS.login_state == 0:
            pythoncom.PumpWaitingMessages()

        self.app.exec_()
        
        # Xing.ConnectServer("demo.ebestsec.co.kr", 20001)
        # if Xing.Login(ID, demo_pw, Cert_pw, 0, True) is True:
        #     pass
        # else:
        #     nErrCode = Xing.GetLastError()
        #     strErrMsg = Xing.GetErrorMessage(nErrCode)
        #     print("[X] Server Connection Failed !!! {%s: %s}" % (nErrCode, strErrMsg))
        # while XASession.login_state == 0:
        #     pythoncom.PumpWaitingMessages()

        # for i in range(1):
        #     Number = Xing.GetAccountList(i)
        #     Main.Number = Number
        #     Name = Xing.GetAccountName(Number)
        #     Detail = Xing.GetAcctDetailName(Number)
        #     print("\n%s님의 %s 계좌번호: %s\n" % (Name, Detail, Number))

        # Main.request_option_table(yyyymm=when)
        # Main.request_balance()
        # Main.request_hoka()
        # while True:
        #     pythoncom.PumpWaitingMessages()


    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        
    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)
        
    def request_login_kiwoom(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop.exec_()
        
    def login_slot(self,err_code):
        print(errors(err_code)[1])
        self.login_event_loop.exit()
        
    def request_logininfo(self):
        a = self.dynamicCall("GetLoginInfo(QString)","ACCOUNT_CNT") # 보유 개좌 수
        b = self.dynamicCall("GetLoginInfo(QString)","ACCLIST") # or "ACCNO" / 계좌번호
        b = b[:-1]
        c = self.dynamicCall("GetLoginInfo(QString)","USER_ID") # ID
        e = self.dynamicCall("GetLoginInfo(QString)","USER_NAME") # 사용자 이름
        f = self.dynamicCall("GetLoginInfo(QString)","GetServerGubun") # 1:모의 else: 실거래
        g = self.dynamicCall("GetLoginInfo(QString)","KEY_BSECGB") # 키보드 보안 0:정상, 1:해지
        h = self.dynamicCall("GetLoginInfo(QString)","FIREW_SECGB")# 방화벽 설정 0:미설정,1:설정,2:해지
        # print(a,b,c,e,f,g,h)
        print("%s님의 계좌번호 %s" % (e,b))
        
    # @staticmethod
    # def request_balance():
    #     Main.tt.SetFieldData("t0441InBlock", "accno", 0, Main.Number)
    #     Main.tt.SetFieldData("t0441InBlock", "passwd", 0, demo_pw)
    #     err = Main.tt.Request(False)

    @staticmethod
    def request_option_table(yyyymm=None):
        T2301.t2301.SetFieldData("t2301InBlock", "yyyymm", 0, yyyymm)
        T2301.t2301.SetFieldData("t2301InBlock", "gubun", 0, "G")
        err = T2301.t2301.Request(False)

    @staticmethod
    def request_hoka(): # 호가 잔량
        Hoka.t.SetFieldData("t2105InBlock", "shcode", 0, fCode)
        err = Hoka.t.Request(False) 
        
    @staticmethod
    def request_Chart1(Code=None):
        cc = Chart1.Call_일목
        cc.SetFieldData("ChartIndexInBlock", "indexid", 0, "")
        cc.SetFieldData("ChartIndexInBlock", "indexname", 0, "일목균형표")
        cc.SetFieldData("ChartIndexInBlock", "indexparam", 0, "")
        cc.SetFieldData("ChartIndexInBlock", "market", 0, "5")
        cc.SetFieldData("ChartIndexInBlock", "period", 0, "1")
        cc.SetFieldData("ChartIndexInBlock", "shcode", 0, Code)
        cc.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500")
        cc.SetFieldData("ChartIndexInBlock", "ncnt", 0, n분)
        cc.SetFieldData("ChartIndexInBlock", "sdate", 0, "")
        cc.SetFieldData("ChartIndexInBlock", "edate", 0, "")
        cc.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1")
        cc.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0")
        cc.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1")
        err = cc.RequestService("ChartIndex", 0)


    def request_Chart2(Code=None):
        cp = Chart2.Put_일목
        cp.SetFieldData("ChartIndexInBlock", "indexid", 0, "")
        cp.SetFieldData("ChartIndexInBlock", "indexname", 0, "일목균형표")
        cp.SetFieldData("ChartIndexInBlock", "indexparam", 0, "")
        cp.SetFieldData("ChartIndexInBlock", "market", 0, "5") 
        cp.SetFieldData("ChartIndexInBlock", "period", 0, "1")
        cp.SetFieldData("ChartIndexInBlock", "shcode", 0, Code)
        cp.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500")
        cp.SetFieldData("ChartIndexInBlock", "ncnt", 0, n분)
        cp.SetFieldData("ChartIndexInBlock", "sdate", 0, "") 
        cp.SetFieldData("ChartIndexInBlock", "edate", 0, "") 
        cp.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1") 
        cp.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0")
        cp.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1")
        err = cp.RequestService("ChartIndex", 0)


    # @staticmethod
    # def order_option(Code=None, BnsTpCode=None):
    #     co = CFOAT010.order
    #     co.SetFieldData("CFOAT00100InBlock1", "AcntNo", 0, Main.Number)
    #     co.SetFieldData("CFOAT00100InBlock1", "Pwd", 0, "0000")
    #     co.SetFieldData("CFOAT00100InBlock1", "FnoIsuNo", 0, Code)
    #     co.SetFieldData("CFOAT00100InBlock1", "BnsTpCode", 0, BnsTpCode)
    #     co.SetFieldData("CFOAT00100InBlock1", "FnoOrdprcPtnCode", 0, "03")
    #     co.SetFieldData("CFOAT00100InBlock1", "FnoOrdPrc", 0, "")
    #     co.SetFieldData("CFOAT00100InBlock1", "OrdQty", 0, 수량)
    #     err = co.Request(False)
    #     print("주문 오류 %s" % err)
    

if __name__ == "__main__":
    Main()