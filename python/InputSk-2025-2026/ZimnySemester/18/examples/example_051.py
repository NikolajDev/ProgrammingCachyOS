>>> zoz = ('Prvy', 'DRUHY', 'druha', 'pRva', 'PRVE', 'druhI')
>>> sorted(zoz)
    ['DRUHY', 'PRVE', 'Prvy', 'druhI', 'druha', 'pRva']
>>> sorted(zoz, key=str.lower)
    ['druha', 'druhI', 'DRUHY', 'pRva', 'PRVE', 'Prvy']
>>> sorted(zoz, key=lambda s: s.lower())
    ['druha', 'druhI', 'DRUHY', 'pRva', 'PRVE', 'Prvy']