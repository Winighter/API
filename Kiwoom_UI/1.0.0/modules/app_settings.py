class S(): # S = Settings
    # APP SETTINGS
    # ///////////////////////////////////////////////////////////////
    ENABLE_CUSTOM_TITLE_BAR = True
    ETC_INFO = 0
    MENU_WIDTH = 220
    LEFT_BOX_WIDTH = 220
    RIGHT_BOX_WIDTH = 220
    TIME_ANIMATION = 200
    LOGIN_STATE = 0
    STATE = 0
    REAL_STATE = 0
    GET_BROCODE_STATE = 0
    fCode = ''
    oCode = ''
    
    # LIST
    # ///////////////////////////////////////////////////////////////
    BroCodeList = []
    cSg_List = []
    pSg_List = []
    콜저가풋고가 = []
    콜고가풋저가 = []
    oCode = ''
    # SCREEN NUMBER (MAX = 200)
    # ///////////////////////////////////////////////////////////////

    # REAL DATA
    SN_REAL = '9999'

    # FID LIST
    # ///////////////////////////////////////////////////////////////
    FL_FUTURE = '10'
    FL_HOKA = '128'
    FL_SIGO = '10;16;17;18'
    
    # DICTIONARY
    # ///////////////////////////////////////////////////////////////
    correction_order_dict = {}
    option_table_dict = {}
    real_dict = {}
    revise_order_dict = {}
    balance_dict = {}
    cLow_dict = {}
    cHigh_dict = {}
    pLow_dict = {}
    pHigh_dict = {}
    # CONDITION
    # ///////////////////////////////////////////////////////////////
    # 시가 고가 갯수 확인하는 가격 범위
    sgMin = 0.5
    sgMax = 10
    miss_range = 0.03

    # 매매할 가격 범위
    bas_max = float(1.0)
    bas_min = float(0.5)

    이익 = 25
    손절 = -10
    수량 = 4
    cHoka = 2000
    pHoka = -2000
    cHoka2 = 4000
    pHoka2 = -4000
    Act_Check = 0
    매수 = False
    CB_terms = 0
    PB_terms = 0
    형님행사가 = ''
    형님저가 = 0
    추세 = ''
    반대매수 = 0
    형님행사가2 = ''
    형님저가2 = 0
    형님Cnt = 0

    # 차트 옵션
    n분 = "10" # n분 차트

    # 손익율 = (평가금액 - 약정금액)/약정금액*100 -0.03%

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """