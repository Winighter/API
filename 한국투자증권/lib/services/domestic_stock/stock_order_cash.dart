import 'package:kis/services/index.dart';
import 'package:http/http.dart' as http;

// 5. 주식 주문_현금 (모의/실전) (토큰/계좌번호) (Instance? 주문 성공만 확인하면 될듯?)
Future postStockOrder(String token, String oCode, String oPrice) async {
  final url =
      Uri.parse('$testDomain/uapi/domestic-stock/v1/trading/order-cash');
  final header = {
    'content-type': 'application/json',
    'authorization': 'Bearer $token',
    'appkey': appkey,
    'appsecret': appsecret,
    'tr_id': 'VTTC0802U',
    'tr_cont': '',
    'custtype': 'P',
  };
  final response = await http.post(
    url,
    headers: header,
    body: jsonEncode(
      {
        "ORD_PRCS_DVSN_CD": "02",
        "CANO": acntnum,
        "ACNT_PRDT_CD": '01', // 주식: 01, 선옵: 03
        "SLL_BUY_DVSN_CD": '02', // 01:매도, 02:매수
        "SHTN_PDNO": oCode, // 선물 6자리, 옵션 9자리
        "ORD_QTY": "1", // 주문수량
        "UNIT_PRICE": '5', // 주문가격/ 시장가나 최유리 지정가인 경우 0
        "NMPR_TYPE_CD": "",
        "KRX_NMPR_CNDT_CD": "",
        "CTAC_TLNO": "",
        "FUOP_ITEM_DVSN_CD": "",
        "ORD_DVSN_CD": "01" // 01: 지정가, 02: 시장가
      },
    ),
  );
  if (response.statusCode == 200) {
    final jsonBody = jsonDecode(utf8.decode(response.bodyBytes));
    if (jsonBody['rt_cd'] == "0") {
      // Success Message
      // final short_rb = jsonBody['output'];
    }
  }
  throw Error();
}
