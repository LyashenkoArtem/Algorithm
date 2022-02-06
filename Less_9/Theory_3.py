import hashlib

def is_eq_str(a: str, b: str, verbose = False) -> bool:
    assert len(a) > 0 and len(b), 'Строки пустые!'
    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbose:
        print(f'hash 1 = {ha}\nhash 2 = {hb}')

    return ha == hb

s_1 = input('1 ')
s_2 = input('2 ')

print('Строки одинаковые' if is_eq_str(s_1, s_2, True) else 'Строки разные')