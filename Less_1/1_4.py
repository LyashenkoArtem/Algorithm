'''
Пользователь вводит две буквы.
Определить, на каких местах алфавита
они стоят, и сколько между ними находится букв.
'''


let_1 = input('Введите букву: ')
let_2 = input('Введите вторую букву: ')
if let_1 == let_2:
    print('Вы ввели одинаковые символы!')
else:
    let_1a = ord(let_1)
    let_2a = ord(let_2)

    num_1 = let_1a - 96
    num_2 = let_2a - 96

    if num_1 < num_2:
        pass
    else:
        let_1a, let_2a = let_2a, let_1a

    num_3 = let_2a - let_1a - 1

    print(f'Символ {let_1} находится на {num_1} месте,\n'
          f'Символ {let_2} находится на {num_2} месте,\n'
          f'Расстояние между ними {num_3} символов')