>>> time.localtime()
    time.struct_time(tm_year=2019, tm_mon=11, tm_mday=27, tm_hour=8, tm_min=53, tm_sec=53, tm_wday=2, tm_yday=331, tm_isdst=0)
>>> time.localtime()[:3]        # momentálny dátum v tvare (rok, mesiac, deň)
    (2019, 11, 27)
>>> time.localtime()[3:6]       # momentálny čas v tvare (hodiny, minúty, sekundy)
    (8, 54, 17)
>>> time.localtime()[6]         # momentálny deň v týždni, kde pondelok má hodnotu 0, teda 2 označuje stredu
    2