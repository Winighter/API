import os,sys,time,math,threading

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
widgets = None
매수 = False
정정 = False

class Main(QMainWindow):
    Number = ""
    balance_dict = {}
    revise_order_dict = {}
    f128 = 0
    def __init__(self):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.log_out = False
        
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = 'ATS'
        description = "ATS APP - Auto Trading System"

        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.Label_title.setText(description)
        
        # KIWOOM API SETUP
        # ///////////////////////////////////////////////////////////////
        
        # EVENTLOOP
        self.login_event_loop = QEventLoop()
        self.tr_event_loop = QEventLoop()
        # OBJECT
        Main.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.onEvent()
        
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.btn_Menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        
        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_Home.clicked.connect(self.onClick)
        widgets.btn_DDE.clicked.connect(self.onClick)
        widgets.btn_Menu.clicked.connect(self.onClick)

        widgets.btn_Login.clicked.connect(self.onLogin)
        widgets.btn_Con_Real.clicked.connect(self.Connect_Real)
        widgets.btn_Discon_Real.clicked.connect(self.Disconnect_All_Real)


        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.btn_setting(self, True)
        widgets.btn_setting.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.btn_Account.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        
        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.page_home)
        widgets.btn_Home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_Home.styleSheet()))

        # OBJECT
        # ///////////////////////////////////////////////////////////////

    def text(text):
        widgets.textBrowser.append(str(text))
  
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def onClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        
        # SHOW HOME PAGE    
        if btnName == "btn_Home":
            widgets.stackedWidget.setCurrentWidget(widgets.page_home)

        if btnName == "btn_DDE":
            widgets.stackedWidget.setCurrentWidget(widgets.page_DDE)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        
        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
            
    def changeTextFunction(self):
        #self.Textbrowser이름.setPlainText()
        #Textbrowser에 있는 글자를 가져오는 메서드
        widgets.textBrowser.setPlainText("This is Textbrowser - Change Text")    
        
    def appendTextFunction(self):
        widgets.textBrowser.append("Append Text")
        widgets.textBrowser.setEnabled(True)
        
    def clearTextFunction(self):
        #self.Textbrowser.clear()
        #Textbrowser에 있는 글자를 지우는 메서드
        self.textbrow_Test.clear()

    # KIWOOM (OPEN) API TERRITORY
    # ///////////////////////////////////////////////////////////////

    def onLogin(self):
        if Settings.LOGIN_STATE == 0:
            Main.kiwoom.dynamicCall("CommConnect()")
            widgets.label_State.setText("Connecting...")
            widgets.label_State.setStyleSheet("Color: #f1fa8c")
            self.login_event_loop.exec_()
        else:
            pass
            # state = Main.kiwoom.dynamicCall("GetConnectState()")


    def login_slot(self, err_code): # 로그인
        if err_code == 0:
            self.login_event_loop.exit()
            Settings.LOGIN_STATE = 1
            widgets.label_State.setText("Connected")
            widgets.label_State.setStyleSheet("Color: lightgreen")
            widgets.btn_Login.setText('로그인 성공')
            self.request_login_info()
            self.request_balance()
            self.request_cCode()
            self.request_pCode()


    def Connect_Real(self):
        if Settings.LOGIN_STATE == 1:
            # Main.kiwoom.dynamicCall("SetRealReg(QString,QString,QString,QString)",SN_REAL_HOKA,self.fCode,'10;128','0')
            self.regist_Real_Code(SN_REAL_FUTURE_PRICE,self.fCode,FL_FUTURE,'0')
            self.regist_Real_Code(SN_REAL_HOKA,self.fCode,FL_HOKA,'0')
            self.regist_Real_Code(SN_REAL_CALL_OPTION_MARKET_PRICE,self.cCodeList,FL_SIGO,'1')
            self.regist_Real_Code(SN_REAL_PUT_OPTION_MARKET_PRICE,self.pCodeList,FL_SIGO,'1')
        else:
            print("Unconnected")


    def Disconnect_All_Real(self):
        if Settings.LOGIN_STATE == 1:
            Main.kiwoom.dynamicCall("SetRealRemove(QString,QString)", 'ALL','ALL')
        else:
            print("Unconnected")


    def regist_Real_Code(self,strScreenNo,CodeList,FidList,OptType):
        Main.kiwoom.dynamicCall("SetRealReg(QString,QString,QString,QString)",strScreenNo,CodeList,FidList,OptType)


    # Event Management territory
    def onEvent(self):
        Main.kiwoom.OnEventConnect.connect(self.login_slot)
        Main.kiwoom.OnReceiveTrData.connect(self.trdata_slot)
        Main.kiwoom.OnReceiveChejanData.connect(self.chejan_slot)
        Main.kiwoom.OnReceiveRealData.connect(self.realdata_slot)


    def request_login_info(self):
        self.Number = Main.kiwoom.dynamicCall("GetLoginInfo(QString)","ACCLIST")[:-1] # or "ACCNO" / 계좌번호
        user = Main.kiwoom.dynamicCall("GetLoginInfo(QString)","USER_NAME") # 사용자 이름

        fList = Main.kiwoom.dynamicCall("GetFutureList()").split(';')
        self.fCode = fList[0]

        fMonth = list(map(int, Main.kiwoom.dynamicCall("GetMonthList()").split(';')))
        fMonth.sort()
        self.fMonth = str(fMonth[0])

        oMonth = list(map(int, Main.kiwoom.dynamicCall("GetMonthList()").split(';')))
        oMonth.sort()
        self.oMonth = str(oMonth[0])

        print("\n%s님의 계좌번호 %s\n" % (user,self.Number))


    # Post here your functions for Tr Data
    # ///////////////////////////////////////////////////////////////
    def request_balance(self):
        Main.kiwoom.dynamicCall("SetInputValue(QString,QString)","계좌번호",self.Number)
        Main.kiwoom.dynamicCall("SetInputValue(QString,QString)","비밀번호",'')
        Main.kiwoom.dynamicCall("SetInputValue(QString,QString)","비밀번호입력매체구분",'00')
        Main.kiwoom.dynamicCall("CommRqData(QString,QString,QString,QString)","선옵잔고","opw20007","0", SN_TR1)
        self.tr_event_loop.exec_()


    def request_cCode(self):
        Main.kiwoom.dynamicCall("SetInputValue(QString,QString)","만기년월",self.oMonth)
        Main.kiwoom.dynamicCall("CommRqData(QString,QString,QString,QString)","콜종목코드","OPT50021","0", SN_TR2)
        self.tr_event_loop.exec_()      


    def request_pCode(self):
        Main.kiwoom.dynamicCall("SetInputValue(QString,QString)","만기년월",self.oMonth)
        Main.kiwoom.dynamicCall("CommRqData(QString,QString,QString,QString)","풋종목코드","OPT50022","0", SN_TR3)
        self.tr_event_loop.exec_()      


    def request_option_daychart(self,종목코드):
        Main.kiwoom.dynamicCall("SetInputValue(QString,QString)","종목코드",종목코드)
        Main.kiwoom.dynamicCall("SetInputValue(QString,QString)","기준일자",self.oMonth)
        Main.kiwoom.dynamicCall("CommRqData(QString,QString,QString,QString)","옵션일차트","opt50068","0", SN_TR4)
        self.tr_event_loop.exec_()

    # TR EVENTS
    # ///////////////////////////////////////////////////////////////
    def trdata_slot(self, sScrNo, sRQName, sTrCode, sRecordName, sPrevNext):
        if sRQName == '선옵잔고':
            rows = Main.kiwoom.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)
            if rows > 0:
                for i in range(rows):
                    Code = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "종목코드")
                    Code = Code.strip()

                    Name = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "종목명")
                    Name = Name.strip()

                    Gubun = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "매도매수구분")
                    Gubun = Gubun.strip()

                    Quantity = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "수량")
                    Quantity = Quantity.strip()

                    Buy_Price = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "매입단가")
                    Buy_Price = Buy_Price.strip()

                    Price = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "현재가")
                    Price = Price.strip()

                    평가손익 = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "평가손익")
                    평가손익 = 평가손익.strip()

                    청산가능수량 = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "청산가능수량")
                    청산가능수량 = 청산가능수량.strip()

                    약정금액 = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "약정금액")
                    약정금액 = 약정금액.strip()

                    평가금액 = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "평가금액")
                    평가금액 = 평가금액.strip()
                    
                    print(Code,Name,Gubun,Quantity,Buy_Price,Price,평가손익,청산가능수량,약정금액,평가금액)
            else:
                print("비어있는 잔고\n")
            self.tr_event_loop.exit()


        if sRQName == "콜종목코드":
            str = []
            rows = Main.kiwoom.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)
            for i in range(rows):
                     
                cPrice = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "현재가")
                cPrice = float(cPrice.strip().lstrip('+').lstrip('-'))

                cOpen = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "시가")
                cOpen = float(cOpen.strip().lstrip('+').lstrip('-'))

                cHigh = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "고가")
                cHigh = float(cHigh.strip().lstrip('+').lstrip('-'))

                cLow = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "저가")
                cLow = float(cLow.strip().lstrip('+').lstrip('-'))

                cCode = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "종목코드")
                cCode = cCode.strip()

                cActPrice = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "행사가")
                cActPrice = cActPrice.strip()

                if (sgMin <= cHigh <= sgMax):
                    str.append(cCode)

            self.cCodeList = ';'.join(str)
            self.tr_event_loop.exit()


        if sRQName == "풋종목코드":
            str = []
            rows = Main.kiwoom.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)
            for i in range(rows):
                pPrice = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "현재가")
                pPrice = float(pPrice.strip().lstrip('+').lstrip('-'))

                pOpen = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "시가")
                pOpen = float(pOpen.strip().lstrip('+').lstrip('-'))

                pHigh = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "고가")
                pHigh = float(pHigh.strip().lstrip('+').lstrip('-'))

                pLow = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "저가")
                pLow = float(pLow.strip().lstrip('+').lstrip('-'))

                pCode = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "종목코드")
                pCode = pCode.strip()

                pActPrice = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "행사가")
                pActPrice = pActPrice.strip()

                if (sgMin <= pHigh <= sgMax):
                    str.append(pCode)

            self.pCodeList = ';'.join(str)
            self.tr_event_loop.exit()


        if sRQName == "옵션일차트":
            rows = Main.kiwoom.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)
            for i in range(rows):
                cdDay = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "일자")
                cdDay = cdDay.strip()

                cdPrcie = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "현재가")
                cdPrcie = float(cdPrcie.strip().lstrip('+').lstrip('-'))

                cdOpen = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "시가")
                cdOpen = float(cdOpen.strip().lstrip('+').lstrip('-'))

                cdHigh = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "고가")
                cdHigh = float(cdHigh.strip().lstrip('+').lstrip('-'))

                cdLow = Main.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "저가")
                cdLow = float(cdLow.strip().lstrip('+').lstrip('-'))
                print(cdDay)

            self.tr_event_loop.exit()


    # REAL EVENTS
    # ///////////////////////////////////////////////////////////////
    def chejan_slot(self,Gubun, nItemCnt, sFidList):

        if int(Gubun) == 0: # 접수와 체결

            oCode = Main.kiwoom.dynamicCall("GetChejanData(int)", 9001) # 종목코드

            medosu = Main.kiwoom.dynamicCall("GetChejanData(int)", 905) # 구분
            medosu = medosu.strip().lstrip('+').lstrip('-')

            order_number = Main.kiwoom.dynamicCall("GetChejanData(int)", 9203) # 주문번호
            on = int(order_number)

            order_q = Main.kiwoom.dynamicCall("GetChejanData(int)", 900) # 주문수량

            un_quan = Main.kiwoom.dynamicCall("GetChejanData(int)", 902) # 미체결수량
            un_quan = int(un_quan)

            one_order_number = Main.kiwoom.dynamicCall("GetChejanData(int)", 904) # 원주문번호
            oon = int(one_order_number)

            order_price = Main.kiwoom.dynamicCall("GetChejanData(int)", 901) # 주문가격

            price = Main.kiwoom.dynamicCall("GetChejanData(int)", 10) # 현재가

            rPrice1 = Main.kiwoom.dynamicCall("GetChejanData(int)", 28) # 최우선 매수호가1

            if un_quan == 0 and (("취소" not in medosu)):
                print("\n%s 체결 | No.%s | %s | 주문가: %s | 주문수량: %s개 | 미체결량: %s개\n"%(medosu,on,oCode,order_price,order_q,un_quan))
            else:
                Main.revise_order_dict = ({'종목코드':oCode,'구분':medosu,'주문번호':on,'주문수량':order_q,'주문가격':order_price,'미체결수량':un_quan,'원주문번호':oon,'매수호가':rPrice1,'현재가':price})
                print("%s 접수 | No.%s | %s | 주문가: %s | 주문수량: %s개 | 미체결량: %s개 | 현재가: %s"%(medosu,on,oCode,order_price,order_q,un_quan,price))


    # REALTYPE DATA
    def realdata_slot(self, oCode, RealType):

        if RealType == "선물시세":
            a = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,10) # 현재가
            a = abs(float(a))
            self.Future_Price = a

            b = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,16)  # 시가
            b = abs(float(b))

            c = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,17)  # 고가
            c = abs(float(c))

            d = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,18)  # 저가
            d = abs(float(d))

            e = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,197)  # KOSPI200
            e = abs(float(e))
            print("선물시세: %s %s %s %s %s"%(a,b,c,d,e))


        elif RealType == "선물호가잔량":
            순매수잔량 = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,128) # 순매수잔량
            print('순매수잔량: %s' % 순매수잔량)


        elif RealType == "옵션시세":
            a = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,10) # 현재가
            a = abs(float(a))

            b = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,16)  # 시가
            b = abs(float(b))

            c = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,17)  # 고가
            c = abs(float(c))

            d = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,18)  # 저가
            d = abs(float(d))

            e = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,28) # (최우선)매수호가
            e = abs(float(e))

            f = Main.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,137) # 호가순잔량
            f = abs(float(f))
            print("옵션시세: %s %s %s %s %s %s"%(a,b,c,d,e,f))


    # CUSTOM FUNCTION
    # ///////////////////////////////////////////////////////////////

    # FUNTION THAT FINDS BRO CODE
    def get_bro_code(self,bCode):
        PM = 2.5
        if bCode[0:1] == "2":
            PM = PM*-1
        a = str(bCode[0:5])
        b = str(math.trunc(option_table_dict[bCode]['행사가'] + PM))
        return a + b


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))
    main = Main()
    sys.exit(app.exec_())