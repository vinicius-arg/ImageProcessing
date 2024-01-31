class Image:
	def __init__(self, type:str, pixels, size:int, range:int, url:str):
		self.type = type
		self.pixels = pixels
		self.size = size
		self.range = range
		self.url = url
		
	def write(self, output:str):
		img = open(output, 'w')
		if self.type == 'P1':
			img.write(f'{type}\n{self.size}\n')
		else:
			img.write(f'{type}\n{self.size}\n{self.range}\n')
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
	size = pixels.pop(0)
	color_range = pixels.pop(0)
	# Mapeando pixels em vetor
	img = list(map(int, pixels))

	return Image(type, img, size, color_range, input)