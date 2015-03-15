import cv2
import numpy as np

if __name__ == '__main__':
	sz1 = 200;  #raw
	sz2 = 300; #column
	print u'generate a empty image array(%d,%d)'%(sz1,sz2);
	img = np.zeros((sz1,sz2,3),np.uint8);
	pos1 = np.random.randint(200,size=(2000,1));# rand row 
	pos2 = np.random.randint(300,size=(2000,1));# rand col
	for i in range(2000):
		img[pos1[i],pos2[i],[0]]=np.random.randint(0,255);
		img[pos1[i],pos2[i],[1]]=np.random.randint(0,255);
		img[pos1[i],pos2[i],[2]]=np.random.randint(0,255);
	cv2.imshow('snow image',img);
	cv2.waitKey();
	cv2.destroyAllWindows();
