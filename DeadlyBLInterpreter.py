from PIL import Image
import random
import math

with open("brains.txt", "r") as f:
	z = f.readline().strip('\n')
	w = len(z) - 1
	print(w)
	if int(math.sqrt(w)) < math.sqrt(w):
		w = int(math.sqrt(w)) + 1
	else:
		w = int(math.sqrt(w))
	im = Image.new("RGB", (w, w))
	pix = im.load()
	v = 0
	bloller = {'>':(255,0,0), '<':(128,0,0), '+':(0,255,0), '-':(0,128,0), '.':(0,0,255), ',':(0,0,128), '[':(255,255,0), ']':(128,128,0)}
	for x in range(w):
		for y in range(w):
			try:
				print(v)
				if v >= len(z):
					pix[x,y] = (0,0,0)
				else:
					pix[x,y] = bloller[z[v]]
				v += 1
			except EOFError:
				pix[x,y] = (255,255,255)
im.save("fire.png", "PNG")