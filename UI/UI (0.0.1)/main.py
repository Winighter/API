import sys
import platform

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

from modules import *


widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
 
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = 'ATS'
        description = 'Welcome to the World'
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.TopBar_Left_Label.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # RIGHT MENUS
        widgets.Btn_Login.clicked.connect(lambda: Kiwoom.onLogin(self)) # LOGIN
        widgets.Btn_RealData.clicked.connect(lambda: Kiwoom.toggle_RealData_state(self, True))
        
        # LEFT MENUS
        widgets.Btn_Home.clicked.connect(self.buttonClick)
        widgets.Btn_Dde.clicked.connect(self.buttonClick)
        widgets.Btn_Etc.clicked.connect(self.buttonClick)
        
        # EXTRA LEFT MENUS
        widgets.Btn_VideoPlayer.clicked.connect(self.buttonClick)
        widgets.Btn_File.clicked.connect(self.buttonClick)
        widgets.Btn_Info.clicked.connect(self.buttonClick)
  

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self,True)
        widgets.Btn_Settings.clicked.connect(openCloseLeftBox)
        widgets.Btn_Close_extraLeftBox.clicked.connect(openCloseLeftBox)
        widgets.Btn_OpenVideoFile.clicked.connect(self.open_file)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.Btn_OpenLoginBox.clicked.connect(openCloseRightBox)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.Pages_Widget.setCurrentWidget(widgets.page_Home)
        
        self.tr_event_loop = QEventLoop()

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "Btn_Home":
            widgets.Pages_Widget.setCurrentWidget(widgets.page_Home)

        # SHOW DDE PAGE
        if btnName == "Btn_Dde":
            widgets.Pages_Widget.setCurrentWidget(widgets.page_Dde)

        # SHOW ETC PAGE
        if btnName == "Btn_Etc":
            widgets.Pages_Widget.setCurrentWidget(widgets.page_Etc)

        # SHOW VIDEO PLAYER PAGE
        if btnName == "Btn_VideoPlayer":
            widgets.Pages_Widget.setCurrentWidget(widgets.page_VideoPlayer)    
            UIFunctions.toggleLeftBox(self,True)    

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
    
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        
        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    # VIDEO PLAYER
    # ///////////////////////////////////////////////////////////////



    # IMPORT FILES
    # ///////////////////////////////////////////////////////////////

    def open_file(self):
        fileName = QFileDialog.getOpenFileNames(self,'Open file','./')


    def add_save(self):
        FileSave = QFileDialog.getSaveFileNames(self, 'Save file', './')
        # self.label2.setText(FileSave)
 
    def find_folder(self):
        FileFolder = QFileDialog.getExistingDirectory(self,'Find Folder')
        # self.label3.setText(FileFolder)

    # KIWOOM EVENTS
    # ///////////////////////////////////////////////////////////////
    
    # LOGIN EVENT
    def login_slot(self, err_code): # 로그인
        if err_code == 0:
            Kiwoom.login_event_loop.exit()
            Settings.LOGIN_STATE = 1
            self.ui.Pages_Widget.setCurrentWidget(self.ui.page_Dde)
            widgets.LoginStateLabel.setText("Connected")
            widgets.LoginStateLabel.setStyleSheet("Color: lightgreen")
            widgets.Btn_Login.setText('LogOut')
            widgets.Btn_Login.setStyleSheet(u"QPushButton {\n""	color: rgb(144, 238, 144);\n""	border: 0px solid\n""}\n""QPushButton:hover {background-color: #69737A}\n""")
            Kiwoom.regist_Real_Code(self,Settings.SN_REAL_MARKET_OPERATION_HOURS,'',Settings.SN_REAL_MARKET_OPERATION_HOURS,'1')
            Kiwoom.request_login_info(self)
            Kiwoom.request_balance(self)
            Kiwoom.request_cCode(self)
            Kiwoom.request_pCode(self)
            Kiwoom.request_cCode(self)
            Kiwoom.request_pCode(self)

    # TR EVENTS
    def trdata_slot(self, sScrNo, sRQName, sTrCode, sRecordName, sPrevNext):

        if sRQName == '선옵잔고':
            rows = self.kiwoom.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)
            if rows > 0:
                for i in range(rows):
                    Code = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "종목코드")
                    Code = Code.strip()

                    Gubun = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "매도매수구분")
                    Gubun = Gubun.strip()
                    if Gubun == '2':
                        Gubun = '매수'
                    else:
                        Gubun = '매도'

                    Quantity = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "수량")
                    Quantity = int(Quantity.strip())

                    Buy_Price = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "매입단가")
                    Buy_Price = float(Buy_Price.strip())*0.001

                    Price = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "현재가")
                    Price = float(Price.strip())*0.001

                    청산가능수량 = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "청산가능수량")
                    청산가능수량 = int(청산가능수량.strip())

                    약정금액 = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "약정금액")
                    약정금액 = int(약정금액.strip())

                    평가금액 = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "평가금액")
                    평가금액 = int(평가금액.strip())
                    
                    수익률 = round(((평가금액-약정금액)/약정금액*100),2)
                    
                    self.balance_dict = {'종목코드':Code,'구분':Gubun,'수량':Quantity,'매입단가':Buy_Price,'현재가':Price,'청산가능수량':청산가능수량,'약정금액':약정금액,'평가금액':평가금액,'수익률':수익률}
                    
                    if (Settings.손절 >= 수익률) or (수익률 >= Settings.이익):
                        Kiwoom.request_orderFO(self,'신규매도',Code,청산가능수량,'0')
            else:
                print("비어있는 잔고\n")
                self.balance_dict = {}
            self.tr_event_loop.exit()


        if sRQName == "콜종목코드":
            idx = 3
            self.cStr = []
            self.cAct = []
            rows = self.kiwoom.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)
            for i in range(rows):
                cPrice = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "현재가")
                cPrice = float(cPrice.strip().lstrip('+').lstrip('-'))

                cOpen = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "시가")
                cOpen = float(cOpen.strip().lstrip('+').lstrip('-'))

                cHigh = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "고가")
                cHigh = float(cHigh.strip().lstrip('+').lstrip('-'))

                cLow = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "저가")
                cLow = float(cLow.strip().lstrip('+').lstrip('-'))

                cCode = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "종목코드")
                cCode = cCode.strip()

                cActPrice = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "행사가")
                cActPrice = float(cActPrice.strip())

                Settings.option_table_dict.update({cCode:{'행사가':cActPrice,'현재가':cPrice,'시가':cOpen,'고가':cHigh,'저가':cLow}})
                
                if Settings.Act_Check == 0 and (Settings.sgMin <= cOpen <= Settings.sgMax):
                    self.cStr.append(cCode)
                    self.cAct.append(cActPrice)

                if Settings.Act_Check == 1 and (self.minActPrice <= cActPrice <= self.maxActPrice):
                    self.cStr.append(cCode)
                    widgets.tableWidget.setItem(idx, 0, QTableWidgetItem('%s'%cLow))
                    widgets.tableWidget.setItem(idx, 1, QTableWidgetItem('%s'%cHigh))
                    widgets.tableWidget.setItem(idx, 2, QTableWidgetItem('%s'%cOpen))
                    widgets.tableWidget.setItem(idx, 3, QTableWidgetItem('%s'%cPrice))
                    widgets.tableWidget.setItem(idx, 4, QTableWidgetItem('%s'%cActPrice))
                    idx += 1

            Kiwoom.Disconnect_All_Real(self)
            Settings.cCodeList = ';'.join(self.cStr)
            self.tr_event_loop.exit()


        if sRQName == "풋종목코드":
            idx = 3
            self.pStr = []
            self.pAct = []
            rows = self.kiwoom.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)
            for i in range(rows):
                pPrice = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "현재가")
                pPrice = float(pPrice.strip().lstrip('+').lstrip('-'))

                pOpen = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "시가")
                pOpen = float(pOpen.strip().lstrip('+').lstrip('-'))

                pHigh = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "고가")
                pHigh = float(pHigh.strip().lstrip('+').lstrip('-'))

                pLow = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "저가")
                pLow = float(pLow.strip().lstrip('+').lstrip('-'))

                pCode = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "종목코드")
                pCode = pCode.strip()

                pActPrice = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)", sTrCode, sRQName, i, "행사가")
                pActPrice = float(pActPrice.strip())

                Settings.option_table_dict.update({pCode:{'행사가':pActPrice,'현재가':pPrice,'시가':pOpen,'고가':pHigh,'저가':pLow}})

                if Settings.Act_Check == 0 and (Settings.sgMin <= pOpen <= Settings.sgMax):
                    self.pStr.append(pCode)
                    self.pAct.append(pActPrice)

                if Settings.Act_Check == 1 and (self.minActPrice <= pActPrice <= self.maxActPrice):
                    self.pStr.append(pCode)
                    widgets.tableWidget.setItem(idx, 8, QTableWidgetItem('%s'%pLow))
                    widgets.tableWidget.setItem(idx, 7, QTableWidgetItem('%s'%pHigh))
                    widgets.tableWidget.setItem(idx, 6, QTableWidgetItem('%s'%pOpen))
                    widgets.tableWidget.setItem(idx, 5, QTableWidgetItem('%s'%pPrice))
                    idx += 1

            Kiwoom.Disconnect_All_Real(self)
            Settings.pCodeList = ';'.join(self.pStr)
            self.tr_event_loop.exit()

            if Settings.Act_Check == 0:
                self.maxActPrice = Kiwoom.compare_CP(self,'max',self.cAct[0],self.pAct[0])
                self.minActPrice = Kiwoom.compare_CP(self,'min',self.cAct[-1],self.pAct[-1])
                self.cStr = []
                self.pStr = []


    # REAL EVENTS
    def chejan_slot(self,Gubun, nItemCnt, sFidList):

        if int(Gubun) == 0: # 접수와 체결

            oCode = self.kiwoom.dynamicCall("GetChejanData(int)", 9001) # 종목코드

            medosu = self.kiwoom.dynamicCall("GetChejanData(int)", 905) # 구분
            medosu = medosu.strip().lstrip('+').lstrip('-')

            order_number = self.kiwoom.dynamicCall("GetChejanData(int)", 9203) # 주문번호
            on = int(order_number)

            order_q = self.kiwoom.dynamicCall("GetChejanData(int)", 900) # 주문수량

            un_quan = self.kiwoom.dynamicCall("GetChejanData(int)", 902) # 미체결수량
            un_quan = int(un_quan)

            one_order_number = self.kiwoom.dynamicCall("GetChejanData(int)", 904) # 원주문번호
            oon = int(one_order_number)

            order_price = self.kiwoom.dynamicCall("GetChejanData(int)", 901) # 주문가격

            price = self.kiwoom.dynamicCall("GetChejanData(int)", 10) # 현재가

            rPrice1 = self.kiwoom.dynamicCall("GetChejanData(int)", 28) # 최우선 매수호가1

            if un_quan == 0 and (("취소" not in medosu)):
                print("\n%s 체결 | No.%s | %s | 주문가: %s | 주문수량: %s개 | 미체결량: %s개\n"%(medosu,on,oCode,order_price,order_q,un_quan))
            else:
                Main.revise_order_dict = ({'종목코드':oCode,'구분':medosu,'주문번호':on,'주문수량':order_q,'주문가격':order_price,'미체결수량':un_quan,'원주문번호':oon,'매수호가':rPrice1,'현재가':price})
                print("%s 접수 | No.%s | %s | 주문가: %s | 주문수량: %s개 | 미체결량: %s개 | 현재가: %s"%(medosu,on,oCode,order_price,order_q,un_quan,price))


    # REALTYPE DATA EVENT
    def realdata_slot(self, oCode, RealType):
        if RealType == "장시작시간":
            a = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,215) # 장운영구분
            if a == 0:
                print('장시작전')

            if a == 2:
                print('장종료전')

            if a == 3:
                print('장시작')

            if a == (4 or 8):
                print('장종료')

            if a == 9:
                print('장마감')

        if RealType == "선물시세":
            a = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,10) # 현재가
            a = abs(float(a))
            self.Future_Price = a

            b = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,16)  # 시가
            b = abs(float(b))

            c = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,17)  # 고가
            c = abs(float(c))

            d = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,18)  # 저가
            d = abs(float(d))

            e = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,197)  # KOSPI200
            e = abs(float(e))

            widgets.tableWidget.setItem(1, 1, QTableWidgetItem('%s'%a))
            widgets.tableWidget.setItem(1, 2, QTableWidgetItem('%s'%b))
            widgets.tableWidget.setItem(1, 3, QTableWidgetItem('%s'%c))
            widgets.tableWidget.setItem(1, 4, QTableWidgetItem('%s'%d))
            widgets.tableWidget.setItem(1, 5, QTableWidgetItem('%s'%e))


        elif RealType == "선물호가잔량":
            a = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,128) # 순매수잔량
            a = int(a)
            widgets.tableWidget.setItem(1, 6, QTableWidgetItem('%s'%a))

            if len(Settings.pSg_List) > 0 and len(Settings.cSg_List) == 0:
                if a >= Settings.cHoka:
                    Settings.추세 = 'CALL'
                    widgets.tableWidget.setItem(1, 7, QTableWidgetItem('CALL'))

                if 0 < a < Settings.cHoka:
                    widgets.tableWidget.setItem(1, 7, QTableWidgetItem('CALL 대기'))

                if a < 0:
                    widgets.tableWidget.setItem(1, 7, QTableWidgetItem(('CALL ?')))

            if len(Settings.cSg_List) > 0 and len(Settings.pSg_List) == 0:
                if a <= Settings.pHoka:
                    widgets.tableWidget.setItem(1, 7, QTableWidgetItem('PUT'))
                    Settings.추세 = 'PUT'

                if 0 > a > Settings.pHoka:
                    widgets.tableWidget.setItem(1, 7, QTableWidgetItem('PUT 대기'))

                if a > 0:
                    widgets.tableWidget.setItem(1, 7, QTableWidgetItem(('PUT ?')))

            if len(Settings.cSg_List) == len(Settings.pSg_List) == 0:
                widgets.tableWidget.setItem(1, 7, QTableWidgetItem('중립'))


        elif RealType == "옵션시세":
            a = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,10) # 현재가
            a = abs(float(a))

            b = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,16)  # 시가
            b = abs(float(b))

            c = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,17)  # 고가
            c = abs(float(c))

            d = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,18)  # 저가
            d = abs(float(d))

            e = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,28) # (최우선)매수호가
            e = abs(float(e))

            f = self.kiwoom.dynamicCall("GetCommRealData(QString,int)",oCode,137) # 호가순잔량
            f = abs(float(f))

            if oCode[0:1] == '2': # UPDATE CALL PRICE
                cIdx = self.cStr.index(oCode) + 3
                widgets.tableWidget.setItem(cIdx, 0, QTableWidgetItem('%s'%d))
                widgets.tableWidget.setItem(cIdx, 1, QTableWidgetItem('%s'%c))
                widgets.tableWidget.setItem(cIdx, 2, QTableWidgetItem('%s'%b))
                widgets.tableWidget.setItem(cIdx, 3, QTableWidgetItem('%s'%a))

                if b == c:
                    widgets.tableWidget.item(cIdx,1).setBackground(QBrush(QColor(214,230,245)))
                    widgets.tableWidget.item(cIdx,1).setTextColor(QBrush(QColor(0,0,0)))
                    widgets.tableWidget.item(cIdx,2).setBackground(QBrush(QColor(214,230,245)))
                    widgets.tableWidget.item(cIdx,2).setTextColor(QBrush(QColor(0,0,0)))
                    
                    if b not in Settings.cSg_List:
                        Settings.cSg_List.append(b)
                        list(set(Settings.cSg_List))
                
                if b != c and (b in Settings.cSg_List):
                    del Settings.cSg_List[b]
                    

                if Settings.매수 == False and self.balance_dict == {} and Settings.bas_min <= b <= Settings.bas_max:
                    if Settings.추세 == 'CALL':
                        Settings.매수 = True
                        Kiwoom.request_orderFO(self,'신규매수',oCode,Settings.수량,e)

                    elif self.반대매수 == 2:
                        Settings.매수 = True
                        self.반대매수 = 0
                        Kiwoom.request_orderFO(self,'신규매수',oCode,Settings.수량,e)


            if oCode[0:1] == '3': # UPDATE PUT PRICE
                pIdx = self.pStr.index(oCode) + 3
                widgets.tableWidget.setItem(pIdx, 5, QTableWidgetItem('%s'%a))
                widgets.tableWidget.setItem(pIdx, 6, QTableWidgetItem('%s'%b))
                widgets.tableWidget.setItem(pIdx, 7, QTableWidgetItem('%s'%c))
                widgets.tableWidget.setItem(pIdx, 8, QTableWidgetItem('%s'%d))

                if b == c:
                    widgets.tableWidget.item(pIdx, 6).setBackground(QBrush(QColor(214,230,245)))
                    widgets.tableWidget.item(pIdx, 7).setBackground(QBrush(QColor(214,230,245)))

                    if b not in Settings.pSg_List:
                        Settings.pSg_List.append(b)
                        list(set(Settings.pSg_List))
                
                if b != c and (b in Settings.pSg_List):
                    del Settings.pSg_List[b]
                    

                if Settings.추세 == 'PUT' and self.balance_dict == {} and Settings.bas_min <= b <= Settings.bas_max:
                    if Settings.매수 == False:
                        Settings.매수 = True
                        Kiwoom.request_orderFO(self,'신규매수',oCode,Settings.수량,e)

                    elif self.반대매수 == 3:
                        Settings.매수 = True
                        self.반대매수 = 0
                        Kiwoom.request_orderFO(self,'신규매수',oCode,Settings.수량,e)


            # # SELL ORDER TERRITORY
            # # ///////////////////////////////////////////////////////////////

            if self.balance_dict != {}:
                if oCode == self.balance_dict['종목코드']:

                    if Settings.매수 == True:
                        buy_price = self.balance_dict['매입단가']
                        주문가능수량 = self.balance_dict['청산가능수량']
                        수익률 = (a - buy_price)/buy_price * 100
                        Settings.형님행사가 = Kiwoom.get_bro_code(self,oCode)

                        # 수익률 조건 매도
                        if (Settings.손절 >= 수익률) or (수익률 >= Settings.이익):
                            Kiwoom.request_orderFO(self,'신규매도',oCode,주문가능수량,'0')


                        # 보유 종목의 형님저가 도달시 매도
                        if a == self.형님저가:
                            Kiwoom.request_orderFO(self,'신규매도',oCode,주문가능수량,'0')


                        # 추세 변동 매도 및 매수
                        if (len(Settings.cSg_List) or len(Settings.pSg_List)) == 0:

                            if oCode[0:1] == '2' and len(Settings.pSg_List) == 0:
                                Kiwoom.request_orderFO(self,'신규매도',oCode,주문가능수량,'0')
                                self.반대매수 = 3

                            if oCode[0:1] == '3' and len(Settings.cSg_List) == 0:
                                Kiwoom.request_orderFO(self,'신규매도',oCode,주문가능수량,'0')  
                                self.반대매수 = 2
                                

                if Settings.형님행사가 == self.balance_dict['종목코드']:
                    self.형님저가 = d


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())