import numpy as np

class Image:
	def __init__(self, type:str, pixels, size:int, rows:int, columns:int, range:int, url:str):
		self.type = type
		self.pixels = pixels
		self.size = size
		self.rows = rows
		self.columns = columns
		self.range = range
		self.url = url

	def array(self):
		return list(sum(self.pixels, []))

	def write(self, output:str):
		img = open(output, 'w')
		if self.type == 'P1':
			img.write(f'{self.type}\n{self.columns} {self.rows}\n')
		else:
			img.write(f'{self.type}\n{self.columns} {self.rows}\n{self.range}\n')
		for row in self.pixels:
			for column in row:
				img.write(f'{column}\n')
		img.close()

def read(input):
	FILE = open(input, 'r')
	pixels = []

	for line in FILE:
		# Removendo quebras de linha
		if '\n' in line:
			line = line.replace('\n', '')
		# Ignorando linhas de comentários 
		if not ('#' in line):
			pixels.append(line)

	FILE.close()
	# Extraindo metadados
	type = pixels.pop(0)
	size_line = list(map(int, pixels.pop(0).split()))
	rows = size_line[0]
	columns = size_line[1]
	size = rows * columns
	px = np.zeros((rows,columns), dtype=np.int32)
	color_range = int(pixels.pop(0))
	# Mapeando pixels em matriz
	index = 0
	pixels = list(map(int, pixels))
	
	for m in range(rows):
		for n in range(columns):
			px[m][n] = pixels[index]
			index+=1
	
	return Image(type, px, size, rows, columns, color_range, input)

img = read('./Assets/barco.pgm')
# img.array()