'''First task'''
if __name__ == '__main__':
    STRENG = input('Ввод: ')
    print(''.join(chr(ord(i) + 1) for i in STRENG))
