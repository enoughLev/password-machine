import random


def get_spis():
    return read_from_file()


def generator_pas(l_length): #l_length: int - не работает в строке 27. Ругается, что l_length не является INT
    l_length = int(l_length) 
    def verif(l_password: str):
        ch_under = "_"  # символ "_"
        ch_mins = "-"  # символ "-"
        if ch_under in l_password and ch_mins in l_password and any(ch.isdigit() for ch in l_password):
            return False
        else:
            return True

    letters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X",
           "C",
           "V", "B", "N", "M", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j",
           "k",
           "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-",
           "_"]  # список всех символов]
    while True:
        #gened_pas: str - не работает в строке 28. Говорит, что не работает без объявления переменной
        gened_pas = ""
        for i in range(l_length): 
            gened_pas += random.choice(letters)
        if verif(gened_pas): 
            continue
        else: 
            return gened_pas


def search_password(spis: list, l_serv_name: str):
    return spis.index(l_serv_name) + 1 if l_serv_name in spis else 0


def read_from_file():
    l_spis = []
    rd_file = open('password\password.txt', 'r')
    for line in rd_file: 
        if not (line == '\n'): l_spis.append(line.rstrip("\n"))
    rd_file.close()
    return l_spis


def writing_to_file(l_serv_name, pas_str):
    wr_file = open('password\password.txt', 'a+')
    wr_file.write(l_serv_name.rstrip())
    wr_file.write("\n")
    wr_file.write(pas_str.rstrip())
    wr_file.write("\n\n")
    wr_file.close()
