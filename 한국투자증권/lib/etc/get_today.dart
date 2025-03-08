import 'package:intl/intl.dart';

String getToday() {
  String formattedDate = DateFormat('yyyyMMdd').format(DateTime.now());
  return formattedDate;
}
