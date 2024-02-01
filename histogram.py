import matplotlib.pyplot as plt

def get(img: object):
	histogram = []
	pixels = img.pixels
	for k in range(img.range + 1):
		histogram.append(pixels.count(k))
	return histogram

def normalize(histogram):
	return list(map(lambda x: x / sum(histogram), histogram))

def accumulate(histogram, colors=256):
	acc = []
	norm_hist = normalize(histogram)
	for i in range(colors):
		acc.append(sum(norm_hist[0:i]))
	return acc

def colorize(img, histogram):
	acc_hist = accumulate(histogram)
	return (list(map(lambda x: round(x*img.range), acc_hist)))

def equalize(img):
	pixels = img.pixels
	histogram = get(img)
	equalized = [0 for x in range(img.range + 1)]
	colors = colorize(img, histogram)
	for i in colors:
		equalized[i] += histogram.pop(0)
	
	return equalized

def show(histogram, colors=256):
	plt.bar([k for k in range(colors)], histogram, color="gray")
	plt.title("Histogram")
	plt.xlabel("Gray intensity values (R[k])")
	plt.show()