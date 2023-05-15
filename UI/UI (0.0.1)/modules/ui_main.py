# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainBblwmH.ui'
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
        MainWindow.resize(1055, 720)
        MainWindow.setMinimumSize(QSize(1055, 720))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(18, 18, 18);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Left_Box = QFrame(self.centralwidget)
        self.Left_Box.setObjectName(u"Left_Box")
        self.Left_Box.setMinimumSize(QSize(70, 0))
        self.Left_Box.setMaximumSize(QSize(70, 16777215))
        self.Left_Box.setFrameShape(QFrame.NoFrame)
        self.Left_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Left_Box)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Logo_Box = QFrame(self.Left_Box)
        self.Logo_Box.setObjectName(u"Logo_Box")
        self.Logo_Box.setMinimumSize(QSize(0, 0))
        self.Logo_Box.setMaximumSize(QSize(16777215, 60))
        self.Logo_Box.setFrameShape(QFrame.NoFrame)
        self.Logo_Box.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.Logo_Box)

        self.leftMenuFrame = QFrame(self.Left_Box)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 50))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.toggleBox)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setMinimumSize(QSize(0, 50))
        self.Btn_Toggle.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_Toggle.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_17.addWidget(self.Btn_Toggle)


        self.verticalLayout_12.addWidget(self.toggleBox)

        self.frame_Menu = QFrame(self.leftMenuFrame)
        self.frame_Menu.setObjectName(u"frame_Menu")
        self.frame_Menu.setFrameShape(QFrame.NoFrame)
        self.frame_Menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_Menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Btn_Home = QPushButton(self.frame_Menu)
        self.Btn_Home.setObjectName(u"Btn_Home")
        sizePolicy.setHeightForWidth(self.Btn_Home.sizePolicy().hasHeightForWidth())
        self.Btn_Home.setSizePolicy(sizePolicy)
        self.Btn_Home.setMinimumSize(QSize(0, 50))
        self.Btn_Home.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_Home.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_5.addWidget(self.Btn_Home)

        self.Btn_Dde = QPushButton(self.frame_Menu)
        self.Btn_Dde.setObjectName(u"Btn_Dde")
        sizePolicy.setHeightForWidth(self.Btn_Dde.sizePolicy().hasHeightForWidth())
        self.Btn_Dde.setSizePolicy(sizePolicy)
        self.Btn_Dde.setMinimumSize(QSize(0, 50))
        self.Btn_Dde.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_Dde.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_5.addWidget(self.Btn_Dde)

        self.Btn_Etc = QPushButton(self.frame_Menu)
        self.Btn_Etc.setObjectName(u"Btn_Etc")
        sizePolicy.setHeightForWidth(self.Btn_Etc.sizePolicy().hasHeightForWidth())
        self.Btn_Etc.setSizePolicy(sizePolicy)
        self.Btn_Etc.setMinimumSize(QSize(0, 50))
        self.Btn_Etc.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_Etc.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_5.addWidget(self.Btn_Etc)

        self.Btn_Etc_2 = QPushButton(self.frame_Menu)
        self.Btn_Etc_2.setObjectName(u"Btn_Etc_2")
        sizePolicy.setHeightForWidth(self.Btn_Etc_2.sizePolicy().hasHeightForWidth())
        self.Btn_Etc_2.setSizePolicy(sizePolicy)
        self.Btn_Etc_2.setMinimumSize(QSize(0, 50))
        self.Btn_Etc_2.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_Etc_2.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_5.addWidget(self.Btn_Etc_2)

        self.Btn_Etc_3 = QPushButton(self.frame_Menu)
        self.Btn_Etc_3.setObjectName(u"Btn_Etc_3")
        sizePolicy.setHeightForWidth(self.Btn_Etc_3.sizePolicy().hasHeightForWidth())
        self.Btn_Etc_3.setSizePolicy(sizePolicy)
        self.Btn_Etc_3.setMinimumSize(QSize(0, 50))
        self.Btn_Etc_3.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_Etc_3.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_5.addWidget(self.Btn_Etc_3)


        self.verticalLayout_12.addWidget(self.frame_Menu, 0, Qt.AlignTop)

        self.Settings_Box = QFrame(self.leftMenuFrame)
        self.Settings_Box.setObjectName(u"Settings_Box")
        self.Settings_Box.setMaximumSize(QSize(16777215, 16777215))
        self.Settings_Box.setFrameShape(QFrame.NoFrame)
        self.Settings_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Settings_Box)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Btn_Settings = QPushButton(self.Settings_Box)
        self.Btn_Settings.setObjectName(u"Btn_Settings")
        sizePolicy.setHeightForWidth(self.Btn_Settings.sizePolicy().hasHeightForWidth())
        self.Btn_Settings.setSizePolicy(sizePolicy)
        self.Btn_Settings.setMinimumSize(QSize(0, 50))
        self.Btn_Settings.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_Settings.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_11.addWidget(self.Btn_Settings)


        self.verticalLayout_12.addWidget(self.Settings_Box, 0, Qt.AlignBottom)


        self.verticalLayout_4.addWidget(self.leftMenuFrame)


        self.horizontalLayout.addWidget(self.Left_Box)

        self.extraLeftBox = QFrame(self.centralwidget)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.extraLeftBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.extraLeft_Box_Top = QFrame(self.extraLeftBox)
        self.extraLeft_Box_Top.setObjectName(u"extraLeft_Box_Top")
        self.extraLeft_Box_Top.setMaximumSize(QSize(16777215, 60))
        self.extraLeft_Box_Top.setStyleSheet(u"background-color: rgb(189, 147, 249);\n"
"color: rgb(255, 255, 255);")
        self.extraLeft_Box_Top.setFrameShape(QFrame.NoFrame)
        self.extraLeft_Box_Top.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.extraLeft_Box_Top)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.Btn_Close_extraLeftBox = QPushButton(self.extraLeft_Box_Top)
        self.Btn_Close_extraLeftBox.setObjectName(u"Btn_Close_extraLeftBox")
        self.Btn_Close_extraLeftBox.setMinimumSize(QSize(30, 30))
        self.Btn_Close_extraLeftBox.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.Btn_Close_extraLeftBox, 0, 2, 1, 1)

        self.label_3 = QLabel(self.extraLeft_Box_Top)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label = QLabel(self.extraLeft_Box_Top)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.extraLeft_Box_Top)

        self.extraLeftContent = QFrame(self.extraLeftBox)
        self.extraLeftContent.setObjectName(u"extraLeftContent")
        self.extraLeftContent.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.extraLeftContent.setFrameShape(QFrame.NoFrame)
        self.extraLeftContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.extraLeftContent)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.extraLeftMain_1 = QFrame(self.extraLeftContent)
        self.extraLeftMain_1.setObjectName(u"extraLeftMain_1")
        self.extraLeftMain_1.setFrameShape(QFrame.NoFrame)
        self.extraLeftMain_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.extraLeftMain_1)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Btn_VideoPlayer = QPushButton(self.extraLeftMain_1)
        self.Btn_VideoPlayer.setObjectName(u"Btn_VideoPlayer")
        self.Btn_VideoPlayer.setMinimumSize(QSize(0, 50))
        self.Btn_VideoPlayer.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_VideoPlayer.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_19.addWidget(self.Btn_VideoPlayer)

        self.Btn_File = QPushButton(self.extraLeftMain_1)
        self.Btn_File.setObjectName(u"Btn_File")
        self.Btn_File.setMinimumSize(QSize(0, 50))
        self.Btn_File.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_File.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_19.addWidget(self.Btn_File)

        self.Btn_Info = QPushButton(self.extraLeftMain_1)
        self.Btn_Info.setObjectName(u"Btn_Info")
        self.Btn_Info.setMinimumSize(QSize(0, 50))
        self.Btn_Info.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_Info.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_19.addWidget(self.Btn_Info)


        self.verticalLayout_18.addWidget(self.extraLeftMain_1, 0, Qt.AlignTop)

        self.extraLeftMain_2 = QFrame(self.extraLeftContent)
        self.extraLeftMain_2.setObjectName(u"extraLeftMain_2")
        self.extraLeftMain_2.setFrameShape(QFrame.NoFrame)
        self.extraLeftMain_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_18.addWidget(self.extraLeftMain_2)


        self.verticalLayout_6.addWidget(self.extraLeftContent)


        self.horizontalLayout.addWidget(self.extraLeftBox)

        self.Main_Container = QFrame(self.centralwidget)
        self.Main_Container.setObjectName(u"Main_Container")
        self.Main_Container.setStyleSheet(u"")
        self.Main_Container.setFrameShape(QFrame.NoFrame)
        self.Main_Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main_Container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Box = QFrame(self.Main_Container)
        self.Top_Box.setObjectName(u"Top_Box")
        self.Top_Box.setMaximumSize(QSize(16777215, 60))
        self.Top_Box.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Top_Box.setFrameShape(QFrame.NoFrame)
        self.Top_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Top_Box)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TopBar1 = QFrame(self.Top_Box)
        self.TopBar1.setObjectName(u"TopBar1")
        self.TopBar1.setMaximumSize(QSize(16777215, 30))
        self.TopBar1.setStyleSheet(u"")
        self.TopBar1.setFrameShape(QFrame.NoFrame)
        self.TopBar1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.TopBar1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TopBar1_Left = QFrame(self.TopBar1)
        self.TopBar1_Left.setObjectName(u"TopBar1_Left")
        self.TopBar1_Left.setFrameShape(QFrame.NoFrame)
        self.TopBar1_Left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.TopBar1_Left)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.TopBar_Left_Label = QLabel(self.TopBar1_Left)
        self.TopBar_Left_Label.setObjectName(u"TopBar_Left_Label")
        self.TopBar_Left_Label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.TopBar_Left_Label)


        self.horizontalLayout_2.addWidget(self.TopBar1_Left)

        self.TopBar1_Right = QFrame(self.TopBar1)
        self.TopBar1_Right.setObjectName(u"TopBar1_Right")
        self.TopBar1_Right.setMaximumSize(QSize(180, 16777215))
        self.TopBar1_Right.setFrameShape(QFrame.NoFrame)
        self.TopBar1_Right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.TopBar1_Right)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Btn_OpenLoginBox = QPushButton(self.TopBar1_Right)
        self.Btn_OpenLoginBox.setObjectName(u"Btn_OpenLoginBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Btn_OpenLoginBox.sizePolicy().hasHeightForWidth())
        self.Btn_OpenLoginBox.setSizePolicy(sizePolicy1)
        self.Btn_OpenLoginBox.setMinimumSize(QSize(45, 30))
        self.Btn_OpenLoginBox.setMaximumSize(QSize(45, 30))
        self.Btn_OpenLoginBox.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.horizontalLayout_3.addWidget(self.Btn_OpenLoginBox)

        self.Btn_Minimize = QPushButton(self.TopBar1_Right)
        self.Btn_Minimize.setObjectName(u"Btn_Minimize")
        sizePolicy1.setHeightForWidth(self.Btn_Minimize.sizePolicy().hasHeightForWidth())
        self.Btn_Minimize.setSizePolicy(sizePolicy1)
        self.Btn_Minimize.setMinimumSize(QSize(45, 30))
        self.Btn_Minimize.setMaximumSize(QSize(45, 30))
        self.Btn_Minimize.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.horizontalLayout_3.addWidget(self.Btn_Minimize)

        self.Btn_MaximizeRestore = QPushButton(self.TopBar1_Right)
        self.Btn_MaximizeRestore.setObjectName(u"Btn_MaximizeRestore")
        sizePolicy1.setHeightForWidth(self.Btn_MaximizeRestore.sizePolicy().hasHeightForWidth())
        self.Btn_MaximizeRestore.setSizePolicy(sizePolicy1)
        self.Btn_MaximizeRestore.setMinimumSize(QSize(45, 30))
        self.Btn_MaximizeRestore.setMaximumSize(QSize(45, 30))
        self.Btn_MaximizeRestore.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.horizontalLayout_3.addWidget(self.Btn_MaximizeRestore)

        self.Btn_Close = QPushButton(self.TopBar1_Right)
        self.Btn_Close.setObjectName(u"Btn_Close")
        sizePolicy1.setHeightForWidth(self.Btn_Close.sizePolicy().hasHeightForWidth())
        self.Btn_Close.setSizePolicy(sizePolicy1)
        self.Btn_Close.setMinimumSize(QSize(45, 30))
        self.Btn_Close.setMaximumSize(QSize(45, 30))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.Btn_Close.setFont(font1)
        self.Btn_Close.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(255,0,0,255)}")

        self.horizontalLayout_3.addWidget(self.Btn_Close)


        self.horizontalLayout_2.addWidget(self.TopBar1_Right)


        self.verticalLayout_2.addWidget(self.TopBar1)

        self.Top_Bar2 = QFrame(self.Top_Box)
        self.Top_Bar2.setObjectName(u"Top_Bar2")
        self.Top_Bar2.setMinimumSize(QSize(0, 30))
        self.Top_Bar2.setMaximumSize(QSize(16777215, 16777215))
        self.Top_Bar2.setStyleSheet(u"")
        self.Top_Bar2.setFrameShape(QFrame.NoFrame)
        self.Top_Bar2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.Top_Bar2)


        self.verticalLayout.addWidget(self.Top_Box)

        self.Main_Box = QFrame(self.Main_Container)
        self.Main_Box.setObjectName(u"Main_Box")
        self.Main_Box.setFrameShape(QFrame.NoFrame)
        self.Main_Box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Main_Box)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Pages_Widget_Frame = QFrame(self.Main_Box)
        self.Pages_Widget_Frame.setObjectName(u"Pages_Widget_Frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Pages_Widget_Frame.sizePolicy().hasHeightForWidth())
        self.Pages_Widget_Frame.setSizePolicy(sizePolicy2)
        self.Pages_Widget_Frame.setStyleSheet(u"")
        self.Pages_Widget_Frame.setFrameShape(QFrame.NoFrame)
        self.Pages_Widget_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Pages_Widget_Frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Pages_Frame = QFrame(self.Pages_Widget_Frame)
        self.Pages_Frame.setObjectName(u"Pages_Frame")
        sizePolicy2.setHeightForWidth(self.Pages_Frame.sizePolicy().hasHeightForWidth())
        self.Pages_Frame.setSizePolicy(sizePolicy2)
        self.Pages_Frame.setFrameShape(QFrame.NoFrame)
        self.Pages_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Pages_Frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Pages_Widget = QStackedWidget(self.Pages_Frame)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        sizePolicy2.setHeightForWidth(self.Pages_Widget.sizePolicy().hasHeightForWidth())
        self.Pages_Widget.setSizePolicy(sizePolicy2)
        self.Pages_Widget.setStyleSheet(u"background-color: rgb(124, 124, 124);")
        self.page_Home = QWidget()
        self.page_Home.setObjectName(u"page_Home")
        self.Pages_Widget.addWidget(self.page_Home)
        self.page_Dde = QWidget()
        self.page_Dde.setObjectName(u"page_Dde")
        sizePolicy2.setHeightForWidth(self.page_Dde.sizePolicy().hasHeightForWidth())
        self.page_Dde.setSizePolicy(sizePolicy2)
        self.verticalLayout_9 = QVBoxLayout(self.page_Dde)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_DDE = QFrame(self.page_Dde)
        self.frame_DDE.setObjectName(u"frame_DDE")
        sizePolicy2.setHeightForWidth(self.frame_DDE.sizePolicy().hasHeightForWidth())
        self.frame_DDE.setSizePolicy(sizePolicy2)
        self.frame_DDE.setFrameShape(QFrame.NoFrame)
        self.frame_DDE.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_DDE)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_DDE)
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
        if (self.tableWidget.rowCount() < 20):
            self.tableWidget.setRowCount(20)
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
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, __qtablewidgetitem28)
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font2);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font2);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font2);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font2);
        self.tableWidget.setItem(0, 3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font2);
        self.tableWidget.setItem(0, 4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font2);
        self.tableWidget.setItem(0, 5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font2);
        self.tableWidget.setItem(0, 6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font2);
        self.tableWidget.setItem(0, 7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(1, 6, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font2);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font2);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font2);
        self.tableWidget.setItem(2, 2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font2);
        self.tableWidget.setItem(2, 3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font2);
        self.tableWidget.setItem(2, 4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font2);
        self.tableWidget.setItem(2, 5, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setFont(font2);
        self.tableWidget.setItem(2, 6, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font2);
        self.tableWidget.setItem(2, 7, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font2);
        self.tableWidget.setItem(2, 8, __qtablewidgetitem46)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setMinimumSize(QSize(1050, 0))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.tableWidget.setFont(font3)
        self.tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(83)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_10.addWidget(self.tableWidget)


        self.verticalLayout_9.addWidget(self.frame_DDE)

        self.Pages_Widget.addWidget(self.page_Dde)
        self.page_Etc = QWidget()
        self.page_Etc.setObjectName(u"page_Etc")
        self.Pages_Widget.addWidget(self.page_Etc)
        self.page_VideoPlayer = QWidget()
        self.page_VideoPlayer.setObjectName(u"page_VideoPlayer")
        self.verticalLayout_20 = QVBoxLayout(self.page_VideoPlayer)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.VideoPlayerBox = QFrame(self.page_VideoPlayer)
        self.VideoPlayerBox.setObjectName(u"VideoPlayerBox")
        self.VideoPlayerBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.VideoPlayerBox.setFrameShape(QFrame.NoFrame)
        self.VideoPlayerBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.VideoPlayerBox)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Video_Main = QFrame(self.VideoPlayerBox)
        self.Video_Main.setObjectName(u"Video_Main")
        self.Video_Main.setFrameShape(QFrame.NoFrame)
        self.Video_Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.Video_Main)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.Video = QWidget(self.Video_Main)
        self.Video.setObjectName(u"Video")

        self.verticalLayout_22.addWidget(self.Video)


        self.verticalLayout_21.addWidget(self.Video_Main)

        self.Video_MenuBox = QFrame(self.VideoPlayerBox)
        self.Video_MenuBox.setObjectName(u"Video_MenuBox")
        self.Video_MenuBox.setMaximumSize(QSize(16777215, 60))
        self.Video_MenuBox.setStyleSheet(u"background-color: rgb(18, 18, 18);\n"
"color: rgb(255, 255, 255);")
        self.Video_MenuBox.setFrameShape(QFrame.NoFrame)
        self.Video_MenuBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.Video_MenuBox)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.VideoMenuBox1 = QFrame(self.Video_MenuBox)
        self.VideoMenuBox1.setObjectName(u"VideoMenuBox1")
        self.VideoMenuBox1.setMinimumSize(QSize(0, 0))
        self.VideoMenuBox1.setMaximumSize(QSize(16777215, 25))
        self.VideoMenuBox1.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"")
        self.VideoMenuBox1.setFrameShape(QFrame.NoFrame)
        self.VideoMenuBox1.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.VideoMenuBox1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.VideoLengthBar = QSlider(self.VideoMenuBox1)
        self.VideoLengthBar.setObjectName(u"VideoLengthBar")
        self.VideoLengthBar.setMaximum(100)
        self.VideoLengthBar.setValue(0)
        self.VideoLengthBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.VideoLengthBar, 0, 0, 1, 1)

        self.label_2 = QLabel(self.VideoMenuBox1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.VolumeBar = QSlider(self.VideoMenuBox1)
        self.VolumeBar.setObjectName(u"VolumeBar")
        self.VolumeBar.setMaximumSize(QSize(100, 16777215))
        self.VolumeBar.setMaximum(100)
        self.VolumeBar.setValue(0)
        self.VolumeBar.setSliderPosition(0)
        self.VolumeBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.VolumeBar, 0, 2, 1, 1)


        self.verticalLayout_23.addWidget(self.VideoMenuBox1)

        self.VideoMenuBox2 = QFrame(self.Video_MenuBox)
        self.VideoMenuBox2.setObjectName(u"VideoMenuBox2")
        self.VideoMenuBox2.setMinimumSize(QSize(0, 0))
        self.VideoMenuBox2.setMaximumSize(QSize(16777215, 35))
        self.VideoMenuBox2.setStyleSheet(u"")
        self.VideoMenuBox2.setFrameShape(QFrame.NoFrame)
        self.VideoMenuBox2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.VideoMenuBox2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.VideoMenus1 = QFrame(self.VideoMenuBox2)
        self.VideoMenus1.setObjectName(u"VideoMenus1")
        self.VideoMenus1.setMaximumSize(QSize(350, 16777215))
        self.VideoMenus1.setStyleSheet(u"")
        self.VideoMenus1.setFrameShape(QFrame.NoFrame)
        self.VideoMenus1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.VideoMenus1)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Btn_PlayPause = QPushButton(self.VideoMenus1)
        self.Btn_PlayPause.setObjectName(u"Btn_PlayPause")
        self.Btn_PlayPause.setMinimumSize(QSize(0, 35))
        self.Btn_PlayPause.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_PlayPause.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.horizontalLayout_8.addWidget(self.Btn_PlayPause)

        self.Btn_VideoStop = QPushButton(self.VideoMenus1)
        self.Btn_VideoStop.setObjectName(u"Btn_VideoStop")
        self.Btn_VideoStop.setMinimumSize(QSize(0, 35))
        self.Btn_VideoStop.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.horizontalLayout_8.addWidget(self.Btn_VideoStop)

        self.Btn_PreviousVideo = QPushButton(self.VideoMenus1)
        self.Btn_PreviousVideo.setObjectName(u"Btn_PreviousVideo")
        self.Btn_PreviousVideo.setMinimumSize(QSize(0, 35))
        self.Btn_PreviousVideo.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.horizontalLayout_8.addWidget(self.Btn_PreviousVideo)

        self.Btn_PrecedingVideo = QPushButton(self.VideoMenus1)
        self.Btn_PrecedingVideo.setObjectName(u"Btn_PrecedingVideo")
        self.Btn_PrecedingVideo.setMinimumSize(QSize(0, 35))
        self.Btn_PrecedingVideo.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.horizontalLayout_8.addWidget(self.Btn_PrecedingVideo)

        self.Btn_OpenVideoFile = QPushButton(self.VideoMenus1)
        self.Btn_OpenVideoFile.setObjectName(u"Btn_OpenVideoFile")
        self.Btn_OpenVideoFile.setMinimumSize(QSize(0, 35))
        self.Btn_OpenVideoFile.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.horizontalLayout_8.addWidget(self.Btn_OpenVideoFile)


        self.horizontalLayout_7.addWidget(self.VideoMenus1)

        self.VideoLabel = QFrame(self.VideoMenuBox2)
        self.VideoLabel.setObjectName(u"VideoLabel")
        self.VideoLabel.setMinimumSize(QSize(0, 0))
        self.VideoLabel.setFrameShape(QFrame.NoFrame)
        self.VideoLabel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.VideoLabel)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(10, 0, 0, 0)
        self.label_4 = QLabel(self.VideoLabel)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.label_4)


        self.horizontalLayout_7.addWidget(self.VideoLabel)

        self.VideoFileListBox = QFrame(self.VideoMenuBox2)
        self.VideoFileListBox.setObjectName(u"VideoFileListBox")
        self.VideoFileListBox.setMaximumSize(QSize(35, 16777215))
        self.VideoFileListBox.setFrameShape(QFrame.NoFrame)
        self.VideoFileListBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.VideoFileListBox)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.Btn_FileList = QPushButton(self.VideoFileListBox)
        self.Btn_FileList.setObjectName(u"Btn_FileList")
        self.Btn_FileList.setMinimumSize(QSize(0, 35))
        self.Btn_FileList.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_24.addWidget(self.Btn_FileList)


        self.horizontalLayout_7.addWidget(self.VideoFileListBox)


        self.verticalLayout_23.addWidget(self.VideoMenuBox2)


        self.verticalLayout_21.addWidget(self.Video_MenuBox)


        self.verticalLayout_20.addWidget(self.VideoPlayerBox)

        self.Pages_Widget.addWidget(self.page_VideoPlayer)

        self.verticalLayout_8.addWidget(self.Pages_Widget)


        self.verticalLayout_7.addWidget(self.Pages_Frame)

        self.BottomBar = QFrame(self.Pages_Widget_Frame)
        self.BottomBar.setObjectName(u"BottomBar")
        self.BottomBar.setMinimumSize(QSize(0, 30))
        self.BottomBar.setMaximumSize(QSize(16777215, 16777215))
        self.BottomBar.setStyleSheet(u"background-color: rgb(18, 18, 18);")
        self.BottomBar.setFrameShape(QFrame.NoFrame)
        self.BottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.BottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.BottomLeftBar = QFrame(self.BottomBar)
        self.BottomLeftBar.setObjectName(u"BottomLeftBar")
        self.BottomLeftBar.setFrameShape(QFrame.NoFrame)
        self.BottomLeftBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.BottomLeftBar)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.LoginStateLabel = QLabel(self.BottomLeftBar)
        self.LoginStateLabel.setObjectName(u"LoginStateLabel")
        self.LoginStateLabel.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_14.addWidget(self.LoginStateLabel)


        self.horizontalLayout_5.addWidget(self.BottomLeftBar, 0, Qt.AlignLeft)

        self.BottomRightBar = QFrame(self.BottomBar)
        self.BottomRightBar.setObjectName(u"BottomRightBar")
        self.BottomRightBar.setFrameShape(QFrame.NoFrame)
        self.BottomRightBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.BottomRightBar)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, -1, 0)
        self.VersionInfoLabel = QLabel(self.BottomRightBar)
        self.VersionInfoLabel.setObjectName(u"VersionInfoLabel")
        self.VersionInfoLabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.VersionInfoLabel)


        self.horizontalLayout_5.addWidget(self.BottomRightBar, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.BottomBar)


        self.horizontalLayout_4.addWidget(self.Pages_Widget_Frame)

        self.Login_Box = QFrame(self.Main_Box)
        self.Login_Box.setObjectName(u"Login_Box")
        sizePolicy2.setHeightForWidth(self.Login_Box.sizePolicy().hasHeightForWidth())
        self.Login_Box.setSizePolicy(sizePolicy2)
        self.Login_Box.setMinimumSize(QSize(0, 0))
        self.Login_Box.setMaximumSize(QSize(0, 16777215))
        self.Login_Box.setFrameShape(QFrame.NoFrame)
        self.Login_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.Login_Box)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Login_Menu_Box = QFrame(self.Login_Box)
        self.Login_Menu_Box.setObjectName(u"Login_Menu_Box")
        self.Login_Menu_Box.setFrameShape(QFrame.NoFrame)
        self.Login_Menu_Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Login_Menu_Box)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Btn_Login = QPushButton(self.Login_Menu_Box)
        self.Btn_Login.setObjectName(u"Btn_Login")
        self.Btn_Login.setMinimumSize(QSize(0, 50))
        self.Btn_Login.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.Btn_Login.setFont(font4)
        self.Btn_Login.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_16.addWidget(self.Btn_Login)

        self.Btn_RealData = QPushButton(self.Login_Menu_Box)
        self.Btn_RealData.setObjectName(u"Btn_RealData")
        self.Btn_RealData.setMinimumSize(QSize(0, 50))
        self.Btn_RealData.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_RealData.setFont(font4)
        self.Btn_RealData.setStyleSheet(u"QPushButton {color: rgb(255, 255, 255);border: 0px solid}\n"
"QPushButton:hover {background-color: rgba(105,115,112,150)}")

        self.verticalLayout_16.addWidget(self.Btn_RealData)


        self.verticalLayout_13.addWidget(self.Login_Menu_Box, 0, Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.Login_Box)


        self.verticalLayout.addWidget(self.Main_Box)


        self.horizontalLayout.addWidget(self.Main_Container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.Btn_Home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.Btn_Dde.setText(QCoreApplication.translate("MainWindow", u"DDE", None))
        self.Btn_Etc.setText(QCoreApplication.translate("MainWindow", u"ETC", None))
        self.Btn_Etc_2.setText(QCoreApplication.translate("MainWindow", u"ETC", None))
        self.Btn_Etc_3.setText(QCoreApplication.translate("MainWindow", u"ETC", None))
        self.Btn_Settings.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.Btn_Close_extraLeftBox.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.label.setText("")
        self.Btn_VideoPlayer.setText(QCoreApplication.translate("MainWindow", u"VIDEO PLAYER", None))
        self.Btn_File.setText(QCoreApplication.translate("MainWindow", u"FILE", None))
        self.Btn_Info.setText(QCoreApplication.translate("MainWindow", u"INFO", None))
        self.TopBar_Left_Label.setText("")
        self.Btn_OpenLoginBox.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.Btn_Minimize.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.Btn_MaximizeRestore.setText(QCoreApplication.translate("MainWindow", u"M/R", None))
        self.Btn_Close.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ud589", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ud589", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ud589", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ud589", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ud589", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ud589", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ud589", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ud589", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ud589", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem24 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem25 = self.tableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem26 = self.tableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem27 = self.tableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));
        ___qtablewidgetitem28 = self.tableWidget.verticalHeaderItem(19)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \uc5f4", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem29 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem30 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac00", None));
        ___qtablewidgetitem31 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\uace0\uac00", None));
        ___qtablewidgetitem32 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\uc800\uac00", None));
        ___qtablewidgetitem33 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"KOSPI 200", None));
        ___qtablewidgetitem34 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\ud638\uac00\uc21c\ub9e4\uc218", None));
        ___qtablewidgetitem35 = self.tableWidget.item(0, 7)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uc138", None));
        ___qtablewidgetitem36 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\uc800\uac00", None));
        ___qtablewidgetitem37 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\uace0\uac00", None));
        ___qtablewidgetitem38 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac00", None));
        ___qtablewidgetitem39 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem40 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\ud589\uc0ac\uac00", None));
        ___qtablewidgetitem41 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem42 = self.tableWidget.item(2, 6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac00", None));
        ___qtablewidgetitem43 = self.tableWidget.item(2, 7)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\uace0\uac00", None));
        ___qtablewidgetitem44 = self.tableWidget.item(2, 8)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\uc800\uac00", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.Btn_PlayPause.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.Btn_VideoStop.setText(QCoreApplication.translate("MainWindow", u"\u25a0", None))
        self.Btn_PreviousVideo.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.Btn_PrecedingVideo.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.Btn_OpenVideoFile.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0:00:00 / 0:00:00", None))
        self.Btn_FileList.setText(QCoreApplication.translate("MainWindow", u"FL", None))
        self.LoginStateLabel.setText(QCoreApplication.translate("MainWindow", u"Unconnected", None))
        self.VersionInfoLabel.setText(QCoreApplication.translate("MainWindow", u"0.0.1", None))
        self.Btn_Login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.Btn_RealData.setText(QCoreApplication.translate("MainWindow", u"Connect Real", None))
    # retranslateUi

