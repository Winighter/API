import 'package:kis/services/index.dart';
import 'package:http/http.dart' as http;
import 'package:kis/models/holiday_model.dart';
import 'package:kis/services/common/issue_token.dart';

// 국내 휴장일 조회
Future<List<HolidayModel>> getHoliday(token) async {
  List<HolidayModel> holidayInstances = [];
  String today = getToday();
  var headers = {
    'content-type': 'application/json; charset=utf-8',
    'authorization': 'Bearer $token',
    'appkey': appkeyFO,
    'appsecret': appsecretFO,
    'tr_id': 'CTCA0903R',
    'custtype': 'P',
  };

  final url = Uri.parse(
      '$realDomain/uapi/domestic-stock/v1/quotations/chk-holiday?BASS_DT=$today&CTX_AREA_NK=&CTX_AREA_FK=');
  final response = await http.get(url, headers: headers);
  if (response.statusCode == 200) {
    final List<dynamic> holidays =
        (jsonDecode(utf8.decode(response.bodyBytes))['output']);
    for (var holiday in holidays) {
      final instance = HolidayModel.fromjson(holiday);
      holidayInstances.add(instance);
      if (instance.bass_dt == today) {
        if (instance.opnd_yn == 'Y') {
          // 실제 사용시에는'N'으로
          // 휴장일
          // print('휴장일');
        } else {
          // print('개장일');
          postAccessToken('T');
        }
      }
    }
    // print(holidayInstances);
    return holidayInstances;
  }
  throw Error();
}
