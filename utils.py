from os import remove
from sympy.logic.boolalg import to_cnf

def _to_cnf(proposition):
    if '<=>' in proposition:
        proposition = remove_bimplication(proposition)
    return to_cnf(proposition)


def remove_bimplication(proposition):
    if proposition.count('<=>') > 1: raise Exception('Maximum allowed bi-implications reached per proposition')

    [left, right] = proposition.split('<=>')
    new_proposition = f'({left}>>{right})&({right}>>{left})'
    return new_proposition
