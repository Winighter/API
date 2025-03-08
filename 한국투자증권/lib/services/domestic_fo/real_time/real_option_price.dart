// import 'dart:io';

import 'package:flutter/material.dart';
import 'package:kis/services/index.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'WebSocket Demo';
    return const MaterialApp(
      title: title,
      home: MyHomePage(
        title: title,
      ),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({
    super.key,
    required this.title,
  });

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController _controller = TextEditingController();
  final _channel = WebSocketChannel.connect(
    Uri.parse('ws://ops.koreainvestment.com:21000/tryitout/H0IOCNT0'),
  );

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Form(
              child: TextFormField(
                controller: _controller,
                decoration: const InputDecoration(labelText: 'Send a message'),
              ),
            ),
            const SizedBox(height: 24),
            StreamBuilder(
              stream: _channel.stream,
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  List<String> realList = [];
                  realList = snapshot.data.split("^");
                  if (realList.length == 1) {
                    return Text('');
                  } else {
                    // String a = realList[2]; // 현재가
                    // String b = realList[6]; // 시가 (없어도 상관X)
                    // String c = realList[7]; // 고가
                    // String d = realList[8]; // 저가
                    // String e = realList[42]; // 최우선 매수호가

                    // List l = [d, c, b, a];
                    // String str = l.join(", ");

                    // print(realList[0].substring(realList[0].length - 1));
                    print(realList[0]);
                    return Text(realList[0]);
                  }
                } else {
                  return CircularProgressIndicator();
                }
              },
            )
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _sendMessage,
        tooltip: 'Send message',
        child: const Icon(Icons.send),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }

  void _sendMessage() {
    List<String> code_list = ['201W01325', '201W01327'];
    for (int i = 0; i < code_list.length; i++) {
      print(code_list[i]);
      _channel.sink.add(
        jsonEncode(
          {
            "header": {
              "approval_key": approvalKey,
              'custtype': 'P',
              "tr_type": '1',
              'content-type': 'utf-8',
            },
            "body": {
              "input": {"tr_id": "H0IOCNT0", "tr_key": code_list[i]}
            }
          },
        ),
      );
    }
  }

  @override
  void dispose() {
    _channel.sink.close();
    _controller.dispose();
    super.dispose();
  }
}
