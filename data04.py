# Soal no 4

def baca_data04():
	file = open('data04.txt','r')
	read = file.read().split()
	file.close()
	return read

def main():
	list_data = []
	file = baca_data04()
	data = list(map(int, file))
	list_data.extend(data)
	print(list_data)
	print('Tipe data :',type(list_data))
main()