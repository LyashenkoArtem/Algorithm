import hashlib

def is_eq_str(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Строки постые!'
    assert len(s) >= len(subs), 'Подстрока длиннее строки'


    len_sub = len(subs)
    h_sub = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_sub == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            if h_sub[i:i + len_sub] == subs:

                return i

    return -1

s_1 = input('1 ')
s_2 = input('2 ')
pos = is_eq_str(s_1, s_2)

print(f'Подстрока в позиции {pos}' if pos != -1 else 'Подстрока не найдена')