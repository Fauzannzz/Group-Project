# Soal no 3

def baca_data03():
	file = open('data03.txt','r')
	read = file.read()
	file.close()
	return read

def main():
	my_set = set()
	file = baca_data03()
	data = set(map(int, file.split()))
	my_set.update(data)
	print(my_set)
	print('Tipe data :',type(my_set))
main()