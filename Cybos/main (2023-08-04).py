import win32com.client as win32
from slack import *

class Cybos:
    def __init__(self):
        daishin = win32.Dispatch("CpUtil.CpCybos")
        print(daishin.IsConnect) # 1:정상 / 0: 끊김

        fHoka = win32.Dispatch("CpSysDib.FutureJpBid")
        fHoka.SetInputValue('0',value)

        fsHoka.GetHeaderValue(12)
        fbHoka.GetHeaderValue(29)       
        # SERVER TYPE
        server_type = self.creon.ServerType
        if server_type == 1:
            print("CyBos Plus Server")
        elif server_type:
            print('연결끊김')
        else:
            print('HTS 보통서버')

        self.DisConnect_CreonPlus()
        
    def DisConnect_CreonPlus(self):
        print("종료시작")
        self.creon.PlusDisconnect()

if __name__ == "__main__":
    Cybos()
