from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *


from modules import *
import math

S = Settings
class Kiwoom(QAxWidget):
    def __init__(self):
        print('kiwoom')

    
    def onLogin(self):
        if S.LOGIN_STATE == 0:
            Kiwoom.login_event_loop = QEventLoop()
            self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
            Kiwoom.onEvent(self)
            self.kiwoom.dynamicCall("CommConnect()")
            self.ui.LoginStateLabel.setText("Connecting...")
            self.ui.LoginStateLabel.setStyleSheet("Color: #f1fa8c")
            Kiwoom.login_event_loop.exec_()
        else:
            pass


    def onEvent(self):
        self.kiwoom.OnEventConnect.connect(self.login_slot)
        self.kiwoom.OnReceiveTrData.connect(self.trdata_slot)
        self.kiwoom.OnReceiveChejanData.connect(self.chejan_slot)
        self.kiwoom.OnReceiveRealData.connect(self.realdata_slot)


    def toggle_RealData_state(self, enable):
        if S.LOGIN_STATE == 1:
            if enable:
                if S.REAL_STATE == 0:
                    S.REAL_STATE = 1
                    self.ui.Pages_Widget.setCurrentWidget(self.ui.page_Dde)
                    Kiwoom.regist_Real_Code(self,S.SN_REAL_FUTURE_PRICE,S.fCode,S.FL_FUTURE,'0')
                    Kiwoom.regist_Real_Code(self,S.SN_REAL_HOKA,S.fCode,S.FL_HOKA,'1')
                    Kiwoom.regist_Real_Code(self,S.SN_REAL_CALL_OPTION_MARKET_PRICE,S.cCodeList,S.FL_SIGO,'1')
                    Kiwoom.regist_Real_Code(self,S.SN_REAL_PUT_OPTION_MARKET_PRICE,S.pCodeList,S.FL_SIGO,'1')
                    self.ui.Btn_RealData.setStyleSheet(u"QPushButton {\n""	color: rgb(144, 238, 144);\n""	border: 0px solid\n""}\n""QPushButton:hover {background-color: #69737A}\n""")
                else:
                    S.REAL_STATE = 0
                    Kiwoom.Disconnect_All_Real(self)
                    self.ui.Btn_RealData.setStyleSheet(u"QPushButton {\n""	color: rgb(255, 255, 255);\n""	border: 0px solid\n""}\n""QPushButton:hover {background-color: #000000}\n""")


    def Disconnect_All_Real(self):
        if Settings.LOGIN_STATE == 1:
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

        print("\n%s님의 계좌번호 %s\n" % (user,self.Number))
        

    # Post here your functions for Tr Data
    # ///////////////////////////////////////////////////////////////
    def request_balance(self):
        self.kiwoom.dynamicCall("SetInputValue(QString,QString)","계좌번호",self.Number)
        self.kiwoom.dynamicCall("SetInputValue(QString,QString)","비밀번호",'')
        self.kiwoom.dynamicCall("SetInputValue(QString,QString)","비밀번호입력매체구분",'00')
        self.kiwoom.dynamicCall("CommRqData(QString,QString,QString,QString)","선옵잔고","opw20007","0", S.SN_TR1)
        self.tr_event_loop.exec_()


    def request_cCode(self):
        self.kiwoom.dynamicCall("SetInputValue(QString,QString)","만기년월",self.oMonth)
        self.kiwoom.dynamicCall("CommRqData(QString,QString,QString,QString)","콜종목코드","OPT50021","0", S.SN_TR2)
        self.tr_event_loop.exec_()
        
        
    def request_pCode(self):
        self.kiwoom.dynamicCall("SetInputValue(QString,QString)","만기년월",self.oMonth)
        self.kiwoom.dynamicCall("CommRqData(QString,QString,QString,QString)","풋종목코드","OPT50022","0", S.SN_TR3)
        self.tr_event_loop.exec_()

    # ORDER FUNTION & ORDER RESULTS
    def request_orderFO(self,sRQName,sCode,lQty,sPrice):

        if sRQName == '신규매수':

            print("\n신규매수 주문요청 | 종목코드: %s | 주문가격: %s\n" % (sCode,sPrice))
            err= self.kiwoom.dynamicCall("SendOrderFO(QString,QString,QString,QString,QString,QString,QString,QString,QString,QString)",[
                sRQName,Settings.SN_ORDER,self.Number,sCode,'1','2','1',Settings.수량,sPrice,''])

        if sRQName == '신규매도':

            print("\n신규매도 주문요청 | 종목코드: %s | 주문가격: 시장가\n" % sCode)
            err = self.kiwoom.dynamicCall("SendOrderFO(QString,QString,QString,QString,QString,QString,QString,QString,QString,QString)",[
                sRQName,Settings.SN_ORDER,self.Number,sCode,'1','1','3',lQty,'3',''])
            
        if err == 0:
            print('%s %s 주문 성공' % (sCode,sRQName))

            if sRQName == '신규매수':
                broCode = self.get_bro_code(sCode)
                Settings.BroCodeList.append(broCode)
                Kiwoom.regist_Real_Code(self,S.SN_REAL,broCode,S.FL_SIGO,'1')
                
            if sRQName == '신규매도':
                self.balance_dict = {}
                self.매수 = False
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
        b = str(math.trunc(Settings.option_table_dict[bCode]['행사가'] + PM))
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
            Settings.Act_Check = 1

        if cActprice == pActPrice:
            r = cActprice

        return r