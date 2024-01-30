import matplotlib.pyplot as plt

def getHistogram(img):
	unnorm_hist = [0 for k in range(img.range)]
	for k in range(img.range):
		unnorm_hist[k] = img.count(k)
	return list(map(lambda x: x / img.pixels, unnorm_hist))

def showHistogram(histogram, colors=255):
	plt.bar([k for k in range(colors)], histogram, color="gray")
	plt.title("Normalized histogram")
	plt.xlabel("Gray intensity values (R[k])")
	plt.show()