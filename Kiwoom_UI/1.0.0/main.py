import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from modules import *
from widgets import *

widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        S.ENABLE_CUSTOM_TITLE_BAR = True

        # APPLY TEXTS
        self.setWindowTitle('ATS')
        widgets.label_description.setText("ATS APP - Auto Trading System")

        UIFunctions.uiDefinitions(self)

        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        

        # LEFT MENUS
        widgets.Btn_Login.clicked.connect(lambda: Kiwoom.onLogin(self))  # LOGIN

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        AppFunctions.setThemeHack(self,'')

        widgets.stackedWidget.setCurrentWidget(widgets.page_Home)

        self.tr_event_loop = QEventLoop()


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

    # KIWOOM EVENTS
    # ///////////////////////////////////////////////////////////////

    # LOGIN EVENT
    def login_slot(self, err_code):  # 로그인
        if err_code == 0:
            Kiwoom.login_event_loop.exit()
            S.LOGIN_STATE = 1
            AppFunctions.loginState(self,0)
            Kiwoom.regist_Real_Code(self,'4000',"",'215',"0")
            Kiwoom.request_login_info(self)
            Kiwoom.request_balance(self)
            Kiwoom.request_option_price(self)
            Kiwoom.request_days_remaining(self, S.oCode)
            Kiwoom.toggle_RealData_state(self, True)


    # TR EVENTS
    def trdata_slot(self, sScrNo, sRQName, sTrCode, sRecordName, sPrevNext):
        
        if sRQName == "선옵잔고":
            rows = self.kiwoom.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)
            if rows > 0:
                for i in range(rows):
                    Code = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"종목코드")
                    Code = Code.strip()

                    Gubun = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"매도매수구분")
                    Gubun = Gubun.strip()
                    if Gubun == "2":
                        Gubun = "매수"
                    else:
                        Gubun = "매도"

                    Quantity = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"수량")
                    Quantity = int(Quantity.strip())

                    Buy_Price = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"매입단가")
                    Buy_Price = float(Buy_Price.strip()) * 0.001

                    Price = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"현재가")
                    Price = float(Price.strip()) * 0.001

                    청산가능수량 = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"청산가능수량")
                    청산가능수량 = int(청산가능수량.strip())

                    약정금액 = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"약정금액")
                    약정금액 = int(약정금액.strip())

                    평가금액 = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"평가금액")
                    평가금액 = int(평가금액.strip())

                    수익률 = round(((평가금액 - 약정금액) / 약정금액 * 100), 2)

                    S.balance_dict = {"종목코드": Code,"구분": Gubun,"수량": Quantity,"매입단가": Buy_Price,"현재가": Price,"청산가능수량": 청산가능수량,"약정금액": 약정금액,"평가금액": 평가금액,"수익률": 수익률}

                    if (S.손절 >= 수익률) or (수익률 >= S.이익):
                        Kiwoom.request_orderFO(self, "신규매도", Code, 청산가능수량, "0",'잔고매도','')
            else:
                S.balance_dict = {}
                    
            Kiwoom.Disconnect_All_Real(self)
            self.tr_event_loop.exit()

        if sRQName == "선옵잔존일조회":   
            a = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,0,"영업일기준잔존일")
            a = a.strip()
            widgets.tableWidget.setItem(1, 4, QTableWidgetItem("%s일"%a))
            widgets.tableWidget.item(1, 4).setTextAlignment(Qt.AlignHCenter)
            self.tr_event_loop.exit()
            
        if sRQName == "옵션시세조회":
            oAct = []
            oCode = []
            cStr = []
            pStr = []   
            rows = self.kiwoom.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)
            for i in range(rows):
                cCode = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"종목코드")
                cCode = cCode.strip()

                cActPrice = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"행사가")
                cActPrice = float(cActPrice.strip())
                
                cPrice = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"현재가")
                cPrice = float(cPrice.strip().lstrip("+").lstrip("-"))

                cOpen = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"시가")
                cOpen = float(cOpen.strip().lstrip("+").lstrip("-"))

                cHigh = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"고가")
                cHigh = float(cHigh.strip().lstrip("+").lstrip("-"))

                cLow = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"저가")
                cLow = float(cLow.strip().lstrip("+").lstrip("-"))

                cKijoonka = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"기준가")
                cKijoonka = float(cKijoonka.strip().lstrip("+").lstrip("-"))

                # PUT TR DATA
                pCode = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"풋_종목코드")
                pCode = pCode.strip()

                pActPrice = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"풋_행사가")
                pActPrice = float(pActPrice.strip())
                
                pPrice = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"풋_현재가")
                pPrice = float(pPrice.strip().lstrip("+").lstrip("-"))

                pOpen = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"풋_시가")
                pOpen = float(pOpen.strip().lstrip("+").lstrip("-"))

                pHigh = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"풋_고가")
                pHigh = float(pHigh.strip().lstrip("+").lstrip("-"))

                pLow = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"풋_저가")
                pLow = float(pLow.strip().lstrip("+").lstrip("-"))

                pKijoonka = self.kiwoom.dynamicCall("GetCommData(QString,QString,int,QString)",sTrCode,sRQName,i,"풋_기준가")
                pKijoonka = float(pKijoonka.strip().lstrip("+").lstrip("-"))
                
                S.option_table_dict.update({cCode: {"행사가": cActPrice,"현재가": cPrice,"시가": cOpen,"고가": cHigh,"저가": cLow}})
                S.option_table_dict.update({pCode:{"행사가": pActPrice,"현재가": pPrice,"시가": pOpen,"고가": pHigh,"저가": pLow}})

                if ((S.sgMin <= cOpen <= S.sgMax) or (S.sgMin <= pOpen <= S.sgMax)):
                    cStr.append(cCode)
                    pStr.append(pCode)
                    oCode.append(cCode)
                    oCode.append(pCode)
                    oAct.append(cActPrice)
                    oAct.append(pActPrice)
                    oAct = list(set(oAct))
                    oAct.sort()

                    i = len(oAct) + 2
                    widgets.tableWidget.setItem(i, 0, QTableWidgetItem("%s"%cKijoonka))
                    widgets.tableWidget.setItem(i, 1, QTableWidgetItem("%s"%cLow))
                    widgets.tableWidget.setItem(i, 2, QTableWidgetItem("%s"%cHigh))
                    widgets.tableWidget.setItem(i, 3, QTableWidgetItem("%s"%cOpen))
                    widgets.tableWidget.setItem(i, 4, QTableWidgetItem("%s"%cPrice))
                    widgets.tableWidget.setItem(i, 5, QTableWidgetItem("%s"%oAct[-i+2]))
                    widgets.tableWidget.setItem(i, 6, QTableWidgetItem("%s"%pPrice))  
                    widgets.tableWidget.setItem(i, 7, QTableWidgetItem("%s"%pOpen))
                    widgets.tableWidget.setItem(i, 8, QTableWidgetItem("%s"%pHigh))
                    widgets.tableWidget.setItem(i, 9, QTableWidgetItem("%s"%pLow))
                    widgets.tableWidget.setItem(i, 10, QTableWidgetItem("%s"%pKijoonka))   
                    
                    widgets.tableWidget.item(i, 0).setTextAlignment(Qt.AlignHCenter)   
                    widgets.tableWidget.item(i, 5).setTextAlignment(Qt.AlignHCenter)
                    widgets.tableWidget.item(i, 10).setTextAlignment(Qt.AlignHCenter)   
                    S.oCode = cCode

                Kiwoom.Disconnect_All_Real(self)
            cStr.sort(reverse=True)
            pStr.sort(reverse=True)
            oCode.sort(reverse=True)
            self.cStr = ";".join(cStr)
            self.pStr = ";".join(pStr)
            self.oCode = oCode
            self.tr_event_loop.exit()


    # REAL EVENTS
    def chejan_slot(self, Gubun, nItemCnt, sFidList):
        
        if int(Gubun) == 0:  # 접수와 체결
            oCode = self.kiwoom.dynamicCall("GetChejanData(int)", 9001)  # 종목코드

            medosu = self.kiwoom.dynamicCall("GetChejanData(int)", 905)  # 구분
            medosu = medosu.strip().lstrip("+").lstrip("-")

            order_number = self.kiwoom.dynamicCall("GetChejanData(int)", 9203)  # 주문번호
            on = int(order_number)

            order_q = self.kiwoom.dynamicCall("GetChejanData(int)", 900)  # 주문수량
            order_q = int(order_q)

            un_quan = self.kiwoom.dynamicCall("GetChejanData(int)", 902)  # 미체결수량
            un_quan = int(un_quan)

            one_order_number = self.kiwoom.dynamicCall("GetChejanData(int)", 904)  # 원주문번호
            oon = int(one_order_number)

            order_price = self.kiwoom.dynamicCall("GetChejanData(int)", 901)  # 주문가격
            order_price = float(order_price)

            price = self.kiwoom.dynamicCall("GetChejanData(int)", 10)  # Price

            rPrice1 = self.kiwoom.dynamicCall("GetChejanData(int)", 28)  # 최우선 매수호가1

            if un_quan == 0 and (("취소" not in medosu)):
                print("\n%s 체결 | No.%s | %s | 주문가: %s | 주문수량: %s개 | 미체결량: %s개\n"% (medosu, on, oCode, order_price, order_q, un_quan))
                if medosu == '매도':
                    S.balance_dict = {}

                if medosu == "매수":
                    S.balance_dict.update({"종목코드": oCode,"구분": medosu,"수량": order_q,"매입단가": order_price,"Price": price,"청산가능수량": order_q})
                    
            else:
                if medosu != '정정':
                    print("%s 접수 | No.%s | %s | 주문가: %s | 주문수량: %s개 | 미체결량: %s개 | Price: %s"% (medosu, on, oCode, order_price, order_q, un_quan, price))
                    S.correction_order_dict.update({"종목코드": oCode,"구분": medosu,"주문번호": on,"주문수량": order_q,"주문가격": order_price,"미체결수량": un_quan,"원주문번호": oon})



    # REALTYPE DATA EVENT
    def realdata_slot(self, oCode, RealType):
        if RealType == "장시작시간":
            a = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 215)
            print(type(a))
            if a == 0:
                print('장시작전')

            if a == 2:
                print('장종료전')
                
            if a == 3:
                print('장시작')

            if a == 4 or 8:
                print('장종료')

            if a == 9:
                print('장마감')
            

        if RealType == "선물시세":
            a = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 10)  # Price
            a = abs(float(a))

            b = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 16)  # Open
            b = abs(float(b))

            c = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 17)  # High
            c = abs(float(c))

            d = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 18)  # Low
            d = abs(float(d))

            e = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 197)  # KOSPI200
            e = abs(float(e))
            
            widgets.tableWidget.setItem(1, 6, QTableWidgetItem("%s" % a))
            widgets.tableWidget.setItem(1, 7, QTableWidgetItem("%s" % b))
            widgets.tableWidget.setItem(1, 8, QTableWidgetItem("%s" % c))
            widgets.tableWidget.setItem(1, 9, QTableWidgetItem("%s" % d))
            
            widgets.tableWidget.item(1, 6).setTextAlignment(Qt.AlignHCenter)   
            widgets.tableWidget.item(1, 7).setTextAlignment(Qt.AlignHCenter)
            widgets.tableWidget.item(1, 8).setTextAlignment(Qt.AlignHCenter)
            widgets.tableWidget.item(1, 9).setTextAlignment(Qt.AlignHCenter)
                     

        elif RealType == "선물호가잔량":
            a = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 128)  # 순매수잔량
            a = int(a)
        
            widgets.tableWidget.setItem(1, 10, QTableWidgetItem("%s" % a))
            widgets.tableWidget.item(1, 10).setTextAlignment(Qt.AlignHCenter)

            if 0 < a < S.cHoka:
                S.추세 = 'CALL대기'

            if 0 > a > S.pHoka:
                S.추세 = 'PUT대기'
            
            if S.cHoka <= a:
                S.추세 = 'CALL'

            if S.pHoka >= a:
                S.추세 = 'PUT'

            if S.cHoka2 <= a:
                S.추세 = 'CALL추세' 
                
            if S.pHoka2 >= a:
                S.추세 = 'PUT추세'

            widgets.tableWidget.setItem(1, 5, QTableWidgetItem(S.추세))
            widgets.tableWidget.item(1, 5).setTextAlignment(Qt.AlignHCenter)

        elif RealType == "옵션시세":
            a = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 10)  # 현재가
            a = abs(float(a))

            b = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 16)  # 시가
            b = abs(float(b))

            c = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 17)  # 고가
            c = abs(float(c))

            d = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 18)  # 저가
            d = abs(float(d))

            e = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 28)  # (최우선)매수호가
            e = abs(float(e))

            f = self.kiwoom.dynamicCall("GetCommRealData(QString,int)", oCode, 137)  # 호가순잔량
            f = abs(float(f))

            if oCode[0:1] == "2":  # UPDATE CALL PRICE
                if (S.매수 == False) and (S.balance_dict == {}):
                    if (S.bas_min <= e <= S.bas_max) and (a >= b + S.miss_range):
                        if S.추세 == "CALL":
                            S.매수 = True
                            Kiwoom.request_orderFO(self, "신규매수", oCode, S.수량, e, '','')

                        elif S.반대매수 == 2:
                            S.매수 = True
                            S.반대매수 = 0
                            Kiwoom.request_orderFO(self, "신규매수", oCode, S.수량, e, '','')


                i = int(self.oCode.index(oCode)-len(self.oCode)/2) + 3
                widgets.tableWidget.setItem(i, 1, QTableWidgetItem("%s" % d))
                widgets.tableWidget.setItem(i, 2, QTableWidgetItem("%s" % c))
                widgets.tableWidget.setItem(i, 3, QTableWidgetItem("%s" % b))
                widgets.tableWidget.setItem(i, 4, QTableWidgetItem("%s" % a))
                
                widgets.tableWidget.item(i, 1).setTextAlignment(Qt.AlignHCenter)
                widgets.tableWidget.item(i, 2).setTextAlignment(Qt.AlignHCenter)
                widgets.tableWidget.item(i, 3).setTextAlignment(Qt.AlignHCenter)
                widgets.tableWidget.item(i, 4).setTextAlignment(Qt.AlignHCenter)
                
                # 교차 가격 뒤집기
                crscLow = widgets.tableWidget.item(i,1).text()
                crscHigh = float(widgets.tableWidget.item(i,2).text())
                crscOpen = widgets.tableWidget.item(i,3).text()
                crscPrice = widgets.tableWidget.item(i,4).text()
                crspPrice = widgets.tableWidget.item(i,6).text()
                crspOpen = widgets.tableWidget.item(i,7).text()
                crspHigh = float(widgets.tableWidget.item(i,8).text())
                crspLow = widgets.tableWidget.item(i,9).text()

                if crscPrice == crspPrice:
                    cross_dict.update({oCode:crscPrice})
                    widgets.tableWidget.setItem(i, 11, QTableWidgetItem("%s" % crscPrice))   
                    widgets.tableWidget.item(i, 11).setTextAlignment(Qt.AlignHCenter)

                    if (crscHigh > crspHigh) and (crscLow > crspLow) and (crscPrice > crspOpen):
                        widgets.tableWidget.item(i, 11).setForeground(QBrush(QColor(255, 0, 0)))

                    if (crspHigh > crscHigh) and (crscLow < crspLow) and (crspPrice > crscOpen):
                        widgets.tableWidget.item(i, 11).setForeground(QBrush(QColor(144, 238, 144)))

                # 콜 High == 풋 High
                if crscHigh == crspHigh:
                    widgets.tableWidget.item(i, 2).setBackground(QBrush(QColor(255, 85, 85)))
                    widgets.tableWidget.item(i, 8).setBackground(QBrush(QColor(255, 85, 85)))

                # 콜 Low == 풋 Low
                if crscLow == crspLow:
                    widgets.tableWidget.item(i, 1).setBackground(QBrush(QColor(139, 233, 253)))
                    widgets.tableWidget.item(i, 9).setBackground(QBrush(QColor(139, 233, 253)))         
                                    
                # Low High
                if crscLow == crspHigh:
                    widgets.tableWidget.item(i, 1).setBackground(QBrush(QColor(255, 184, 108)))
                    widgets.tableWidget.item(i, 8).setBackground(QBrush(QColor(255, 184, 108)))

                if crscHigh == crspLow:
                    widgets.tableWidget.item(i, 2).setBackground(QBrush(QColor(255, 184, 108)))
                    widgets.tableWidget.item(i, 9).setBackground(QBrush(QColor(255, 184, 108)))
                
                for abc in 주요가List:
                    if (crscHigh - S.miss_range) <= abc <= (crscHigh + S.miss_range):
                        widgets.tableWidget.item(i, 2).setBackground(QBrush(QColor(255, 184, 108)))

                    if (crspHigh - S.miss_range) <= abc <= (crspHigh + S.miss_range):
                        widgets.tableWidget.item(i, 8).setBackground(QBrush(QColor(255, 184, 108)))         


                if oCode not in S.cHigh_dict:
                    S.cHigh_dict.update({oCode:c})

                if oCode not in S.cLow_dict:
                    S.cLow_dict.update({oCode:d})

                else:
                    S.cHigh_dict[oCode] = c
                    S.cLow_dict[oCode] = d

                if S.sgMin <= b <= S.sgMax:
                    if (b == c) or (round(abs(b-c),2) <= S.miss_range):
                        widgets.tableWidget.item(i, 2).setBackground(QBrush(QColor(214, 230, 245)))
                        widgets.tableWidget.item(i, 2).setForeground(QBrush(QColor(0, 0, 0)))
                        widgets.tableWidget.item(i, 3).setBackground(QBrush(QColor(214, 230, 245)))
                        widgets.tableWidget.item(i, 3).setForeground(QBrush(QColor(0, 0, 0)))
                        if oCode not in S.cSg_List:
                            S.cSg_List.append(oCode)

            if oCode[0:1] == "3":  # UPDATE PUT PRICE

                if oCode in self.oCode:
                    i = self.oCode.index(oCode) + 3
                    
                    widgets.tableWidget.setItem(i, 6, QTableWidgetItem("%s" % a))
                    widgets.tableWidget.setItem(i, 7, QTableWidgetItem("%s" % b))
                    widgets.tableWidget.setItem(i, 8, QTableWidgetItem("%s" % c))
                    widgets.tableWidget.setItem(i, 9, QTableWidgetItem("%s" % d))
                    
                    widgets.tableWidget.item(i, 6).setTextAlignment(Qt.AlignHCenter) 
                    widgets.tableWidget.item(i, 7).setTextAlignment(Qt.AlignHCenter)
                    widgets.tableWidget.item(i, 8).setTextAlignment(Qt.AlignHCenter)
                    widgets.tableWidget.item(i, 9).setTextAlignment(Qt.AlignHCenter)                  
                     
                    # 교차 가격 뒤집기
                    crscLow = widgets.tableWidget.item(i,1).text()
                    crscHigh = float(widgets.tableWidget.item(i,2).text())
                    crscOpen = widgets.tableWidget.item(i,3).text()
                    crscPrice = widgets.tableWidget.item(i,4).text()
                    crspPrice = widgets.tableWidget.item(i,6).text()
                    crspOpen = widgets.tableWidget.item(i,7).text()
                    crspHigh = float(widgets.tableWidget.item(i,8).text())
                    crspLow = widgets.tableWidget.item(i,9).text()

                    if crscPrice == crspPrice:
                        cross_dict.update({oCode:crscPrice})
                        widgets.tableWidget.setItem(i, 11, QTableWidgetItem("%s" % crspPrice))
                        widgets.tableWidget.item(i, 11).setTextAlignment(Qt.AlignHCenter)
                        if (crscHigh > crspHigh) and (crscLow > crspLow) and (crscPrice > crspOpen):
                            widgets.tableWidget.item(i, 11).setForeground(QBrush(QColor(255, 0, 0)))

                        if (crspHigh > crscHigh) and (crscLow < crspLow) and (crspPrice > crscOpen):
                            widgets.tableWidget.item(i, 11).setForeground(QBrush(QColor(144, 238, 144)))
                    # 콜 High == 풋 High
                    if crscHigh == crspHigh:
                        widgets.tableWidget.item(i, 2).setBackground(QBrush(QColor(255, 85, 85)))
                        widgets.tableWidget.item(i, 8).setBackground(QBrush(QColor(255, 85, 85)))        
                                            
                    # 콜 Low == 풋 Low
                    if crscLow == crspLow:
                        widgets.tableWidget.item(i, 1).setBackground(QBrush(QColor(139, 233, 253)))
                        widgets.tableWidget.item(i, 9).setBackground(QBrush(QColor(139, 233, 253)))      
                                
                    # Low == High
                    if crscLow == crspHigh:
                        widgets.tableWidget.item(i, 1).setBackground(QBrush(QColor(255, 184, 108)))
                        widgets.tableWidget.item(i, 8).setBackground(QBrush(QColor(255, 184, 108)))

                    if crscHigh == crspLow:
                        widgets.tableWidget.item(i, 2).setBackground(QBrush(QColor(255, 184, 108)))
                        widgets.tableWidget.item(i, 9).setBackground(QBrush(QColor(255, 184, 108)))

                    for abc in 주요가List:
                        if (crscHigh - S.miss_range) <= abc <= (crscHigh + S.miss_range):
                            widgets.tableWidget.item(i, 2).setBackground(QBrush(QColor(255, 184, 108)))

                        if (crspHigh - S.miss_range) <= abc <= (crspHigh + S.miss_range):
                            widgets.tableWidget.item(i, 8).setBackground(QBrush(QColor(255, 184, 108)))          

                    if oCode not in S.pHigh_dict:
                        S.pHigh_dict.update({oCode:c})

                    if oCode not in S.pLow_dict:
                        S.pLow_dict.update({oCode:d})

                    else:
                        S.pHigh_dict[oCode] = c
                        S.pLow_dict[oCode] = d

                    if S.sgMin <= b <= S.sgMax:
                        if (b == c) or (round(abs(b-c),2) <= S.miss_range):
                            widgets.tableWidget.item(i, 7).setBackground(QBrush(QColor(214, 230, 245)))
                            widgets.tableWidget.item(i, 7).setForeground(QBrush(QColor(0, 0, 0)))
                            widgets.tableWidget.item(i, 8).setBackground(QBrush(QColor(214, 230, 245)))
                            widgets.tableWidget.item(i, 8).setForeground(QBrush(QColor(0, 0, 0)))
                            if oCode not in S.pSg_List:
                                S.pSg_List.append(oCode)

                    if (S.추세 == "PUT") and (S.balance_dict == {}):
                        if (S.bas_min <= e <= S.bas_max) and (a >= b + S.miss_range):
                            if S.매수 == False:
                                S.매수 = True
                                Kiwoom.request_orderFO(self, "신규매수", oCode, S.수량, e, '','')

                            elif S.반대매수 == 3:
                                S.매수 = True
                                S.반대매수 = 0
                                Kiwoom.request_orderFO(self, "신규매수", oCode, S.수량, e, '','')

                if d in (S.콜고가풋저가 or S.콜저가풋고가):
                    if S.REAL_STATE == 0:
                        S.REAL_STATE = 1
                        Kiwoom.Disconnect_All_Real(self)
                    else:
                        S.REAL_STATE = 0
                        Kiwoom.Disconnect_All_Real(self)

            # SELL ORDER TERRITORY
            # ///////////////////////////////////////////////////////////////

            if S.balance_dict != {}:
                if oCode == S.balance_dict["종목코드"]:
                    buy_price = float(S.balance_dict["매입단가"])
                    주문가능수량 = int(S.balance_dict["청산가능수량"])

                    # GET BRO CODE AND PRICE
                    if S.형님행사가 == '':
                        S.형님Cnt = 1
                        S.형님행사가 = Kiwoom.get_bro_code(self, oCode)

                    if (a > S.형님저가 > 0.01) and (S.형님행사가 != ''):
                        S.형님Cnt = 2
                        S.형님행사가2 = Kiwoom.get_bro_code(self, S.형님행사가)

                    if S.매수 == True:
                        수익률 = (a - buy_price) / buy_price * 100
                        
                        
                        # 공통 손절 매도 주문
                        if S.손절 >= 수익률:
                            Kiwoom.request_orderFO(self, "신규매도", oCode, 주문가능수량, "0",'손절','')

                        if ((수익률 >= S.이익 and S.형님저가 > 0) or (수익률 >= 20 and a < b)):
                            if oCode[0:1] == '2':
                                # 콜 이익 매도 주문
                                if (S.추세 != 'CALL추세') and (a < S.형님저가):
                                    Kiwoom.request_orderFO(self, "신규매도", oCode, 주문가능수량, "0", '이익','')

                                if S.추세 == 'CALL추세':
                                    if (a > b) and (a >= S.형님저가2):
                                        Kiwoom.request_orderFO(self, "신규매도", oCode, 주문가능수량, "0", '이익','')
                                        
                                    if (a < b) and (S.형님저가 <= a < S.형님저가2):                                       
                                        Kiwoom.request_orderFO(self, "신규매도", oCode, 주문가능수량, "0", '이익','')
                                
                                # 콜 추세 변동 손절 및 매수
                                if len(S.pSg_List) > 0 and len(S.cSg_List) == 0:
                                    S.PB_terms = 1
                                    
                                if S.PB_terms == 1 and len(S.pSg_List) == 0:
                                    S.반대매수 = 2
                                    Kiwoom.request_orderFO(self, "신규매도", oCode, 주문가능수량, "0",'콜변동','')
                        
                            if oCode[0:1] == '3':
                                # 풋 이익 매도 주문
                                if (S.추세 != 'PUT추세') and (a < S.형님저가):
                                    Kiwoom.request_orderFO(self, "신규매도", oCode, 주문가능수량, "0", '이익','')

                                if S.추세 == 'PUT추세':
                                    if (a > b) and (a >= S.형님저가2):
                                        Kiwoom.request_orderFO(self, "신규매도", oCode, 주문가능수량, "0", '이익','')
                                        
                                    if (a < b) and (S.형님저가 <= a < S.형님저가2):                                       
                                        Kiwoom.request_orderFO(self, "신규매도", oCode, 주문가능수량, "0", '이익','')
                                
                                # 추세 변동 손절 및 매수
                                if len(S.cSg_List) > 0 and len(S.pSg_List) == 0:
                                    S.CB_terms = 1

                                if S.CB_terms == 1 and len(S.cSg_List) == 0:
                                    S.반대매수 = 3
                                    Kiwoom.request_orderFO(self, "신규매도", oCode, 주문가능수량, "0",'풋변동','')


                    elif (S.매수 == False) and (주문가능수량 > 0):
                        S.매수 = True
                    if buy_price == 0:
                        S.balance_dict = {}

                if oCode == S.형님행사가:
                    S.형님저가 = d

                if oCode == S.형님행사가2:
                    S.형님저가2 = d

            if S.balance_dict == {} and S.correction_order_dict != {}:
                cod = S.correction_order_dict
                종목코드 = cod['종목코드']
                주문수량 = cod['주문수량']
                미체결수량 = cod['미체결수량'] 
                if oCode == 종목코드 and 미체결수량 == 주문수량:
                    주문가격 = cod['주문가격']
                    가격차이 = round(e - 주문가격,3)
                    if e > 가격차이:
                        주문번호 = cod['주문번호']
                        원주문번호 = cod['원주문번호']
                        Kiwoom.request_orderFO(self,'정정',종목코드,미체결수량,e,'',주문번호)
                        
                        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    main = MainWindow()
    sys.exit(app.exec_())