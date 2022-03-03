# Soal no 6

def baca_data06():
    file = open("data06.txt", "r")
    dict_kosong = []
    for i in file:
        tim1, skor1, skor2, tim2 = i.split()
        dict_kosong.append({
            "Team 1": tim1,
            "Gol Dicetak Team 1": int(skor1),
            "Gol Dicetak Team 2": int(skor2),
            "Team 2": tim2,
        })
    file.close()
    return dict_kosong

def cari_pemenang(dict_kosong):
    if dict_kosong['Gol Dicetak Team 1'] > dict_kosong['Gol Dicetak Team 2']:
        dict_kosong['hasil'] = 'Team'+ " " + dict_kosong['Team 1'] + " " + "menang"
    elif dict_kosong['Gol Dicetak Team 1'] < dict_kosong['Gol Dicetak Team 2']:
        dict_kosong['hasil'] = 'Team'+ " " + dict_kosong['Team 2'] + " " + "menang"
    else:
        dict_kosong['hasil'] = 'Pertandingan Seri'


    return dict_kosong
def main():
    list_siswa = baca_data06()
    nilai_siswa = list(map(cari_pemenang, list_siswa))
    print(nilai_siswa)
    print(type(nilai_siswa))
main()