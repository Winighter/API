# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maincaddlh.ui'
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
        MainWindow.resize(1108, 714)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"")
        self.vboxLayout = QVBoxLayout(self.styleSheet)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMinimumSize(QSize(782, 0))
        self.bgApp.setMaximumSize(QSize(16777215, 16777215))
        self.bgApp.setStyleSheet(u"background-color: #44475a;")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.bgApp.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuBox = QFrame(self.bgApp)
        self.LeftMenuBox.setObjectName(u"LeftMenuBox")
        self.LeftMenuBox.setMinimumSize(QSize(70, 0))
        self.LeftMenuBox.setMaximumSize(QSize(70, 16777215))
        self.LeftMenuBox.setStyleSheet(u"background-color: #282a36;")
        self.LeftMenuBox.setFrameShape(QFrame.NoFrame)
        self.LeftMenuBox.setFrameShadow(QFrame.Raised)
        self.LeftMenuBox.setLineWidth(1)
        self.verticalLayout_4 = QVBoxLayout(self.LeftMenuBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Logobox = QFrame(self.LeftMenuBox)
        self.Logobox.setObjectName(u"Logobox")
        self.Logobox.setMinimumSize(QSize(0, 65))
        self.Logobox.setMaximumSize(QSize(16777215, 65))
        self.Logobox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Logobox.setFrameShape(QFrame.NoFrame)
        self.Logobox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Logobox)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.Logobox)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"image: url(:/images/images/images/icon.ico);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame)


        self.verticalLayout_4.addWidget(self.Logobox)

        self.MenuBox = QFrame(self.LeftMenuBox)
        self.MenuBox.setObjectName(u"MenuBox")
        self.MenuBox.setFrameShape(QFrame.NoFrame)
        self.MenuBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.MenuBox)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.MenuListBox = QFrame(self.MenuBox)
        self.MenuListBox.setObjectName(u"MenuListBox")
        self.MenuListBox.setFrameShape(QFrame.NoFrame)
        self.MenuListBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.MenuListBox)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.MenuBtnBox = QFrame(self.MenuListBox)
        self.MenuBtnBox.setObjectName(u"MenuBtnBox")
        self.MenuBtnBox.setMinimumSize(QSize(0, 120))
        self.MenuBtnBox.setMaximumSize(QSize(16777215, 120))
        self.MenuBtnBox.setFrameShape(QFrame.StyledPanel)
        self.MenuBtnBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.MenuBtnBox)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 0, 5, 0)
        self.btn_Menu = QPushButton(self.MenuBtnBox)
        self.btn_Menu.setObjectName(u"btn_Menu")
        self.btn_Menu.setMinimumSize(QSize(0, 30))
        self.btn_Menu.setMaximumSize(QSize(16777215, 30))
        self.btn_Menu.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.btn_Menu)

        self.btn_Home = QPushButton(self.MenuBtnBox)
        self.btn_Home.setObjectName(u"btn_Home")
        self.btn_Home.setMinimumSize(QSize(0, 30))
        self.btn_Home.setMaximumSize(QSize(16777215, 30))
        self.btn_Home.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.btn_Home)

        self.btn_DDE = QPushButton(self.MenuBtnBox)
        self.btn_DDE.setObjectName(u"btn_DDE")
        self.btn_DDE.setMinimumSize(QSize(0, 30))
        self.btn_DDE.setMaximumSize(QSize(16777215, 30))
        self.btn_DDE.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.btn_DDE)


        self.verticalLayout_11.addWidget(self.MenuBtnBox)

        self.SpaceBox = QFrame(self.MenuListBox)
        self.SpaceBox.setObjectName(u"SpaceBox")
        self.SpaceBox.setFrameShape(QFrame.StyledPanel)
        self.SpaceBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.SpaceBox)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.btn_tap4 = QPushButton(self.SpaceBox)
        self.btn_tap4.setObjectName(u"btn_tap4")
        self.btn_tap4.setMinimumSize(QSize(0, 30))
        self.btn_tap4.setMaximumSize(QSize(16777215, 30))
        self.btn_tap4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.btn_tap4)

        self.btn_tap5 = QPushButton(self.SpaceBox)
        self.btn_tap5.setObjectName(u"btn_tap5")
        self.btn_tap5.setMinimumSize(QSize(0, 30))
        self.btn_tap5.setMaximumSize(QSize(16777215, 30))
        self.btn_tap5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.btn_tap5)

        self.btn_tap6 = QPushButton(self.SpaceBox)
        self.btn_tap6.setObjectName(u"btn_tap6")
        self.btn_tap6.setMinimumSize(QSize(0, 30))
        self.btn_tap6.setMaximumSize(QSize(16777215, 30))
        self.btn_tap6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.btn_tap6)

        self.btn_tap7 = QPushButton(self.SpaceBox)
        self.btn_tap7.setObjectName(u"btn_tap7")
        self.btn_tap7.setMinimumSize(QSize(0, 30))
        self.btn_tap7.setMaximumSize(QSize(16777215, 30))
        self.btn_tap7.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.btn_tap7)


        self.verticalLayout_11.addWidget(self.SpaceBox)


        self.verticalLayout_9.addWidget(self.MenuListBox)

        self.SettingBox = QFrame(self.MenuBox)
        self.SettingBox.setObjectName(u"SettingBox")
        self.SettingBox.setMinimumSize(QSize(70, 70))
        self.SettingBox.setMaximumSize(QSize(70, 70))
        self.SettingBox.setStyleSheet(u"")
        self.SettingBox.setFrameShape(QFrame.NoFrame)
        self.SettingBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.SettingBox)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_setting = QPushButton(self.SettingBox)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(70, 60))
        self.btn_setting.setMaximumSize(QSize(70, 60))
        self.btn_setting.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_setting.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.btn_setting)


        self.verticalLayout_9.addWidget(self.SettingBox)


        self.verticalLayout_4.addWidget(self.MenuBox)


        self.horizontalLayout.addWidget(self.LeftMenuBox)

        self.LeftHideBox = QFrame(self.bgApp)
        self.LeftHideBox.setObjectName(u"LeftHideBox")
        self.LeftHideBox.setMinimumSize(QSize(0, 0))
        self.LeftHideBox.setMaximumSize(QSize(0, 16777215))
        self.LeftHideBox.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.LeftHideBox.setFrameShape(QFrame.NoFrame)
        self.LeftHideBox.setFrameShadow(QFrame.Raised)
        self.LeftHideBox.setLineWidth(1)
        self.verticalLayout_5 = QVBoxLayout(self.LeftHideBox)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.LeftHideBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 65))
        self.frame_2.setMaximumSize(QSize(16777215, 65))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.extraIcon = QFrame(self.frame_2)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setFrameShape(QFrame.StyledPanel)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.frame_2)
        self.extraLabel.setObjectName(u"extraLabel")

        self.gridLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.frame_2)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")

        self.gridLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.LeftHideBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.LeftHideBox)

        self.MainBox = QFrame(self.bgApp)
        self.MainBox.setObjectName(u"MainBox")
        self.MainBox.setStyleSheet(u"")
        self.MainBox.setFrameShape(QFrame.NoFrame)
        self.MainBox.setFrameShadow(QFrame.Raised)
        self.MainBox.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.MainBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TopBox = QFrame(self.MainBox)
        self.TopBox.setObjectName(u"TopBox")
        self.TopBox.setMinimumSize(QSize(0, 64))
        self.TopBox.setMaximumSize(QSize(16777215, 64))
        self.TopBox.setStyleSheet(u"background-color: #282a36;")
        self.TopBox.setFrameShape(QFrame.NoFrame)
        self.TopBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.TopBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Label_title = QLabel(self.TopBox)
        self.Label_title.setObjectName(u"Label_title")
        self.Label_title.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.Label_title)

        self.RigthTopBox = QFrame(self.TopBox)
        self.RigthTopBox.setObjectName(u"RigthTopBox")
        self.RigthTopBox.setMinimumSize(QSize(170, 0))
        self.RigthTopBox.setMaximumSize(QSize(150, 16777215))
        self.RigthTopBox.setFrameShape(QFrame.NoFrame)
        self.RigthTopBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.RigthTopBox)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_Account = QPushButton(self.RigthTopBox)
        self.btn_Account.setObjectName(u"btn_Account")
        self.btn_Account.setMinimumSize(QSize(33, 33))
        self.btn_Account.setMaximumSize(QSize(33, 33))
        self.btn_Account.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.btn_Account)

        self.btn_Minimize = QPushButton(self.RigthTopBox)
        self.btn_Minimize.setObjectName(u"btn_Minimize")
        self.btn_Minimize.setMinimumSize(QSize(33, 33))
        self.btn_Minimize.setMaximumSize(QSize(33, 33))
        self.btn_Minimize.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.btn_Minimize)

        self.btn_MaximizeRestore = QPushButton(self.RigthTopBox)
        self.btn_MaximizeRestore.setObjectName(u"btn_MaximizeRestore")
        self.btn_MaximizeRestore.setMinimumSize(QSize(33, 33))
        self.btn_MaximizeRestore.setMaximumSize(QSize(33, 33))
        self.btn_MaximizeRestore.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.btn_MaximizeRestore)

        self.btn_Close = QPushButton(self.RigthTopBox)
        self.btn_Close.setObjectName(u"btn_Close")
        self.btn_Close.setMinimumSize(QSize(33, 33))
        self.btn_Close.setMaximumSize(QSize(33, 33))
        self.btn_Close.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.btn_Close)


        self.horizontalLayout_4.addWidget(self.RigthTopBox)


        self.verticalLayout.addWidget(self.TopBox)

        self.Main = QFrame(self.MainBox)
        self.Main.setObjectName(u"Main")
        self.Main.setStyleSheet(u"background-color: rgb(98, 114, 164);")
        self.Main.setFrameShape(QFrame.NoFrame)
        self.Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.Main)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PageBox = QFrame(self.content)
        self.PageBox.setObjectName(u"PageBox")
        self.PageBox.setStyleSheet(u"")
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
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.page_home)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.HomeBox = QFrame(self.page_home)
        self.HomeBox.setObjectName(u"HomeBox")
        self.HomeBox.setFrameShape(QFrame.StyledPanel)
        self.HomeBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.HomeBox)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.textBrowser = QTextBrowser(self.HomeBox)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_15.addWidget(self.textBrowser)


        self.verticalLayout_14.addWidget(self.HomeBox)

        self.stackedWidget.addWidget(self.page_home)
        self.page_DDE = QWidget()
        self.page_DDE.setObjectName(u"page_DDE")
        self.page_DDE.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.page_DDE)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.PageDDEBox = QFrame(self.page_DDE)
        self.PageDDEBox.setObjectName(u"PageDDEBox")
        self.PageDDEBox.setStyleSheet(u"")
        self.PageDDEBox.setFrameShape(QFrame.StyledPanel)
        self.PageDDEBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.PageDDEBox)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(9, -1, -1, -1)
        self.tableWidget = QTableWidget(self.PageDDEBox)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
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
        if (self.tableWidget.rowCount() < 13):
            self.tableWidget.setRowCount(13)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem27)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_18.addWidget(self.tableWidget)


        self.verticalLayout_16.addWidget(self.PageDDEBox)

        self.stackedWidget.addWidget(self.page_DDE)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.PageBox)

        self.RightHideBox = QFrame(self.content)
        self.RightHideBox.setObjectName(u"RightHideBox")
        self.RightHideBox.setMinimumSize(QSize(0, 0))
        self.RightHideBox.setMaximumSize(QSize(0, 16777215))
        self.RightHideBox.setStyleSheet(u"")
        self.RightHideBox.setFrameShape(QFrame.NoFrame)
        self.RightHideBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.RightHideBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.RightHideBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 200))
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_Login = QPushButton(self.frame_4)
        self.btn_Login.setObjectName(u"btn_Login")
        self.btn_Login.setMinimumSize(QSize(0, 45))

        self.verticalLayout_7.addWidget(self.btn_Login)

        self.btn_Con_Real = QPushButton(self.frame_4)
        self.btn_Con_Real.setObjectName(u"btn_Con_Real")
        self.btn_Con_Real.setMinimumSize(QSize(0, 45))

        self.verticalLayout_7.addWidget(self.btn_Con_Real)

        self.btn_Discon_Real = QPushButton(self.frame_4)
        self.btn_Discon_Real.setObjectName(u"btn_Discon_Real")
        self.btn_Discon_Real.setMinimumSize(QSize(0, 45))

        self.verticalLayout_7.addWidget(self.btn_Discon_Real)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.RightHideBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.RightHideBox)


        self.verticalLayout_2.addWidget(self.content)

        self.BottomBox = QFrame(self.Main)
        self.BottomBox.setObjectName(u"BottomBox")
        self.BottomBox.setMinimumSize(QSize(0, 25))
        self.BottomBox.setMaximumSize(QSize(16777215, 25))
        self.BottomBox.setStyleSheet(u"")
        self.BottomBox.setFrameShape(QFrame.NoFrame)
        self.BottomBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.BottomBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_State = QLabel(self.BottomBox)
        self.label_State.setObjectName(u"label_State")
        self.label_State.setStyleSheet(u"color: rgb(255, 85, 85);")
        self.label_State.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.label_State)

        self.label_version = QLabel(self.BottomBox)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_version)

        self.frame_size_grip = QFrame(self.BottomBox)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(25, 0))
        self.frame_size_grip.setMaximumSize(QSize(25, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_size_grip)


        self.verticalLayout_2.addWidget(self.BottomBox)


        self.verticalLayout.addWidget(self.Main)


        self.horizontalLayout.addWidget(self.MainBox)

        self.MainBox.raise_()
        self.LeftMenuBox.raise_()
        self.LeftHideBox.raise_()

        self.vboxLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_Menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_DDE.setText(QCoreApplication.translate("MainWindow", u"DDE", None))
        self.btn_tap4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_tap5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_tap6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_tap7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.extraCloseColumnBtn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Label_title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_Account.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_Minimize.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.btn_MaximizeRestore.setText(QCoreApplication.translate("MainWindow", u"\u3141", None))
        self.btn_Close.setText(QCoreApplication.translate("MainWindow", u"X", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uc800\uac00", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uace0\uac00", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac00", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\ud589\uc0ac\uac00", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac00", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\uace0\uac00", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\uc800\uac00", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"14", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem22 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"asdjiojwqodi", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem24 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"c", None));
        ___qtablewidgetitem25 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"e", None));
        ___qtablewidgetitem26 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"f", None));
        ___qtablewidgetitem27 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"g", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.btn_Login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_Con_Real.setText(QCoreApplication.translate("MainWindow", u" connect real", None))
        self.btn_Discon_Real.setText(QCoreApplication.translate("MainWindow", u"disconnect real ", None))
        self.label_State.setText(QCoreApplication.translate("MainWindow", u"Unconnected", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"0.0.1", None))
    # retranslateUi

