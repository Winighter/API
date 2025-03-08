import 'package:kis/services/index.dart';

// 실시간 해외 선물옵션 실시간 호가 (실전)
Stream realOverseasHokaFO() async* {
  bool reallock = false;
  final channel = WebSocketChannel.connect(
      Uri.parse("ws://ops.koreainvestment.com:21000/tryitout/HDFFF010"));
  await channel.ready;
  channel.sink.add(
    jsonEncode(
      {
        "header": {
          "appkey": appkey,
          "appsecret": appsecret,
          'custtype': 'P',
          'tr_type': '1',
          'content-type': 'utf-8'
        },
        "body": {
          "input": {
            "tr_id": "HDFFF010",
            "tr_key": OVERSEAS_FO_CODE,
          }
        }
      },
    ),
  );
  channel.stream.listen(
    (data) {
      if (reallock == false) {
        final jsondata = jsonDecode(data);
        if (jsondata['body']['msg1'] == "SUBSCRIBE SUCCESS") {
          reallock = true;
        }
      } else {
        print(data);
        return data;
        // List<String> real_list = [];
        // real_list = data.split("^");
        // final String result = real_list[23];
        // return result;
      }
    },
  );
  throw Error();
}
