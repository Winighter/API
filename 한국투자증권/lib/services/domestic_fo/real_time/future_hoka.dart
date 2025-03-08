import 'package:kis/services/index.dart';
import 'package:flutter/material.dart';
import 'package:kis/services/index.dart';

// 실시간 선물 호가 (실전)
Stream realFutureHoka() async* {
  final channel = WebSocketChannel.connect(
      Uri.parse("ws://ops.koreainvestment.com:21000/tryitout/H0IFASP0"));
  await channel.ready;
  channel.sink.add(
    jsonEncode(
      {
        "header": {
          "appkey": appkeyFO,
          "appsecret": appsecretFO,
          'custtype': 'P',
          'tr_type': '1',
          'content-type': 'utf-8',
        },
        "body": {
          "input": {"tr_id": "H0IFASP0", "tr_key": FUTURE_CODE}
        }
      },
    ),
  );
  yield* channel.stream;
}
