import 'package:kis/services/index.dart';
import 'package:http/http.dart' as http;

// 2.Hash
class HashModel {
  String CANO, ACNT_PRDT_CD, OVRS_EXCG_CD, HASH;
  HashModel.fromjson(Map<String, dynamic> json)
      : CANO = json['BODY']['CANO'],
        ACNT_PRDT_CD = json['BODY']['ACNT_PRDT_CD'],
        OVRS_EXCG_CD = json['BODY']['OVRS_EXCG_CD'],
        HASH = json['HASH'];
}

Future<HashModel> postHashKey() async {
  final url = Uri.parse('$realDomain/uapi/hashkey');
  final response = await http.post(
    url,
    headers: {
      'content-Type': 'application/json',
      'appkey': appkey,
      'appsecret': appsecret,
    },
    body: jsonEncode({
      'CANO': acntnum,
      'ACNT_PRDT_CD': '03', // Stock: 01, FO: 03
      'OVRS_EXCG_CD': 'SHAA',
    }),
  );
  if (response.statusCode == 200) {
    dynamic jsonHash = jsonDecode(response.body);
    final HashModel hash = HashModel.fromjson(jsonHash);
    // print(hash);
    return hash;
  }
  throw Error();
}
