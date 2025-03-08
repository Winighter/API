import 'package:kis/services/index.dart';
import 'package:http/http.dart' as http;

// 1.Approval Key
class ApprovalKeyModel {
  final String approvalKey;
  ApprovalKeyModel.fromjson(Map<String, dynamic> json)
      : approvalKey = json['approval_key'];
}

Future<ApprovalKeyModel> postApprovalKey() async {
  final url = Uri.parse('$testDomain/oauth2/Approval');
  final response = await http.post(
    url,
    body: jsonEncode({
      "grant_type": "client_credentials",
      "appkey": appkey,
      "secretkey": appsecret,
    }),
  );
  if (response.statusCode == 200) {
    final dynamic jsonKey = jsonDecode(response.body);
    final ApprovalKeyModel key = ApprovalKeyModel.fromjson(jsonKey);
    print(key.approvalKey);
    return key;
  }
  throw Error();
}
