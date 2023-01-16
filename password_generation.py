import random

letters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X",
           "C",
           "V", "B", "N", "M", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j",
           "k",
           "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-",
           "_"]  # список всех символов]
ch_under = "_"  # символ "_"
ch_mins = "-"  # символ "-"


def generator_pas(l_length):
    while True:
        gened_pas = ""
        for i in range(0, l_length, 1):
            x = random.choice(letters)
            gened_pas += str(x)
        if verif(gened_pas):
            continue
        else:
            return gened_pas


def verif(l_password):
    if ch_under in l_password and ch_mins in l_password and any(ch.isdigit() for ch in l_password):
        return False
    else:
        return True


def read_from_file():
    l_spis = []
    rd_file = open('password\password.txt', 'r')
    for line in rd_file:
        l_spis.append(line.rstrip(":\n"))
    rd_file.close()
    return l_spis


def enter():
    serv_name = input("\nВведите название сервиса: ")
    serv_name = serv_name.lower()
    if serv_name == "" or serv_name == " ":
        print("\nНазвание сервиса не должно быть пустым!")
        enter()
    else:
        pas_i = search_password(serv_name) + 1
        if pas_i >= 0:
            print("\n\nУ вас уже имеется пароль от данного сервиса.", "-------", serv_name)
            print("Ваш пароль: " + spis[pas_i], "\n")
        else:
            password = create_password()
            writing_to_file(serv_name, password)
            print("\nСервис: ", serv_name)
            print("Сгенерированный пароль: ", password, "\n")


def search_password(l_serv_name):
    return spis.index(l_serv_name) if l_serv_name in spis else -2


def create_password():
    while True:
        length = input("Введите длину пароля: ")
        if length.isdigit():
            length = int(length)
            if length < 5:
                print("\nВнимание! Введите длину пароля не менее 5 символов. Рекомендуется 8 и более.\n")
                continue
            elif length >= 5:
                break
        else:
            print("\n----------ВНИМАНИЕ ОШИБКА----------!")
            print("\tВведите длину пароля в цифрах!\n")
            continue
    return generator_pas(length)


def writing_to_file(l_serv_name, pas_str):
    wr_file = open('password\password.txt', 'w')
    for i in range(len(spis)):
        wr_file.write(spis[i])
        wr_file.write("\n")
    wr_file.write(l_serv_name.rstrip())
    wr_file.write("\n")
    wr_file.write(pas_str.rstrip())
    wr_file.write("\n")
    wr_file.write("\n")
    wr_file.write("\n")
    wr_file.close()


spis = read_from_file()  # список для чтения из файла
enter()
