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


if __name__ == "__main__":
    Cybos()