class HolidayModel {
  final String bass_dt, wday_dvsn_cd, bzdy_yn, tr_day_yn, opnd_yn, sttl_day_yn;

  HolidayModel.fromjson(Map<String, dynamic> json)
      : bass_dt = json['bass_dt'], // 기준일자(YYYYMMDD)
        wday_dvsn_cd =
            json['wday_dvsn_cd'], // 01:일, 02:월, 03:화, 04:수, 05:목, 06:금, 07:토
        bzdy_yn = json['bzdy_yn'], // 금융기관이 업무를 하는 날
        tr_day_yn = json['tr_day_yn'], // 증권 업무가 가능한 날(입출금, 이체 등의 업무 포함
        opnd_yn = json['opnd_yn'], // 주식시장이 개장되는 날
        sttl_day_yn = json['sttl_day_yn']; // 주식 거래에서 실제로 주식을 인수하고 돈을 지불하는 날
}
