import 'dart:async';
import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/services.dart';
import 'package:kis/models/future_option_balance_model.dart';
import 'package:kis/services/domestic_fo/balance_fo.dart';
import 'package:kis/services/index.dart';

// 계좌 잔고
class BalancePage extends StatefulWidget {
  const BalancePage({super.key});

  @override
  State<BalancePage> createState() => BalanceState();
}

class BalanceState extends State<BalancePage> {
  @override
  Widget build(BuildContext context) {
    final Future<List<FoBalanceModel>> balances = getBalanceFO('token');
    return Scaffold(
      body: Center(
          child: FutureBuilder(
        future: balances,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return ListView(
              children: [
                for (var balance in snapshot.data!) Text(balance.shtn_pdno),
              ],
            );
          }
          return Center(
            child: CupertinoActivityIndicator(
              radius: 20,
              color: Colors.blue,
            ),
          );
        },
      )),
    );
  }
}
