import grayLevelSlicing as glvs
import ImportPicture as ip
import sys

input = sys.argv[1]
output = sys.argv[2]

img = ip.read(input)

sliced_planes = glvs.slice(img)
img1 = ip.Image('P1', sliced_planes[4], img.size, img.rows, img.columns, 1, input)

img1.write(output)