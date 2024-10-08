#  datetime_helper.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2023.

import datetime as dt
from typing import Final

TIMEGAMMA_KST: Final = "+09:00"
TIMEZONE_KST: Final = dt.timezone(dt.timedelta(hours=9), 'Asia/Seoul')


def dt_utc_strptime_kst(dt_string: str, dt_format: str) -> dt.datetime:
    """(타임존이 없으면 KST로 가정한다) 문자열 형식날짜 -> 표준날짜시간"""
    dtm = dt.datetime.strptime(dt_string, dt_format)
    if not dtm.tzname():
        dtm = dtm.replace(tzinfo=TIMEZONE_KST)
    return dtm.astimezone(dt.timezone.utc)


def dt_utc_iso_strptime_kst(dt_string: str, dt_format: str) -> str:
    """(타임존이 없으면 KST로 가정한다)문자열 형식날짜 -> 표준날짜시간 문자열로 반환"""
    return dt_utc_strptime_kst(dt_string, dt_format).isoformat()


def dt_utc_today_begin() -> dt.datetime:
    """오늘 날짜의 시작시간을 UTC 시간으로 반환. 예) 2023.11.24 00:00:00+09:00 -> 2023-11-23 15:00:00+00:00"""
    return dt.datetime.combine(dt.date.today(), dt.time()).astimezone(dt.timezone.utc)


def dt_utc_today_end() -> dt.datetime:
    """오늘 날짜의 종료시간을 UTC 시간으로 반환. 예) 2023.11.24 23:59:59+09:00 -> 2023-11-24 14:59:59.999999+00:00"""
    return dt.datetime.combine(dt.date.today(), dt.time(23, 59, 59, 999999)).astimezone(dt.timezone.utc)
