import grayLevelSlicing as glvs
import ImportPicture as ip
import sys

input = sys.argv[1]
output = sys.argv[2]

img = ip.read(input)

sliced_planes = glvs.slice(img)
img1 = glvs.zip(img, sliced_planes, 0, 5)
img2 = ip.Image(img.type, img1, img.size, img.rows, img.columns, img.range, input)

img2.write(output)