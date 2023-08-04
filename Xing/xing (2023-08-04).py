import pythoncom
import win32com.client as win32com
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class HTS:
    login_state = 0
    def OnLogin(self, szCode, szMsg):
        if szCode == "0000":
            HTS.login_state = 1
        else:
            print("[X] HTS Login failed !!! {%s: %s}\n" % (szCode,szMsg))


class Chart1:
    cc = None

    def OnReceiveChartRealData(self, trCode):
        h = self.GetFieldChartRealData("ChartIndexOutBlock1", "High") # 상한선
        # h = float(h)

        l = self.GetFieldChartRealData("ChartIndexOutBlock1", "Low") # 하한선
        # l = float(l)
        print('Call :%s, %s'%(h,l))


class Chart2:
    cp = None

    def OnReceiveChartRealData(self, trCode):
        h = self.GetFieldChartRealData("ChartIndexOutBlock1", "High") # 상한선
        # h = float(h)

        l = self.GetFieldChartRealData("ChartIndexOutBlock1", "Low") # 하한선
        # l = float(l)
        print('Put :%s, %s'%(h,l))

class Xing(QAxWidget):
    check = 0
    tt = None
    oo = None

    def login_xing(self):
        Xing_hts = win32com.DispatchWithEvents("XA_Session.XASession", HTS)

        Chart1.cc = win32com.DispatchWithEvents("XA_DataSet.XAQuery", Chart1)
        Chart1.cc.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"

        Chart2.cp = win32com.DispatchWithEvents("XA_DataSet.XAQuery", Chart2)
        Chart2.cp.ResFileName = "C:/eBEST/xingAPI/Res/ChartIndex.res"
        
        Xing_hts.ConnectServer("hts.ebestsec.co.kr", 20001)

        if Xing_hts.Login('ypeace20', 'yw2603!@', 'c3484758!@', 0, True) is True:
            pass
        else:
            nErrCode = Xing_hts.GetLastError()
            strErrMsg = Xing_hts.GetErrorMessage(nErrCode)
            print("\n[X] HTS Server Connection Failed !!! {%s: %s}" % (nErrCode, strErrMsg))
        while HTS.login_state == 0:
            pythoncom.PumpWaitingMessages()

        
    @staticmethod
    def request_Chart1(Code=None):
        Chart1.cc.SetFieldData("ChartIndexInBlock", "indexid", 0, "")
        Chart1.cc.SetFieldData("ChartIndexInBlock", "indexname", 0, "Price Channel")
        Chart1.cc.SetFieldData("ChartIndexInBlock", "indexparam", 0, "20")
        Chart1.cc.SetFieldData("ChartIndexInBlock", "market", 0, "5")
        Chart1.cc.SetFieldData("ChartIndexInBlock", "period", 0, "1")
        Chart1.cc.SetFieldData("ChartIndexInBlock", "shcode", 0, Code)
        Chart1.cc.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500")
        Chart1.cc.SetFieldData("ChartIndexInBlock", "ncnt", 0, '10')
        Chart1.cc.SetFieldData("ChartIndexInBlock", "sdate", 0, "")
        Chart1.cc.SetFieldData("ChartIndexInBlock", "edate", 0, "")
        Chart1.cc.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1")
        Chart1.cc.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0")
        Chart1.cc.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1")
        err = Chart1.cc.RequestService("ChartIndex", 0)
        print(err)


    def request_Chart2(Code=None):
        Chart2.cp.SetFieldData("ChartIndexInBlock", "indexid", 0, "")
        Chart2.cp.SetFieldData("ChartIndexInBlock", "indexname", 0, "Price Channel")
        Chart2.cp.SetFieldData("ChartIndexInBlock", "indexparam", 0, "20")
        Chart2.cp.SetFieldData("ChartIndexInBlock", "market", 0, "5") 
        Chart2.cp.SetFieldData("ChartIndexInBlock", "period", 0, "1")
        Chart2.cp.SetFieldData("ChartIndexInBlock", "shcode", 0, Code)
        Chart2.cp.SetFieldData("ChartIndexInBlock", "qrycnt", 0, "500")
        Chart2.cp.SetFieldData("ChartIndexInBlock", "ncnt", 0, '10')
        Chart2.cp.SetFieldData("ChartIndexInBlock", "sdate", 0, "") 
        Chart2.cp.SetFieldData("ChartIndexInBlock", "edate", 0, "") 
        Chart2.cp.SetFieldData("ChartIndexInBlock", "Isamend", 0, "1") 
        Chart2.cp.SetFieldData("ChartIndexInBlock", "Isgab", 0, "0")
        Chart2.cp.SetFieldData("ChartIndexInBlock", "IsReal", 0, "1")
        err = Chart2.cp.RequestService("ChartIndex", 0)
        print(err)