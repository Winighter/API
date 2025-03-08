import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:kis/etc/info.dart';
import 'package:kis/screens/home_screen.dart';
import 'package:kis/services/common/issue_token.dart';
import 'package:kis/services/common/holiday.dart';
import 'package:kis/services/domestic_fo/order_fo_cash_.dart';
import 'package:kis/services/domestic_fo/option_display_cp2.dart';
import 'package:kis/services/domestic_fo/real_time/future_hoka.dart';

void main() {
  // postAccessToken("F");
  postFutureOptionOrder(toke, "201W01327");
  // postAccessToken('R');
  // getDisplayCP();
  // runApp(App());
}

// void main() => runApp(const App());

class App extends StatelessWidget {
  const App({super.key});
  @override
  Widget build(BuildContext context) {
    SystemChrome.setPreferredOrientations(
        [DeviceOrientation.portraitUp, DeviceOrientation.portraitDown]);
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: '한국투자증권',
      home: HomeScreen(),
    );
  }
}
// flutter build apk --release --target-platform=android-arm64
