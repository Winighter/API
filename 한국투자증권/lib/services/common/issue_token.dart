import 'package:http/http.dart' as http;
import 'package:kis/services/index.dart';
import 'package:kis/services/common/holiday.dart';
import 'package:kis/services/domestic_fo/balance_fo.dart';
import 'package:kis/services/domestic_fo/option_display_cp.dart';

// Access Token (Instance)
class TokenModel {
  final int expiresIn;
  final String accessToken, tokenType, accessTokenExpired;
  TokenModel.fromjson(Map<String, dynamic> json)
      : accessToken = json['access_token'],
        accessTokenExpired = json['access_token_token_expired'],
        tokenType = json['token_type'],
        expiresIn = json['expires_in'];
}

Future<TokenModel> postAccessToken(ftr) async {
  var domain = testDomain;
  var key = appkey;
  var secret = appsecret;
  if (ftr == 'T') {
    domain = realDomain;
    key = appkeyFO;
    secret = appsecretFO;
  }
  final url = Uri.parse('$domain/oauth2/tokenP');
  final response = await http.post(
    url,
    body: jsonEncode({
      'grant_type': "client_credentials",
      'appkey': key,
      'appsecret': secret,
    }),
  );
  if (response.statusCode == 200) {
    print(response.body);
    final dynamic jsonToken = jsonDecode(response.body);
    final TokenModel token = TokenModel.fromjson(jsonToken);
    print(token.accessToken);
    if (true) {
      getHoliday(token.accessToken);
      if (ftr == 'F') {
        print('모의투자접속');
        // getBalanceFO(token.accessToken);
      }
      if (ftr == 'T') {
        print('실전투자접속');
      }
    }
    return token;
  }
  print('토큰 생성 에러 재실행');
  throw Error();
}
