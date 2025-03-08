import 'package:kis/services/index.dart';
import 'package:http/http.dart' as http;

// Discard Token
class DiscardTokenModel {
  final String message;
  final int code;
  DiscardTokenModel.fromjson(Map<String, dynamic> json)
      : code = json['code'],
        message = json['message'];
}

Future<DiscardTokenModel> postDiscardToken(token) async {
  final url = Uri.parse('$testDomain/oauth2/revokeP');
  final response = await http.post(
    url,
    body: jsonEncode({
      'appkey': appkey,
      'appsecret': appsecret,
      'token': token,
    }),
  );
  if (response.statusCode == 200) {
    final dynamic jsonToken = jsonDecode(utf8.decode(response.bodyBytes));
    final DiscardTokenModel result = DiscardTokenModel.fromjson(jsonToken);
    // print(result);
    return result;
  }
  throw Error();
}
