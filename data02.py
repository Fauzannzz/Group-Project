# Soal no 2

def baca_data02():
	file = open('data02.txt','r')
	read = file.read()
	file.close()
	return read

def main():
	file = baca_data02()
	data = tuple(map(int, file.split()))
	print(data)
	print('Tipe data :',type(data))
main()