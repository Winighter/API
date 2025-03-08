import 'package:kis/services/index.dart';

// 실시간 CME 야간선물 실시간 호가 (실전)
Stream realCmeNightFutureHoka() async* {
  // bool reallock = false;
  final channel = WebSocketChannel.connect(
      Uri.parse("ws://ops.koreainvestment.com:21000/tryitout/H0MFASP0"));
  await channel.ready;
  channel.sink.add(
    jsonEncode(
      {
        "header": {
          "appkey": appkey,
          "appsecret": appsecret,
          "custtype": "P",
          "tr_type": "1",
          "content-type": "utf-8"
        },
        "body": {
          "input": {"tr_id": "H0MFASP0", "tr_key": CME_NIGHT_FUTURE_CODE}
        }
      },
    ),
  );
  yield* channel.stream;
  // channel.stream.listen(
  //   (data) {
  //     print(data);
  //     if (reallock == false) {
  //       final jsondata = jsonDecode(data);
  //       if (jsondata['body']['msg1'] == "SUBSCRIBE SUCCESS") {
  //         reallock = true;
  //       }
  //     } else {
  //       print(data);
  //       // List<String> real_list = [];
  //       // real_list = data.split("^");
  //       // final String result = real_list[23];
  //       // return result;
  //     }
  //   },
  // );
  // throw Error();
}
