>>> import time
>>> time.localtime()
    time.struct_time(tm_year=2017, tm_mon=11, tm_mday=22, tm_hour=8, tm_min=26, tm_sec=12,
    tm_wday=1, tm_yday=327, tm_isdst=0)
>>> time.localtime()[3:6]
    (8, 26, 24)