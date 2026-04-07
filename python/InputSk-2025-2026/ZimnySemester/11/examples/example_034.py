slovnik = {'cat':'macka', 'dog':'pes', 'my':'moj', 'good':'dobry', 'is':'je'}

def preklad(veta):
    vysl = []
    for slovo in veta.lower().split():
        vysl.append(slovnik.get(slovo, '<' + slovo + '>'))
    return ' '.join(vysl)