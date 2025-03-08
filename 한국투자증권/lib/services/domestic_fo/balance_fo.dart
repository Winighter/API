import 'package:http/http.dart' as http;
import 'package:kis/services/index.dart';
import 'package:kis/models/future_option_balance_model.dart';

// 선옵 잔고 조회 (모의/실전) (토큰)
Future<List<FoBalanceModel>> getBalanceFO(token) async {
  print(token);
  List<FoBalanceModel> optionsInstances = [];
  final params = {
    "CANO": acntnum,
    "ACNT_PRDT_CD": '03',
    'MGNA_DVSN': '1',
    'EXCC_STAT_CD': '2',
    'CTX_AREA_FK200': '02',
    'CTX_AREA_NK200': '01',
  };
  final url = Uri.https('openapivts.koreainvestment.com:29443',
      '/uapi/domestic-futureoption/v1/trading/inquire-balance', params);
  final response = await http.get(
    url,
    headers: {
      'authorization': "Bearer $token",
      'appkey': appkey,
      'appsecret': appsecret,
      'tr_id': 'VTFO6118R', // 실전: CTFO6118R ,모의: VTFO6118R
    },
  );
  if (response.statusCode == 200) {
    final jsonBalance = jsonDecode(utf8.decode(response.bodyBytes));
    if (jsonBalance['rt_cd'] == "0") {
      final List<dynamic> options = jsonBalance['output1'];
      for (var option in options) {
        final instance = FoBalanceModel.fromjson(option);
        print(instance.shtn_pdno);
        optionsInstances.add(instance);
      }
      // print(optionsInstances);
      return optionsInstances;
    }
  }
  throw Error();
}
