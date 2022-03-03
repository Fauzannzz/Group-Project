# Soal no 5

def baca_data05():
    file = open("data05.txt", "r")
    dict_kosong = dict()
    for i in file:
        a, b, c = i.split()
        data = list(map(int, [b,c]))
        dict_kosong.update({a : data})
    file.close()
    return dict_kosong

def main():
    data = baca_data05()
    print(data)
    print('Tipe data :',type(data))

main()