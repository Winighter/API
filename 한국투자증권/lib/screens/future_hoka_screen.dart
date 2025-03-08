import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:kis/services/domestic_fo/real_time/future_hoka.dart';

// 실시간 호가 페이지
class FutureHokaPage extends StatefulWidget {
  const FutureHokaPage({super.key});

  @override
  State<FutureHokaPage> createState() => FutureHokaState();
}

class FutureHokaState extends State<FutureHokaPage> {
  final Stream realhoka = realFutureHoka();
  late int lowHoka, highHoka;
  bool reallock = false;

  bool call = false;
  bool put = false;
  bool order = false;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: StreamBuilder(
          stream: realhoka,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              if (snapshot.connectionState == ConnectionState.done) {
                reallock = false;
              }
              if (reallock == false) {
                lowHoka = 99999;
                highHoka = -99999;
                reallock = true;
              } else {
                List<String> realList = [];
                realList = snapshot.data.split("^");
                String a = realList[34];
                String b = realList[35];
                int aValue = int.parse(a);
                int bValue = int.parse(b);
                final fHoka = bValue - aValue;
                ///////////////////////////////////
                return Text(
                  '$fHoka',
                  style: TextStyle(fontSize: 100),
                  textAlign: TextAlign.center,
                );
              }
            }
            return Center(
              child: CupertinoActivityIndicator(
                radius: 20,
                color: Colors.blue,
              ),
            );
          },
        ),
      ),
    );
  }
}
