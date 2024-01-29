import sys
input = sys.argv[1]
output = sys.argv[2]
ths = int(sys.argv[3])

def write_img(pixels, type):
	imagem = open(output, 'w')
	imagem.write(f'{type}\n{size}\n{colors_interval}\n')
	for line in pixels:
		imagem.write(f'{line}\n')
	imagem.close()	
	return

def threshold(img):
	for i in range(len(img)):
		if img[i] >= ths:
			img[i] = colors_interval
		else: 
			img[i] = 0

pixels_line = []
img = []

imagem = open(input, 'r')

for linha in imagem:
	# Remove quebras de linha
	if '\n' in linha:
		linha = linha.replace('\n', '')
	# Ignora linhas de cabeçalho e comentários 
	if not ('P' in linha) and not ('#' in linha):
		pixels_line.append(linha)

imagem.close()

# Removendo linha relativa ao tamanho da imagem e intervalo de cores
size = pixels_line.pop(0)
colors_interval = pixels_line.pop(0)

img = list(map(int, pixels_line))

# Aplicação de efeitos
threshold(img)

write_img(img, 'P2')