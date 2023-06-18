from main import *

class AppFunctions(MainWindow):
    def setThemeHack(self, theme):

        # CUSTOM THEME
        # ///////////////////////////////////////////////////////////////    
        if theme == 'colorful':
            self.ui.extraRightBox.setStyleSheet("background-color: #ADBED2;")
            self.ui.frame_4.setStyleSheet("QPushButton {color: rgb(255, 255, 255);background-color:#EB8F90;border: 0px solid} QPushButton:hover {background-color: #FFB471}")
            self.ui.frame_2.setStyleSheet("background-color:#EB8F90;")
            self.ui.frame_7.setStyleSheet("background-color:#EB8F90;")
            self.ui.frame_9.setStyleSheet("QPushButton {color: #FFFFFF;background-color:#ADBED2;border: 0px solid} QPushButton:hover {background-color: #FFB471}")
            self.ui.extraLeftBox.setStyleSheet("background-color: #ADBED2;")
            self.ui.extraCloseColumnBtn.setStyleSheet("QPushButton {color: rgb(255, 255, 255);border: 0px solid} QPushButton:hover {background-color: #FFB471}")
            self.ui.tableWidget.setStyleSheet("gridline-color: rgb(85, 85, 85);")
            
    def loginScreenState(self):
        self.login_ui.label_login_state.setText('Incorrect Username or Password.')
        self.login_ui.label_login_state.setStyleSheet("Color: #E81E25")

    def loginState(self, state):
        # CONNECT STATE
        if state == 0: # 성공
            self.ui.LoginStateLabel.setStyleSheet("color: #90EE90;")
            self.ui.LoginStateLabel.setText("Connected")
            self.ui.Btn_Login.setText("REAL DATA")
            self.ui.Btn_Login.setStyleSheet(u"QPushButton {color: #FFFFFF; border: 0px solid}")

        if state == 1: # 실패
            self.ui.LoginStateLabel.setStyleSheet("color: #FF0000;")
            self.ui.LoginStateLabel.setText("Unconnected")

        if state == 2: # 연결중
            self.ui.LoginStateLabel.setStyleSheet("color: #f1fa8c;")
            self.ui.LoginStateLabel.setText("Connecting...")
            
    def realDataState(self, state):
        if state == 0:
            self.ui.Btn_Login.setStyleSheet("color: #90EE90;")
            
        if state == 1:
            self.ui.Btn_Login.setStyleSheet("color: #FFFFFF;")
            
            
    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
    """