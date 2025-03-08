import 'package:http/http.dart' as http;
import 'package:kis/services/index.dart';
import 'package:kis/models/expiration_date_model.dart';

// 국내옵션전광판 옵션월물리스트 조회 (실전) (토큰)
Future<List<ExpirationDatesModel>> getExpirationDates(token) async {
  List<ExpirationDatesModel> datesInstances = [];
  final params = {
    "FID_COND_SCR_DIV_CODE": "509",
    "FID_COND_MRKT_DIV_CODE": '',
    'FID_COND_MRKT_CLS_CODE': '',
  };
  final url = Uri.https(
      'openapivts.koreainvestment.com:29443',
      '/uapi/domestic-futureoption/v1/quotations/display-board-option-list',
      params);
  final response = await http.get(
    url,
    headers: {
      'content-type': 'application/json',
      'authorization': "Bearer $token",
      'appkey': appkey,
      'appsecret': appsecret,
      'tr_id': 'FHPIO056104C0',
      'tr_cont': '',
      'custtype': 'P'
    },
  );
  if (response.statusCode == 200) {
    final jsonBalance = jsonDecode(utf8.decode(response.bodyBytes));
    if (jsonBalance['rt_cd'] == "0") {
      final List<dynamic> dates = jsonBalance['output'];
      for (var date in dates) {
        datesInstances.add(ExpirationDatesModel.fromjson(date));
      }
      // print(datesInstances);
      return datesInstances;
    }
  }
  throw Error();
}
