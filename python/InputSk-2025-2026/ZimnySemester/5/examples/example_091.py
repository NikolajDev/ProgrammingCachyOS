>>> abc = ['raz', 'dva', 'tri']
>>> abc.insert(10, 'koniec')
>>> abc
    ['raz', 'dva', 'tri', 'koniec']
>>> abc.insert(2, 'stred')
>>> abc
    ['raz', 'dva', 'stred', 'tri', 'koniec']
>>> abc.insert(0, 'zaciatok')
>>> abc
    ['zaciatok', 'raz', 'dva', 'stred', 'tri', 'koniec']
>>> abc.insert(-1, 'predposledny')
>>> abc
    ['zaciatok', 'raz', 'dva', 'stred', 'tri', 'predposledny', 'koniec']