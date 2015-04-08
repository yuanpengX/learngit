#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import mlpy
x = [[1,8],[3,20],[1,15],[3,15],[5,35],[4,40],[7,80],[6,69]];
y = [1,1,0,0,1,0,0,1];
showpoint = ['ro','bo'];
tshowpoint = ['r*','b*'];
x = np.array(x);
y = np.array(y);
svm = mlpy.LibSvm();
svm.learn(x,y);
lp_x1 = x[:,0];
lp_x2 = x[:,1];

xmin,xmax = np.min(lp_x1)-1,np.max(lp_x1)+1;
ymin,ymax = np.min(lp_x2)-1,np.max(lp_x2)+1;

plt.subplot(111);
plt.xlabel(u"x");
plt.xlim(xmin,xmax);
plt.ylabel(u"y");
plt.ylim(ymin,ymax);

for ii in xrange(0,len(x)):
	ty = svm.pred(x[ii]);
	plt.plot(lp_x1[ii],lp_x2[ii],showpoint[int(ty)]);

tlp_x1 = np.random.rand(50)*(xmax-xmin)+xmin;
tlp_x2 = np.random.rand(50)*(ymax-ymin)+ymin;
tlp_x = np.array(zip(tlp_x1,tlp_x2));

for ii in range(0,len(tlp_x)):
	ty = svm.pred(tlp_x[ii]);
	plt.plot(tlp_x1[ii],tlp_x2[ii],tshowpoint[int(ty)]);
plt.show()
