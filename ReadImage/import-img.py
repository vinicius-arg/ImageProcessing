import sys
input = sys.argv[1]
output = sys.argv[2]

def write_img(pixels, type):
	imagem = open(output, 'w')
	lines = len(pixels)
	columns = len(pixels[0])
	imagem.write(f'{type}\n{columns} {lines}\n')
	for line in pixels:
		for pixel in line:
			imagem.write(f'{pixel} ')
		imagem.write('\n')
	imagem.close()	
	return

pixels_line = []
pixel = []

imagem = open(input, 'r')

for linha in imagem:
	# Remove quebras de linha
	if '\n' in linha:
		linha = linha.replace('\n', '')
	# Ignora linhas de cabeçalho e comentários 
	if not ('P' in linha) and not ('#' in linha):
		pixels_line.append(linha)

imagem.close()
# Removendo linha relativa ao tamanho da imagem		
pixels_line.pop(0)

for line in pixels_line:
	# Guarda os valores numéricos em temp
	temp = [int(px) for px in line if px.isdigit()]
	pixel.append(temp)
	
write_img(pixel, 'P1')