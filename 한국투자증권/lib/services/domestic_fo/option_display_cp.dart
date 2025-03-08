import 'package:http/http.dart' as http;
import 'package:kis/models/option_display_cp.dart';
import 'package:kis/services/index.dart';

// 국내옵션전광판_콜풋 (실전) (토큰)
Future<List<OptionDisplayCPModel>> getDisplayCP(token) async {
  List<OptionDisplayCPModel> optionsInstances = [];
  final params = {
    'FID_COND_MRKT_DIV_CODE': "O",
    'FID_COND_SCR_DIV_CODE': '20503',
    'FID_MRKT_CLS_CODE': 'CO',
    'FID_MTRT_CNT': '202501', // YYYYMM
    'FID_COND_MRKT_CLS_CODE': '',
    'FID_MRKT_CLS_CODE1': 'PO',
  };
  final url = Uri.https(
      'openapi.koreainvestment.com:9443',
      '/uapi/domestic-futureoption/v1/quotations/display-board-callput',
      params);
  final response = await http.get(
    url,
    headers: {
      'content-type': 'charset=utf-8',
      'authorization': "Bearer $token",
      'appkey': appkeyFO,
      'appsecret': appsecretFO,
      'tr_id': 'FHPIF05030100',
      'tr_cont': '',
      'custtype': 'P'
    },
  );
  if (response.statusCode == 200) {
    final jsonBalance = jsonDecode(utf8.decode(response.bodyBytes));
    if (jsonBalance['rt_cd'] == "0") {
      final List<dynamic> callOptions = jsonBalance['output1'];
      for (var callOption in callOptions) {
        optionsInstances.add(OptionDisplayCPModel.fromjson(callOption));
      }
      final List<dynamic> putOptions = jsonBalance['output2'];
      for (var putOption in putOptions) {
        optionsInstances.add(OptionDisplayCPModel.fromjson(putOption));
      }
      // print(optionsInstances);
      return optionsInstances;
    }
  }
  throw Error();
}
