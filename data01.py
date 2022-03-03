# Soal no 1

def baca_data01():
	file = open('data01.txt','r')
	read = file.read()
	file.close()
	return read

def main():
	file = baca_data01()
	data = list(map(int, file.split()))
	print(data)
	print('Tipe data :',type(data))
main()