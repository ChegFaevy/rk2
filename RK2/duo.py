'''Second task'''
if __name__ == '__main__':
    STRUNG = ''
    with open('stdin.txt', 'r', encoding = 'utf-8') as file:
        STRUNG = file.readline()
    with open('stdout.txt', 'w', encoding = 'utf-8') as file:
        file.write(''.join(chr(ord(i) + 1) for i in STRUNG))
        