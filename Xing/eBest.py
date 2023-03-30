import pythoncom,threading,time
import win32com.client as win32com
from Info import *


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
    t0441_ok = False
    chooose = 0

    def OnReceiveData(self, trCode):
        cnt0441 = self.GetBlockCount("t0441OutBlock1")
        if int(cnt0441) == 0:
            if self.매수 == False:
                print("[%s] %s %s --- %s %s" % (MyBalance.chooose,ChartIndex1.CB_terms,ChartIndex1.C26d,ChartIndex2.PB_terms,ChartIndex2.P26d))

                if (MyBalance.chooose != 2) and (ChartIndex1.CB_terms == True) and (ChartIndex1.C26d == 1):
                    self.매수 = True
                    print("Call 매수 시작")
                    Main.order_option(oCode=Main.cCode,BnsTpCode="2")
                if (MyBalance.chooose != 1) and (ChartIndex2.PB_terms == True) and (ChartIndex2.P26d == 1):
                    self.매수 = True
                    print("Put 매수 시작")
                    Main.order_option(oCode=Main.pCode,BnsTpCode="2")

        elif (int(cnt0441) != 0) and (self.매수 == False):
            self.매수 = True
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
                            ChartIndex1.CB_terms = False
                            print("[%s] Call 수익률: %s 매도 주문 시작" % (expcode,sunikrt))
                            Main.order_option(oCode=expcode,BnsTpCode="1")
    
                        elif CP == "3": # Put 매도
                            self.매수 = False
                            ChartIndex2.PB_terms = False
                            print("[%s] Put 수익률: %s 매도 주문 시작" % (expcode,sunikrt))
                            Main.order_option(oCode=expcode,BnsTpCode="1")


                    # 시가 고가에 의한 손절(매도)
                    if T2301.disaprng1 == True and T2301.sigo2 == 0 and T2301.sigo1 > 0 and CP == "2": # Call 매도
                        self.매수 = False
                        ChartIndex1.CB_terms = False
                        print("[%s] Put 가격 변동 확인됨 --- Call 손절 주문 수익률: %s" % (expcode,sunikrt)+"%")
                        Main.order_option(oCode=expcode,BnsTpCode="1")
                
                    elif (T2301.disaprng2 == True) and (T2301.sigo1 == 0) and (T2301.sigo2 > 0) and (CP == "3"): # Put 매도
                        self.매수 = False
                        ChartIndex2.PB_terms = False
                        print("[%s] Call 가격 변동 확인됨 --- Put 손절 주문 수익률: %s" % (expcode,sunikrt)+"%")
                        Main.order_option(oCode=expcode,BnsTpCode="1")
        # threading.Timer(1.5,Main.request_balance).start()


class T2301: # 옵션 전광판
    # Call = 1 / Put = 2 이다
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
    disaprng1 = False
    disaprng2 = False

    def OnReceiveData(self,trCode):
        Main.request_chartindex1(code=Main.cCode,min=n분)
        time.sleep(1.5)
        Main.request_chartindex2(code=Main.pCode,min=n분)
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
                    T2301.disaprng1 = True
                    T2301.sigo1 = T2301.cnt1
                    
                elif (sigo_max > (open2 and high2) > sigo_min) and (open2 == high2):
                    T2301.cnt2 += 1
                    T2301.disaprng2 = True
                    T2301.sigo2 = T2301.cnt2

                if (bas_max > int(price1) > bas_min):
                    T2301.price1_dict[optcode1] = price1
                    T2301.price1_list = list(T2301.price1_dict.keys())

                elif (bas_max > int(price2) > bas_min):
                    T2301.price2_dict[optcode2] = price2
                    T2301.price2_list = list(T2301.price2_dict.keys())

            else:
                T2301.cCode = T2301.price1_list[0]
                T2301.pCode = T2301.price2_list[-1]
                Main.cCode = T2301.cCode
                Main.pCode = T2301.pCode
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
                    elif (T2301.sigo1) == (T2301.sigo2):
                        T2301.choose = 0
                T2301.cnt1 = 0
                T2301.cnt2 = 0

                # threading.Timer(2,Main.request_option_table,args=[when]).start()


