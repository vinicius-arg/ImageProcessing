class Image:
	def __init__(self, type:str, pixels, size:int, rows:int, columns:int, range:int, url:str):
		self.type = type
		self.pixels = pixels
		self.size = size
		self.rows = rows
		self.columns = columns
		self.range = range
		self.url = url
		
	def write(self, output:str):
		img = open(output, 'w')
		if self.type == 'P1':
			img.write(f'{self.type}\n{self.columns} {self.rows}\n')
		else:
			img.write(f'{self.type}\n{self.columns} {self.rows}\n{self.range}\n')
		for line in self.pixels:
			img.write(f'{line}\n')
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
	color_range = int(pixels.pop(0))
	# Mapeando pixels em vetor
	pixels = list(map(int, pixels))
	
	return Image(type, pixels, size, rows, columns, color_range, input)