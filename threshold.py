def threshold(img, limit):
	for i in range(len(img)):
		if img[i] >= limit:
			img[i] = img.range
		else: 
			img[i] = 0