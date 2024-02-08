import blur
import ImportPicture as ip
import sys

input = sys.argv[1]
output = sys.argv[2]

img = ip.read(input)

px = blur.mean(img, 5)

blur_img = ip.Image(img.type, px, img.size, img.rows, img.columns, img.range, img.url)
blur_img.write(output)
