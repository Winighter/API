import win32com.client

class Main:
    def __init__(self):

        # CREATE OBJECT
        self.creon = win32com.client.Dispatch("CpUtil.CpCybos")
        self.creon_option = win32com.client.Dispatch("CpUtil.CpOptionCode")
        
        
        # SERVER STATE
        server_state = self.creon.IsConnect
        if server_state == 1:
            print("연결정상")
        else:
            print('연결끊김')
            
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
        

     
            
if __name__ == '__main__':
    Main()