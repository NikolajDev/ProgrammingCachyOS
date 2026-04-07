def quick_sort(zoz):
    if len(zoz) < 2:
        return zoz
    pivot = zoz[0]
    mensie = [prvok for prvok in zoz if prvok < pivot]
    rovne =  [prvok for prvok in zoz if prvok == pivot]
    vacsie = [prvok for prvok in zoz if prvok > pivot]
    return quick_sort(mensie) + rovne + quick_sort(vacsie)