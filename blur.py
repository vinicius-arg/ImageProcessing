import numpy as np
import ImportPicture as ip

def mean(img, order):
    pixels = np.zeros((img.rows, img.columns), dtype=np.int32)
    # Coeficiente de máscara
    w = 1 / order**2
    # Ordem da máscara
    m = n = order
    # Constantes de deslocamento
    a = b = int((order-1) / 2)

    for m in range(a+1, img.rows):
        for n in range(b+1, img.columns):
            for s in range(-a, a+1):
                for t in range(-b, b+1):
                    pixels[m-a][n-b] += w*(img.pixels[m+s-a][n+t-b])
    return pixels

def apply(img):
    return ip.Image(img.type, mean(img.pixels,3), img.size, img.rows, img.columns, img.range, img.url)