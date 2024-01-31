import matplotlib.pyplot as plt

def get(img, size):
	histogram = [0 for k in range(size)]
	for k in range(size):
		histogram[k] = img.count(k)
	return histogram

def normalize(histogram):
	return list(map(lambda x: x / sum(histogram), histogram))

def accumulate(histogram, colors=255):
	acc = []
	norm_hist = normalize(histogram)
	for i in range(colors):
		acc.append(norm_hist[0:i])
	return acc

def show(histogram, colors=255):
	plt.bar([k for k in range(colors)], histogram, color="gray")
	plt.title("Normalized histogram")
	plt.xlabel("Gray intensity values (R[k])")
	plt.show()