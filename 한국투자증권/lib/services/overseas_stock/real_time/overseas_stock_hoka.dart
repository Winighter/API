import 'package:kis/services/index.dart';

// 실시간 해외주식 (미국)호가 (실전)
Stream realOverseasStockHoka() async* {
  // bool reallock = false;
  final channel = WebSocketChannel.connect(
      Uri.parse("ws://ops.koreainvestment.com:21000/tryitout/HDFSASP0"));
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
          "input": {"tr_id": "HDFSASP0", "tr_key": OVERSEAS_STOCK_CODE}
        }
      },
    ),
  );
  channel.stream.listen(
    (data) {
      print(data);
      // if (reallock == false) {
      // final jsondata = jsonDecode(data);
      // if (jsondata['body']['msg1'] == "SUBSCRIBE SUCCESS") {
      //   reallock = true;
      // }
      // } else {
      // return data;
      // List<String> real_list = [];
      // real_list = data.split("^");
      // final String result = real_list[23];
      // return result;
      // }
    },
  );
  throw Error();
}
