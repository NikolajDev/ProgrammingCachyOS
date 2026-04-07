>>> abc = 'Monty Python'
>>> abc[2:10:2]
    'nyPt'
>>> abc[::3]
    'MtPh'
>>> abc[9:-7:-1]
    'htyP'
>>> abc[::-1]
    'nohtyP ytnoM'
>>> abc[6:] + ' ' + abc[:5]
    'Python Monty'
>>> abc[4::-1] + ' ' + abc[:5:-1]
    'ytnoM nohtyP'
>>> (abc[6:] + ' ' + abc[:5])[::-1]
    'ytnoM nohtyP'
>>> 'kobyla ma maly bok'[::-1]
    'kob ylam am alybok'
>>> abc[4:9]
    'y Pyt'
>>> abc[4:9][2]          # aj podretazce mozeme dalej indexovat
    'P'
>>> abc[4:9][2:4]
    'Py'
>>> abc[4:9][::-1]
    'tyP y'