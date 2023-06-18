from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *


from modules import *
import math

class Kiwoom(QAxWidget):
    def __init__(self):
        print('kiwoom')

    
    def onLogin(self):
        if S.LOGIN_STATE == 0:
            if S.STATE == 0:
                S.STATE = 1
                Kiwoom.login_event_loop = QEventLoop()
                self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
                Kiwoom.onEvent(self)
                self.kiwoom.dynamicCall("CommConnect()")
                AppFunctions.loginState(self,2)
                Kiwoom.login_event_loop.exec_()
        else:
            Kiwoom.toggle_RealData_state(self, True)
            


    def onEvent(self):
        self.kiwoom.OnEventConnect.connect(self.login_slot)
        self.kiwoom.OnReceiveTrData.connect(self.trdata_slot)
        self.kiwoom.OnReceiveChejanData.connect(self.chejan_slot)
        self.kiwoom.OnReceiveRealData.connect(self.realdata_slot)


    def showEtcInfo(self,enable):
        if enable:
            if S.ETC_INFO == 0:
                S.ETC_INFO = 1
                self.ui.label_2.setStyleSheet("Color: #ffffff")
            else:
                S.ETC_INFO = 0
                self.ui.label_2.setStyleSheet("Color: #121212")
                
                

    def toggle_RealData_state(self, enable):
        if S.LOGIN_STATE == 1:
            if enable:
                if S.REAL_STATE == 0:
                    S.REAL_STATE = 1
                    Kiwoom.Disconnect_All_Real(self)
                    Kiwoom.regist_Real_Code(self,'3692',S.fCode,S.FL_FUTURE,'0')
                    Kiwoom.regist_Real_Code(self,'3691',S.fCode,S.FL_HOKA,'1')
                    Kiwoom.regist_Real_Code(self,'2000',self.cStr,S.FL_SIGO,'1')
                    Kiwoom.regist_Real_Code(self,'2001',self.pStr,S.FL_SIGO,'1')
                    AppFunctions.realDataState(self,0)
                else:
                    S.REAL_STATE = 0
                    Kiwoom.Disconnect_All_Real(self)
                    AppFunctions.realDataState(self,1)
        else:
            QMessageBox.information(self,'로그인 오류','로그인이 되어 있지 않습니다.')

    def Disconnect_All_Real(self):
        if S.LOGIN_STATE == 1:
            self.kiwoom.dynamicCall("SetRealRemove(QString,QString)",'ALL','ALL')
   
            
    def regist_Real_Code(self,strScreenNo,CodeList,FidList,OptType):
        self.kiwoom.dynamicCall("SetRealReg(QString,QString,QString,QString)",strScreenNo,CodeList,FidList,OptType)

    def request_login_info(self):
        self.Number = self.kiwoom.dynamicCall("GetLoginInfo(QString)","ACCLIST")[:-1] # or "ACCNO" / 계좌번호
        user = self.kiwoom.dynamicCall("GetLoginInfo(QString)","USER_NAME") # 사용자 이름

        fList = self.kiwoom.dynamicCall("GetFutureList()").split(';')
        S.fCode = fList[0]

        fMonth = list(map(int, self.kiwoom.dynamicCall("GetMonthList()").split(';')))
        fMonth.sort()
        self.fMonth = str(fMonth[0])

        oMonth = list(map(int, self.kiwoom.dynamicCall("GetMonthList()").split(';')))
        oMonth.sort()
        self.oMonth = str(oMonth[0])
        self.request = False
 

    # Post here your functions for Tr Data
    # ///////////////////////////////////////////////////////////////
    def request_balance(self):
        self.kiwoom.dynamicCall("SetInputValue(QString,QString)","계좌번호",self.Number)
        self.kiwoom.dynamicCall("SetInputValue(QString,QString)","비밀번호",'')
        self.kiwoom.dynamicCall("SetInputValue(QString,QString)","비밀번호입력매체구분",'00')
        self.kiwoom.dynamicCall("CommRqData(QString,QString,QString,QString)","선옵잔고","opw20007","0", '1001')
        self.tr_event_loop.exec_()

    def request_days_remaining(self, oCode):
        self.kiwoom.dynamicCall("SetInputValue(QString,QString)","종목코드",oCode)
        self.kiwoom.dynamicCall("SetInputValue(QString,QString)","기준일자",self.oMonth)
        self.kiwoom.dynamicCall("CommRqData(QString,QString,QString,QString)","선옵잔존일조회","OPT50033","0", '1002') 
        self.tr_event_loop.exec_()
        
    def request_option_price(self):
        self.kiwoom.dynamicCall("SetInputValue(QString,QString)","만기년월",self.oMonth)
        self.kiwoom.dynamicCall("CommRqData(QString,QString,QString,QString)","옵션시세조회","opt50020","0", '1003')
        self.tr_event_loop.exec_()

    # ORDER FUNTION & ORDER RESULTS
    def request_orderFO(self,sRQName,sCode,lQty,sPrice,why,OrdNo):
        if sRQName == '신규매수':
            print("\n%s 신규매수 주문요청 | 종목코드: %s | 주문가격: %s\n" % (why,sCode,sPrice))
            err = self.kiwoom.dynamicCall("SendOrderFO(QString,QString,QString,QString,QString,QString,QString,QString,QString,QString)",[
                sRQName,'1000',self.Number,sCode,'1','2','1',S.수량,sPrice,''])

        if sRQName == '신규매도':
            print("\n%s 신규매도 주문요청 | 종목코드: %s | 주문가격: 시장가\n" % (why,sCode))
            err = self.kiwoom.dynamicCall("SendOrderFO(QString,QString,QString,QString,QString,QString,QString,QString,QString,QString)",[
                sRQName,'1000',self.Number,sCode,'1','1','3',lQty,'3',''])
            
        if sRQName == '정정':
            print("\n%s 정정 주문요청 | 종목코드: %s | 주문가격: %s\n" % (why,sCode,sPrice))
            err = self.kiwoom.dynamicCall("SendOrderFO(QString,QString,QString,QString,QString,QString,QString,QString,QString,QString)",[
                sRQName,'1000',self.Number,sCode,'2','2','1',lQty,sPrice,OrdNo])

        if err == 0:
            print('%s %s 주문 성공' % (sCode,sRQName))
            if sRQName == '신규매수':
                broCode = Kiwoom.get_bro_code(self,sCode)
                S.BroCodeList.append(broCode)
                Kiwoom.regist_Real_Code(self,S.SN_REAL,broCode,S.FL_SIGO,'1')

            if sRQName == '신규매도':
                S.매수 = False
                S.balance_dict = {}
                
            if sRQName == '정정':
                pass
                
        else:
            print('%s %s 주문 에러: %s' % (sCode,sRQName,err))

    # CUSTOM FUNCTION
    # ///////////////////////////////////////////////////////////////

    # FUNTION THAT FINDS BRO CODE
    def get_bro_code(self,bCode):
        PM = 2.5
        if bCode[0:1] == "2":
            PM = PM*-1
        a = str(bCode[0:5])
        b = str(math.trunc(S.option_table_dict[bCode]['행사가'] + PM))
        return a + b


    def compare_CP(self,maxmin,cActprice,pActPrice):

        if maxmin == 'max':
            if cActprice > pActPrice:
                r = cActprice
            if cActprice < pActPrice:
                r = pActPrice

        if maxmin == 'min':
            if cActprice > pActPrice:
                r = pActPrice
            if cActprice < pActPrice:
                r = cActprice
            S.Act_Check = 1

        if cActprice == pActPrice:
            r = cActprice

        return r