class ChartIndex1:
    C26d = 0
    CB_terms = False
    Call_일목 = None

    def OnReceiveChartRealData(self, trCode):
        현재가 = self.GetFieldChartRealData("ChartIndexOutBlock1", "close") # 현재가(종가)
        현재가 = float(현재가)

        기준선 = self.GetFieldChartRealData("ChartIndexOutBlock1", "value2") # 기준선
        기준선 = float(기준선)
        
        if 기준선 != 0:
            if 현재가 > 기준선:
                ChartIndex1.C26d = 1
            elif 현재가 < 기준선:
                ChartIndex1.C26d = 0
                ChartIndex1.CB_terms = True


class ChartIndex2:
    P26d = 0
    Put_일목 = None
    PB_terms = False
    
    def OnReceiveChartRealData(self, trCode):
        현재가 = self.GetFieldChartRealData("ChartIndexOutBlock1", "close") # 현재가(종가)
        현재가 = float(현재가)

        기준선 = self.GetFieldChartRealData("ChartIndexOutBlock1", "value2") # 기준선
        기준선 = float(기준선)

        if 기준선 != 0:
            if 현재가 > 기준선:
                ChartIndex2.P26d = 1
            elif 현재가 < 기준선:
                ChartIndex2.P26d = 0
                ChartIndex2.PB_terms = True
                

class CFOAT010: # 주문
    def OnReceiveData(self, trCode):
        FnoIsuNo = self.GetFieldData("CFOAT00100OutBlock1", "FnoIsuNo", 0) # 종목번호
        OrdQty = self.GetFieldData("CFOAT00100OutBlock1", "OrdQty", 0) # 주문수량
        OrdNo = self.GetFieldData("CFOAT00100OutBlock2", "OrdNo", 0) # 주문번호
        print("주문 체결: 종목번호:%s, 주문수량:%s, 주문번호:%s" % (FnoIsuNo,OrdQty,OrdNo))


