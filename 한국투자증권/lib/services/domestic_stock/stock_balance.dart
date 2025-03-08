import 'package:http/http.dart' as http;
import 'package:kis/services/index.dart';
import 'package:kis/models/stock_balance_model.dart';

// 4.주식 잔고 조회 (모의/실전) (토큰)
Future<List<StockBalanceModel>> getBalance(token) async {
  List<StockBalanceModel> stocksInstances = [];
  final params = {
    "CANO": acntnum,
    "ACNT_PRDT_CD": '01',
    'AFHR_FLPR_YN': 'N',
    'OFL_YN': '',
    'INQR_DVSN': '02',
    'UNPR_DVSN': '01',
    'FUND_STTL_ICLD_YN': 'Y',
    'FNCG_AMT_AUTO_RDPT_YN': 'N',
    'PRCS_DVSN': '01',
    'CTX_AREA_FK100': '',
    'CTX_AREA_NK100': '',
  };
  final url = Uri.https('openapivts.koreainvestment.com:29443',
      '/uapi/domestic-stock/v1/trading/inquire-balance', params);
  final response = await http.get(
    url,
    headers: {
      'content-type': 'application/json',
      'authorization': "Bearer $token",
      'appkey': appkey,
      'appsecret': appsecret,
      'tr_id': 'VTTC8434R', // 실전: TTTC8434R,모의: VTTC8434R
      'tr_cont': '',
      'custtype': 'P'
    },
  );
  if (response.statusCode == 200) {
    final jsonBalance = jsonDecode(utf8.decode(response.bodyBytes));
    if (jsonBalance['rt_cd'] == "0") {
      final List<dynamic> stocks = jsonBalance['output1'];
      for (var stock in stocks) {
        stocksInstances.add(StockBalanceModel.fromjson(stock));
      }
      // print(stocksInstances);
      return stocksInstances;
    }
  }
  throw Error();
}
