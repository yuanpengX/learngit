import cv2
import numpy as np;

#set basic param
fn = "test.jpg";
m = 0;
alpha = 0.7;

#get picture
c0 = cv2.imread(fn);
cc = cv2.cvt(c0,BGR2GRAY);
sh = c0.shape;
cv2.imshow('cover',c0);
#set w_r
w = c0.copy();
w[:,:,:] = 255;
for i in range(sh[0]):
	for j  in range(sh[1]):
		w[i,j,1] = np.random.randint(255);
#add watermarking
w_m = (2*m-1)*w;
w_n = alpha*w_m;
print w_n[1,1,1]
print c0[1,1,1];
c = w_n+c0;
print c[1,1,1]
cv2.imshow('watermarking',w_n);
#show pic 
cv2.imshow('addedpic',c);

#exit
cv2.waitKey();
cv2.destroyAllWindows();
