import 'package:kis/services/index.dart';
import 'package:http/http.dart' as http;

// {rt_cd: 0, msg_cd: 40600000, msg1: 모의투자 매수주문이 완료 되었습니다., output: {ACNT_NAME: 윤영수, TRAD_DVSN_NAME: 매수, ITEM_NAME: 코스피200 F 202412, ORD_TMD: 093753, ORD_GNO_BRNO: 00950, ODNO: 0000001919}}
// {rt_cd: 0, msg_cd: 40590000, msg1: 모의투자 매도주문이 완료 되었습니다., output: {ACNT_NAME: 윤영수, TRAD_DVSN_NAME: 매도, ITEM_NAME: 코스피200 F 202412, ORD_TMD: 093859, ORD_GNO_BRNO: 00950, ODNO: 0000001946}}
// 5. 선물옵션 주문_현금 (모의/실전) (토큰/계좌번호) (Instance? 주문 성공만 확인하면 될듯?)

class FutureOptionOrderModel {
  final String rt_cd, // 0 : 성공, 0 이외의 값 : 실패
      msg_cd, // 응답코드
      msg1, // 응답메세지
      ACNT_NAME, // 계좌의 고객명
      TRAD_DVSN_NAME, // 매도/매수 등 구분값
      ITEM_NAME, // 주문 종목 명칭
      ORD_TMD, // 주문 접수 시간
      ORD_GNO_BRNO, // 계좌 개설 시 관리점으로 선택한 영업점의 고유번호
      ODNO; // 	접수한 주문의 일련번호
  FutureOptionOrderModel.fromjson(Map<String, dynamic> json)
      : rt_cd = json['rt_cd'],
        msg_cd = json['msg_cd'],
        msg1 = json['msg1'],
        ACNT_NAME = json['output']['ACNT_NAME'],
        TRAD_DVSN_NAME = json['output']['TRAD_DVSN_NAME'],
        ITEM_NAME = json['output']['ITEM_NAME'],
        ORD_TMD = json['output']['ORD_TMD'],
        ORD_GNO_BRNO = json['output']['ORD_GNO_BRNO'],
        ODNO = json['output']['ODNO'];
}

Future postFutureOptionOrder(String token, String code) async {
  final url = Uri.https("openapivts.koreainvestment.com:29443",
      "uapi/domestic-futureoption/v1/trading/order");
  // Uri.parse('$testDomain/uapi/domestic-futureoption/v1/trading/order');
  final header = {
    'authorization': 'Bearer $token',
    'appkey': appkey,
    'appsecret': appsecret,
    'tr_id': "VTTO1101U",
  };
  final response = await http.post(
    url,
    headers: header,
    body: jsonEncode({
      "ORD_PRCS_DVSN_CD": "02",
      "CANO": acntnum, // 계좌번호 체계(8-2)의 앞 8자리
      "ACNT_PRDT_CD": '03', // 계좌번호 체계(8-2)의 뒤 2자리
      "SLL_BUY_DVSN_CD": '02', // 매도: 01, 매수: 02
      "SHTN_PDNO": code, // 선물 6자리, 옵션 9자리
      "ORD_QTY": "1", // 주문수량
      "UNIT_PRICE": '0', // 주문가격, 시장가나 최유리 지정가인 경우 0
      "ORD_DVSN_CD": "02" // 01: 지정가, 02: 시장가
    }),
  );
  print("Hhhhhhhhhhhhhhhhhhhh");
  print(response.statusCode);
  if (response.statusCode == 200) {
    print(response.body);
    final jsonOrderFO = jsonDecode(utf8.decode(response.bodyBytes));
    print(jsonOrderFO);
    final FutureOptionOrderModel OrderFO =
        FutureOptionOrderModel.fromjson(jsonOrderFO);
    if (OrderFO.rt_cd == "0") {
      // Success Message
    }
    // print(OrderFO);
    return OrderFO;
  }
  throw Error();
}
