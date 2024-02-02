def slice(img: object):
    planes = [list(bin(x)[2:].zfill(8)) for x in img.pixels]
    sliced_planes = [[] for x in range(8)]
    for i in range(8):
        for bits in planes:
            sliced_planes[i].append(int(bits[i]))
    return sliced_planes

def zip(img, planes: list[list], a, b):
    zipped_planes = planes[a:b]
    levels = [[] for x in range(img.size)]
    for i in range(img.size):
        for bit_array in zipped_planes:
            levels[i].append(str(bit_array[i]))
    levels = [f"0b{''.join(x):0<{8}}" for x in levels ]
    levels = [int(x,2) for x in levels]
    return levels