import 'package:kis/services/index.dart';

// 실시간 주식 호가 (모의/실전)
Stream postStockReal(String sCode) async* {
  bool reallock = false;
  final channel = WebSocketChannel.connect(
      Uri.parse("ws://ops.koreainvestment.com:31000/tryitout/H0STASP0"));

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
          "input": {"tr_id": "H0STASP0", "tr_key": sCode}
        }
      },
    ),
  );
  yield* channel.stream;
  channel.stream.listen(
    (data) {
      if (reallock == false) {
        final jsondata = jsonDecode(data);
        if (jsondata['body']['msg1'] == "SUBSCRIBE SUCCESS") {
          reallock = true;
        }
      } else {
        // List<String> real_list = [];
        // real_list = data.split("^");
        // final String result = real_list[23];
        // return result;
      }
    },
  );
  throw Error();
}
