import diff
import ImportPicture as ip
import sys

input = sys.argv[1]
input2= sys.argv[2]
output = sys.argv[3]

img1 = ip.read(input)
img2 = ip.read(input2)

img3 = diff.getSub(img1, img2)
img3.write(output)