"""
Набор сервисных функций написанных для облегчения выполгнения домашних заданий.

Autror: 2022 Andrey Grey megagramm@gmail.com
"""
def rprint(string):
    """Формирует вывод текста на экран по правому краю"""
    eq_symb_len = 79-len(string)-1
    if eq_symb_len > 0:
        print(f'\n{"="*eq_symb_len} {string}\n')
    else:
        print(f'\n{string}\n')