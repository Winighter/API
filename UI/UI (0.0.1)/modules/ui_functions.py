from main import *

# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions(MainWindow):
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
        else:
            GLOBAL_STATE = False
            self.showNormal()
            
    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.Left_Box.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 70
            
            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.Left_Box,b'minimumWidth')
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            # self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()


    def toggleLeftBox(self,enable):
        if enable:
            width = self.ui.extraLeftBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            standard = 0
            
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            
            self.left_animation = QPropertyAnimation(self.ui.extraLeftBox,b'minimumWidth')
            self.left_animation.setDuration(Settings.TIME_ANIMATION)
            self.left_animation.setStartValue(width)
            self.left_animation.setEndValue(widthExtended)
            # self.left_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.left_animation.start()


    def toggleRightBox(self, enable):
        if enable:
            width = self.ui.Login_Box.width()
            maxExtend = Settings.RIGHT_BOX_WIDTH
            standard = 0
            
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            
            self.right_animation = QPropertyAnimation(self.ui.Login_Box,b'minimumWidth')
            self.right_animation.setDuration(Settings.TIME_ANIMATION)
            self.right_animation.setStartValue(width)
            self.right_animation.setEndValue(widthExtended)
            # self.right_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.right_animation.start()
        
        
    def toggleVideoBox(self, enable):
        if enable:
            if Settings.PLAYPAUSE == 0:
                Settings.PLAYPAUSE = 1
                self.ui.Btn_PlayPause.setText('Pause')
                print('Pause')
            else:
                Settings.PLAYPAUSE = 0
                self.ui.Btn_PlayPause.setText('Play')
                print('Play')
    
    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    # event.accept()
            self.ui.centralwidget.mouseMoveEvent = moveWindow
            
        # MINIMIZE
        self.ui.Btn_Minimize.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.Btn_MaximizeRestore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.Btn_Close.clicked.connect(lambda: self.close())