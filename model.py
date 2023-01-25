import random
import view as v
def get_spis():
    return read_from_file()



def generator_pas(l_length):
    letters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X",
           "C",
           "V", "B", "N", "M", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j",
           "k",
           "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-",
           "_"]  # список всех символов]
    while True:
        gened_pas = ""
        len_len = int(l_length)
        for i in range(0, len_len, 1):
            x = random.choice(letters)
            gened_pas += str(x)
        if verif(gened_pas):
            continue
        else:
            print(gened_pas)
            return gened_pas


def verif(l_password):
    ch_under = "_"  # символ "_"
    ch_mins = "-"  # символ "-"
    if ch_under in l_password and ch_mins in l_password and any(ch.isdigit() for ch in l_password):
        return False
    else:
        return True


def read_from_file():
    l_spis = []
    rd_file = open('password\password.txt', 'r')
    for line in rd_file:
        if not (line == '\n'):
            l_spis.append(line.rstrip("\n"))
    rd_file.close()
    return l_spis


def enter(spis, services):
    serv_name = services
    if serv_name == "" or serv_name == " ":
        print("\nНазвание сервиса не должно быть пустым!")
        enter()
    else:
        pas_i = search_password(serv_name)
        if pas_i >= 0:
            print("\n\nУ вас уже имеется пароль от данного сервиса.", "-------", serv_name)
            print("Ваш пароль: " + spis[pas_i])
        else:
            password = create_password()
            writing_to_file(serv_name, password)
            print("\nСервис: ", serv_name)
            print("Сгенерированный пароль: ", password)


def search_password(spis, l_serv_name):
    print(spis)
    
    return spis.index(l_serv_name)+1 if l_serv_name in spis else -1


def create_password(lenght):
    while True:
        if lenght.isdigit():
            length = int(lenght) 
            if int(lenght) < 5:
                lenght = -5 
                continue
            elif int(lenght) >= 5:
                break
        else:
            lenght = -3
            #print("\tВведите длину пароля в цифрах!\n")
            continue
    return generator_pas(length)


def writing_to_file(l_serv_name, pas_str):
    wr_file = open('password\password.txt', 'a+')
    wr_file.write(l_serv_name.rstrip())
    wr_file.write("\n")
    wr_file.write(pas_str.rstrip())
    wr_file.write("\n\n")
    wr_file.close()
