import cv2;
import numpy as np;

def get_Euclidean(x,y):
	myx = np.array(x);
	myy = np.array(y);
	return np.sum((myx-myy)*(myx-myy));

fn = "test1.jpeg";

if __name__ == "__main__":
	myimg = cv2.imread(fn);
	w = myimg.shape[1];
	h = myimg.shape[0];
	myimg2 = np.zeros((h,w,3),np.uint8);
	black = np.array([0,0,0]);
	white = np.array([255,255,255]);
	center = np.array([125,125,125]);
	for y in xrange(0,h-1):
		for x in xrange(0,w-1):
			mydown = myimg[y+1,x,:];
			myright = myimg[y,x+1,:];
			myhere = myimg[y,x,:];
			lmyhere = myhere
			lmyright = myright;
			lmydown = mydown;
			if get_Euclidean(lmyhere,lmydown)>16 and get_Euclidean(lmyhere,lmyright)>16:
				myimg2[y,x,:]=black;
			elif get_Euclidean(lmyhere,lmydown)<=16 and get_Euclidean(lmyhere,lmyright)<=16:
				myimg2[y,x,:] = white;
			else:
				myimg2[y,x,:] = center;
	cv2.namedWindow('img2');
	cv2.imshow('img2',myimg2);
	cv2.waitKey();
	cv2.destroyAllWindows();
