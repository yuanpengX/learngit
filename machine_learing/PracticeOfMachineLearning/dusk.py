import cv2;
from numpy import *;

fn = "test.jpg";
img = cv2.imread(fn);
w = img.shape[0];
h = img.shape[1];
for i in range(w):
	for j in range(h):
		img[i,j,0] = int(img[i,j,0]*0.7);
		img[i,j,1] = int(img[i,j,1]*0.7);
cv2.imshow('dusk',img);
cv2.waitKey();
cv2.destroyAllWindows();