class Main():
    check = 0
    tt = None
    oo = None
    cCode = ""
    pCode = ""

    def __init__(self):

        Xing_hts = win32com.DispatchWithEvents("XA_Session.XASession", HTS)
        Xing = win32com.DispatchWithEvents("XA_Session.XASession", XASession)

        Main.tt = win32com.DispatchWithEvents("XA_DataSet.XAQuery", MyBalance)
        Main.tt.ResFileName = "C:/eBEST/xingAPI/Res/t0441.res"

        T2301.t2301 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", T2301)
        T2301.t2301.ResFileName = "C:/eBEST/xingAPI/Res/t2301.res"

        ChartIndex1.Call_일목 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", ChartIndex1)
        ChartIndex1.Call_일목.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"

        ChartIndex2.Put_일목 = win32com.DispatchWithEvents("XA_DataSet.XAQuery", ChartIndex2)
        ChartIndex2.Put_일목.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"

        CFOAT010.order = win32com.DispatchWithEvents("XA_DataSet.XAQuery", CFOAT010)
        CFOAT010.order.ResFileName = "C:/eBEST/xingAPI/Res/CFOAT00100.res"

        Xing_hts.ConnectServer("hts.ebestsec.co.kr", 20001)

        if Xing_hts.Login(ID, hts_pw, Cert_pw, 0, True) is True:
            pass
        else:
            nErrCode = Xing_hts.GetLastError()
            strErrMsg = Xing_hts.GetErrorMessage(nErrCode)
            print("\n[X] HTS Server Connection Failed !!! {%s: %s}" % (nErrCode, strErrMsg))
        while HTS.login_state == 0:
            pythoncom.PumpWaitingMessages()

        Xing.ConnectServer("demo.ebestsec.co.kr", 20001)
        if Xing.Login(ID, demo_pw, Cert_pw, 0, True) is True:
            pass
        else:
            nErrCode = Xing.GetLastError()
            strErrMsg = Xing.GetErrorMessage(nErrCode)
            print("[X] Server Connection Failed !!! {%s: %s}" % (nErrCode, strErrMsg))
        while XASession.login_state == 0:
            pythoncom.PumpWaitingMessages()

        for i in range(1):
            Number = Xing.GetAccountList(i)
            Main.Number = Number
            Name = Xing.GetAccountName(Number)
            Detail = Xing.GetAcctDetailName(Number)
            print("\n%s님의 %s 계좌번호: %s\n" % (Name, Detail, Number))

        Main.request_option_table(yyyymm=when)
        Main.request_balance()

        print(Main.cCode)
        while True:
            pythoncom.PumpWaitingMessages()

    @staticmethod
    def request_balance():
        Main.tt.SetFieldData("t0441InBlock", "accno", 0, Main.Number)
        Main.tt.SetFieldData("t0441InBlock", "passwd", 0, demo_pw)
        err = Main.tt.Request(False)
        # print("1 %s"%err)

    @staticmethod
    def request_option_table(yyyymm=None):
        T2301.t2301.SetFieldData("t2301InBlock", "yyyymm", 0, yyyymm)
        T2301.t2301.SetFieldData("t2301InBlock", "gubun", 0, "G")
        err = T2301.t2301.Request(False)
        # print("2 %s"% err)

    @staticmethod
    def request_chartindex1(code=None,min=None):
        cc = ChartIndex1.Call_일목
        cc.SetFieldData("ChartIndexInBlock", "indexid", 0, "")
        cc.SetFieldData("ChartIndexInBlock", "indexname", 0, "일목균형표")
        cc.SetFieldData("ChartIndexInBlock", "indexparam", 0, "")
        cc.SetFieldData("ChartIndexInBlock", "market", 0, "5")
        cc.SetFieldData("ChartIndexInBlock", "period", 0, "1")
        cc.SetFieldData("ChartIndexInBlock", "shcode", 0, code)
        cc.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500")
        cc.SetFieldData("ChartIndexInBlock", "ncnt", 0, min)
        cc.SetFieldData("ChartIndexInBlock", "sdate", 0, "")
        cc.SetFieldData("ChartIndexInBlock", "edate", 0, "")
        cc.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1")
        cc.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0")
        cc.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1")
        err = cc.RequestService("ChartIndex", 0)
        # print("3 %s"% err)

    def request_chartindex2(code=None,min=None):
        cp = ChartIndex2.Put_일목
        cp.SetFieldData("ChartIndexInBlock", "indexid", 0, "")
        cp.SetFieldData("ChartIndexInBlock", "indexname", 0, "일목균형표")
        cp.SetFieldData("ChartIndexInBlock", "indexparam", 0, "")
        cp.SetFieldData("ChartIndexInBlock", "market", 0, "5") 
        cp.SetFieldData("ChartIndexInBlock", "period", 0, "1")
        cp.SetFieldData("ChartIndexInBlock", "shcode", 0, code)
        cp.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500")
        cp.SetFieldData("ChartIndexInBlock", "ncnt", 0, min)
        cp.SetFieldData("ChartIndexInBlock", "sdate", 0, "") 
        cp.SetFieldData("ChartIndexInBlock", "edate", 0, "") 
        cp.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1") 
        cp.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0")
        cp.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1")
        err = cp.RequestService("ChartIndex", 0)
        # print("4 %s"% err)

    @staticmethod
    def order_option(oCode=None, BnsTpCode=None):
        co = CFOAT010.order
        co.SetFieldData("CFOAT00100InBlock1", "AcntNo", 0, Main.Number)
        co.SetFieldData("CFOAT00100InBlock1", "Pwd", 0, "0000")
        co.SetFieldData("CFOAT00100InBlock1", "FnoIsuNo", 0, oCode)
        co.SetFieldData("CFOAT00100InBlock1", "BnsTpCode", 0, BnsTpCode)
        co.SetFieldData("CFOAT00100InBlock1", "FnoOrdprcPtnCode", 0, "03")
        co.SetFieldData("CFOAT00100InBlock1", "FnoOrdPrc", 0, "")
        co.SetFieldData("CFOAT00100InBlock1", "OrdQty", 0, 수량)
        co.Request(False)


if __name__ == "__main__":
    Main()
