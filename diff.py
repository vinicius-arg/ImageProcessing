import ImportPicture as ip

def compare(A: object, B: object):
    pixels = [x for x in range(A.size)]
    if A.rows == B.rows and A.columns == B.columns:
        for i in range(A.size):
            pixels[i] = A.pixels[i] - B.pixels[i]
            if (pixels[i] < 0):
                pixels[i] = 0
    else:
        print("\n**Erro: Imagens de tamanho diferente.") 
    return pixels

def getSub(A, B):
    pixels = compare(A, B)
    return ip.Image(A.type, pixels, A.size, A.rows, A.columns, A.range, A.url)