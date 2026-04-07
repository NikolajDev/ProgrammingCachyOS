>>> import calendar
>>> int(calendar.weekday(2025, 10, 12)) # 12.október 2025, vráti: 0=pondelok, 1=utorok, ... 6=nedela
    6
>>> calendar.day_name[calendar.weekday(2025, 10, 12)]
    'Sunday'
>>> calendar.prmonth(2025, 10, 3)      # október 2025, čísla na šírku 3 znaky
            October 2025
    Mon Tue Wed Thu Fri Sat Sun
              1   2   3   4   5
      6   7   8   9  10  11  12
     13  14  15  16  17  18  19
     20  21  22  23  24  25  26
     27  28  29  30  31