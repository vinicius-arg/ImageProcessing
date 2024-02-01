def slice(img: object):
    planes = [list(bin(x)[2:].zfill(8)) for x in img.pixels]
    sliced_planes = [[] for x in range(8)]
    for i in range(8):
        for bits in planes:
            sliced_planes[i].append(int(bits[i]))
    return sliced_planes