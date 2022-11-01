def rprint(string):
    """Формирует вывод текста на экран по правому краю"""
    eq_symb_len = 79-len(string)-1
    if eq_symb_len > 0:
        print(f'\n{"="*eq_symb_len} {string}\n')
    else:
        print(f'\n{string}\n')