# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainENNwVS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 650)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"background-color:#000000; color: #ffffff;")
        self.horizontalLayout_8 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMinimumSize(QSize(0, 0))
        self.bgApp.setMaximumSize(QSize(16777215, 16777215))
        self.bgApp.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid} QPushButton:hover {background-color: #3C4048} QPushButton:pressed {background-color: #BDBDBF;color: #000000}")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.bgApp.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setMaximumSize(QSize(16777215, 16777215))
        self.contentBox.setStyleSheet(u"")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.contentBox.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.contentBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 30))
        self.contentTopBg.setMaximumSize(QSize(16777215, 30))
        self.contentTopBg.setStyleSheet(u"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_description = QLabel(self.contentTopBg)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setStyleSheet(u"#label_description {\n"
"border:none;\n"
"border-left: 15px solid transparent;\n"
"text-align: left;\n"
"\n"
"}")
        self.label_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_description)

        self.contentTop_1 = QFrame(self.contentTopBg)
        self.contentTop_1.setObjectName(u"contentTop_1")
        self.contentTop_1.setMinimumSize(QSize(225, 30))
        self.contentTop_1.setMaximumSize(QSize(225, 30))
        self.contentTop_1.setStyleSheet(u"")
        self.contentTop_1.setFrameShape(QFrame.NoFrame)
        self.contentTop_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.contentTop_1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_Login = QPushButton(self.contentTop_1)
        self.Btn_Login.setObjectName(u"Btn_Login")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Login.sizePolicy().hasHeightForWidth())
        self.Btn_Login.setSizePolicy(sizePolicy)
        self.Btn_Login.setMinimumSize(QSize(90, 30))
        self.Btn_Login.setMaximumSize(QSize(90, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.Btn_Login.setFont(font1)
        self.Btn_Login.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.Btn_Login)

        self.Btn_Minimize = QPushButton(self.contentTop_1)
        self.Btn_Minimize.setObjectName(u"Btn_Minimize")
        self.Btn_Minimize.setMinimumSize(QSize(45, 30))
        self.Btn_Minimize.setMaximumSize(QSize(45, 30))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        self.Btn_Minimize.setFont(font2)
        self.Btn_Minimize.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.Btn_Minimize)

        self.Btn_MaximizeRestore = QPushButton(self.contentTop_1)
        self.Btn_MaximizeRestore.setObjectName(u"Btn_MaximizeRestore")
        self.Btn_MaximizeRestore.setMinimumSize(QSize(45, 30))
        self.Btn_MaximizeRestore.setMaximumSize(QSize(45, 30))
        self.Btn_MaximizeRestore.setFont(font2)
        self.Btn_MaximizeRestore.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.Btn_MaximizeRestore)

        self.Btn_Close = QPushButton(self.contentTop_1)
        self.Btn_Close.setObjectName(u"Btn_Close")
        self.Btn_Close.setMinimumSize(QSize(45, 30))
        self.Btn_Close.setMaximumSize(QSize(45, 30))
        self.Btn_Close.setFont(font2)
        self.Btn_Close.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255); border: 0px solid;} QPushButton:hover {background-color: #E81E25} QPushButton:pressed {background-color: #F05650;}")

        self.horizontalLayout_4.addWidget(self.Btn_Close)


        self.horizontalLayout_5.addWidget(self.contentTop_1)


        self.verticalLayout.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(18, 18, 18);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PageBox = QFrame(self.content)
        self.PageBox.setObjectName(u"PageBox")
        self.PageBox.setStyleSheet(u"background-color:#4D4847")
        self.PageBox.setFrameShape(QFrame.NoFrame)
        self.PageBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.PageBox)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.PageBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.page_Home = QWidget()
        self.page_Home.setObjectName(u"page_Home")
        self.page_Home.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.page_Home)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.PageHomeBox = QFrame(self.page_Home)
        self.PageHomeBox.setObjectName(u"PageHomeBox")
        self.PageHomeBox.setStyleSheet(u"#QTableWidget{\n"
"	Qt.AlignCenter\n"
"\n"
"}")
        self.PageHomeBox.setFrameShape(QFrame.NoFrame)
        self.PageHomeBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.PageHomeBox)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.PageHomeBox)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        if (self.tableWidget.rowCount() < 19):
            self.tableWidget.setRowCount(19)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, __qtablewidgetitem30)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem31.setFont(font3);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFont(font3);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFont(font3);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem34.setFont(font3);
        self.tableWidget.setItem(0, 3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem35.setFont(font3);
        self.tableWidget.setItem(0, 4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem36.setFont(font3);
        self.tableWidget.setItem(0, 5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem37.setFont(font3);
        self.tableWidget.setItem(0, 6, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem38.setFont(font3);
        self.tableWidget.setItem(0, 7, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem39.setFont(font3);
        self.tableWidget.setItem(0, 8, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem40.setFont(font3);
        self.tableWidget.setItem(0, 9, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem41.setFont(font3);
        self.tableWidget.setItem(0, 10, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem42.setFont(font3);
        self.tableWidget.setItem(0, 11, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 6, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 7, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 8, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 9, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 10, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem54.setFont(font3);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem55.setFont(font3);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem56.setFont(font3);
        self.tableWidget.setItem(2, 2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem57.setFont(font3);
        self.tableWidget.setItem(2, 3, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem58.setFont(font3);
        self.tableWidget.setItem(2, 4, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem59.setFont(font3);
        self.tableWidget.setItem(2, 5, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem60.setFont(font3);
        self.tableWidget.setItem(2, 6, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem61.setFont(font3);
        self.tableWidget.setItem(2, 7, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem62.setFont(font3);
        self.tableWidget.setItem(2, 8, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem63.setFont(font3);
        self.tableWidget.setItem(2, 9, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem64.setFont(font3);
        self.tableWidget.setItem(2, 10, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem65.setFont(font3);
        self.tableWidget.setItem(2, 11, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 2, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 3, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 4, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 5, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 6, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 7, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 8, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 9, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 10, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 11, __qtablewidgetitem77)
        self.tableWidget.setObjectName(u"tableWidget")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setWeight(50)
        self.tableWidget.setFont(font4)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_18.addWidget(self.tableWidget)


        self.verticalLayout_16.addWidget(self.PageHomeBox)

        self.stackedWidget.addWidget(self.page_Home)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.PageBox)


        self.verticalLayout_2.addWidget(self.content)

        self.BottomBox = QFrame(self.contentBottom)
        self.BottomBox.setObjectName(u"BottomBox")
        self.BottomBox.setMinimumSize(QSize(0, 30))
        self.BottomBox.setMaximumSize(QSize(16777215, 30))
        self.BottomBox.setFont(font1)
        self.BottomBox.setStyleSheet(u"")
        self.BottomBox.setFrameShape(QFrame.NoFrame)
        self.BottomBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.BottomBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.LoginStateLabel = QLabel(self.BottomBox)
        self.LoginStateLabel.setObjectName(u"LoginStateLabel")
        self.LoginStateLabel.setFont(font2)
        self.LoginStateLabel.setStyleSheet(u"color: #FF0000;")
        self.LoginStateLabel.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.LoginStateLabel)

        self.label_version = QLabel(self.BottomBox)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setFont(font1)
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_version)


        self.verticalLayout_2.addWidget(self.BottomBox)


        self.verticalLayout.addWidget(self.contentBottom)


        self.horizontalLayout.addWidget(self.contentBox)


        self.horizontalLayout_8.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_description.setText("")
        self.Btn_Login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.Btn_Minimize.setText(QCoreApplication.translate("MainWindow", u"__", None))
        self.Btn_MaximizeRestore.setText(QCoreApplication.translate("MainWindow", u"\u25a1", None))
        self.Btn_Close.setText(QCoreApplication.translate("MainWindow", u"X", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\ub9c8\ub514\uac00", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uae30\uc900\uac00", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc800\uac00", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uace0\uac00", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac00", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac00", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\uace0\uac00", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\uc800\uac00", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\uae30\uc900\uac00", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\uad50\ucc28\uac00", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem24 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem25 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem26 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem27 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem28 = self.tableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem29 = self.tableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem30 = self.tableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"18", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem31 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\uc794\uc874\uc77c\uc218", None));
        ___qtablewidgetitem32 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uc138", None));
        ___qtablewidgetitem33 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem34 = self.tableWidget.item(0, 7)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac00", None));
        ___qtablewidgetitem35 = self.tableWidget.item(0, 8)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\uace0\uac00", None));
        ___qtablewidgetitem36 = self.tableWidget.item(0, 9)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\uc800\uac00", None));
        ___qtablewidgetitem37 = self.tableWidget.item(0, 10)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\uc21c\ub9e4\uc218\uc794\ub7c9", None));
        ___qtablewidgetitem38 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\uae30\uc900\uac00", None));
        ___qtablewidgetitem39 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\uc800\uac00", None));
        ___qtablewidgetitem40 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\uace0\uac00", None));
        ___qtablewidgetitem41 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac00", None));
        ___qtablewidgetitem42 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem43 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\ud589\uc0ac\uac00", None));
        ___qtablewidgetitem44 = self.tableWidget.item(2, 6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem45 = self.tableWidget.item(2, 7)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac00", None));
        ___qtablewidgetitem46 = self.tableWidget.item(2, 8)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"\uace0\uac00", None));
        ___qtablewidgetitem47 = self.tableWidget.item(2, 9)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\uc800\uac00", None));
        ___qtablewidgetitem48 = self.tableWidget.item(2, 10)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\uae30\uc900\uac00", None));
        ___qtablewidgetitem49 = self.tableWidget.item(2, 11)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\uad50\ucc28\uac00", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.LoginStateLabel.setText(QCoreApplication.translate("MainWindow", u"Unconnected", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"0.1.0", None))
    # retranslateUi

