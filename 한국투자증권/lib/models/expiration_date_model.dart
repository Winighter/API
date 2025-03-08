class ExpirationDatesModel {
  final String mtrt_yymm_code, mtrt_yymm;

  ExpirationDatesModel.fromjson(Map<String, dynamic> json)
      : mtrt_yymm_code = json['mtrt_yymm_code'],
        mtrt_yymm = json['mtrt_yymm'];
}
