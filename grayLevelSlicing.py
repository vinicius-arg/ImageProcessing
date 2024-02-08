import ImportPicture as ip

def slice(img: object):
    planes = [list(bin(x)[2:].zfill(8)) for x in img.array()]
    sliced_planes = [[] for x in range(8)]
    for i in range(8):
        for bits in planes:
            sliced_planes[i].append(int(bits[i]))
    return sliced_planes

def zip(planes: list[list], a, b):
    img_size = len(planes[0])
    zipped_planes = planes[a:b]
    levels = [[] for x in range(img_size)]
    for i in range(img_size):
        for bit_array in zipped_planes:
            levels[i].append(str(bit_array[i]))
    levels = [f"0b{''.join(x):0<{8}}" for x in levels ]
    levels = [int(x,2) for x in levels]
    return levels

# Precisa de ajuste
def compress(img, a=0, b=4):
    planes = slice(img)
    levels = zip(planes, a, b)
    return ip.Image(img.type, levels, img.size, img.rows, img.columns, img.range, img.url)