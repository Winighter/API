class Settings():
    # APP SETTINGS
    # ///////////////////////////////////////////////////////////////
    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 220
    LEFT_BOX_WIDTH = 220
    RIGHT_BOX_WIDTH = 220
    TIME_ANIMATION = 200
    LOGIN_STATE = 0
    REAL_STATE = 0
    PLAYPAUSE = 0
    fCode = ''
    
    # LIST
    # ///////////////////////////////////////////////////////////////
    cCodeList = []
    pCodeList = []
    BroCodeList = []
    cSg_List = []
    pSg_List = []
    # SCREEN NUMBER (MAX = 200)
    # ///////////////////////////////////////////////////////////////

    # ORDER 
    SN_ORDER = '1000'

    # TR DATA
    SN_TR1 = '1001'
    SN_TR2 = '1002'
    SN_TR3 = '1003'
    SN_TR4 = '1004'

    # REAL DATA
    SN_REAL_HOKA = '3691'
    SN_REAL_FUTURE_PRICE= '3692'
    SN_REAL_CALL_OPTION_MARKET_PRICE = '2000'
    SN_REAL_PUT_OPTION_MARKET_PRICE = '3000'
    SN_REAL_MARKET_OPERATION_HOURS = '4000'
    SN_REAL = '9999'

    # FID LIST
    # ///////////////////////////////////////////////////////////////
    FL_FUTURE = '10'
    FL_HOKA = '128'
    FL_SIGO = '10;16;17;18'
    FN_MARKET_OPERATION_HOURS = '215'
    
    # DICTIONARY
    # ///////////////////////////////////////////////////////////////
    cDict2 = {}
    pDict2 = {}
    option_table_dict = {}
    trendict = {'추세':'','cSiKo':0,'pSiKo':0,'c손절':0,'p손절':0,'cCode':{'':0},'cCode2':{'':0},'pCode':{'':0},'pCode2':{'':0},}
    real_dict = {}

    # CONDITION
    # ///////////////////////////////////////////////////////////////
    # 시가 고가 갯수 확인하는 가격 범위
    sgMax = 10
    sgMin = 0.5

    # 매매할 가격 범위
    bas_max = float(1.2)
    bas_min = float(0.8)

    이익 = 40
    손절 = -10
    수량 = 4
    cHoka = 2000
    pHoka = -2000
    수수료 = 0
    Act_Check = 0
    매수 = False
    형님행사가 = ''
    추세 = ''
    # 실거래시 매수 매도 수수료는 각각 0.015%이며 
    # 모의투자의 수수료율은 0.35% 의 수수료로 계산됩니다


    Order_cancellation_range = 0.05
    OCR = float(Order_cancellation_range)

    KOSPI200 = '201'

    # Dict
    real_dict = {'cCode':'','cPrice':0,'cLow2':0,'cbHoka':0,'pCode':'','pPrice':0,'pLow2':0,'pbHoka':0}

    # 차트 옵션
    n분 = "10" # n분 차트

    # 손익율 = (평가금액 - 약정금액)/약정금액*100 -0.03%