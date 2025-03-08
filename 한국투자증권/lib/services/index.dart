export 'dart:convert';
export 'package:kis/etc/info.dart';
export 'package:kis/etc/get_today.dart';
export 'package:web_socket_channel/web_socket_channel.dart';

const String realDomain = "https://openapi.koreainvestment.com:9443";
const String testDomain = "https://openapivts.koreainvestment.com:29443";

const FO_OD = "VTTO1101U";
const FO_ON = "VTCE1001U";
const FO_REAL_OD = "TTTO1101U";
const FO_REAL_ON = "JTCE1001U";

const test_token =
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6ImNjNmM3MzBjLTVkMjEtNGQwMC1hYTI1LTBjNGZlNThiMzZmMSIsInByZHRfY2QiOiIiLCJpc3MiOiJ1bm9ndyIsImV4cCI6MTcxODA2ODk0NSwiaWF0IjoxNzE3OTgyNTQ1LCJqdGkiOiJQU1VxRFNTeDNNcTJnbVpoYkUzTDV6cnhsNzdrWUMyWnhqOWUifQ.SLdfvz6GnKLL_cetYkWbN0yrVUESZArYaIGAGOfKRQhvfZg6Var9Zb8WRj7Gay9owZPUk9WoBHss7hTtldMQLg";
const test_tokenFO =
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6ImRiOGNiYmFhLTg2ODUtNDc2NS1iNTFjLWE5YzU1ZTEyNTk2NiIsInByZHRfY2QiOiIiLCJpc3MiOiJ1bm9ndyIsImV4cCI6MTcxODA3MzI0OSwiaWF0IjoxNzE3OTg2ODQ5LCJqdGkiOiJQU05pdGFNeFVkZlZTenVtTkE4aURncVQ2aXpDdk5OSWlTWVcifQ.DqIKaFT-_YPRMgxMjCYoMf7l4sTcXNhx6Dih0JnjCLv1AEiZKkH9CPYxRoTyUqyC4D3opK0sTBejSryzHKzPvg";

const FUTURE_CODE = "101W03";
// 1|101W03|KR4101W30003|F 202503| |00000.00|4|2001|KOSPI200
// 1|101W06|KR4101W60000|F 202506| |00000.00|5|2001|KOSPI200
// 1|101W12|KR4101WC0003|F 202512| |00000.00|6|2001|KOSPI200

const CME_NIGHT_FUTURE_CODE = '1101V06';
// 1101V06   KR4101V60002F 202406 00000.00 2001     KOSPI200
// 1101V09   KR4101V90009F 202409 00000.00 2001     KOSPI200
// 1101V12   KR4101VC0004F 202412 00000.00 2001     KOSPI200
// 1101W03   KR4101W30003F 202503 00000.00 2001     KOSPI200
// 1101W06   KR4101W60000F 202506 00000.00 2001     KOSPI200
// 1101W12   KR4101WC0003F 202512 00000.00 2001     KOSPI200
// 1A01612   KR4A016C0004F 202612 00000.00 2001     KOSPI200

const OVERSEAS_STOCK_CODE = "";
// P.DJI DOW JONES INDUSTRIAL AVERAGE INDEX 다우존스 산업지수 DOWJ501
// PCOMP NASDAQ Composite                   나스닥 종합      000NASD501

const OVERSEAS_FO_CODE = "DJEM24";
// DJEM24 YYNN Dow Jones Real Estate-202406 CME DJE 003    1   -2     0.1      10 100  10  1011NN52
// DJEU24 YYNN Dow Jones Real Estate-202409 CME DJE 003    1   -2     0.1      10 100  10  1000NN52
// DJEZ24 YYNN Dow Jones Real Estate-202412 CME DJE 003    1   -2     0.1      10 100  10  1000NN52
// DJEH25 YYNN Dow Jones Real Estate-202503 CME DJE 003    1   -2     0.1      10 100  10  1000NN52
