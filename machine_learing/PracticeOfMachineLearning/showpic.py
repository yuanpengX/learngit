#!/usr/bin/env python

import cv2
fn = "test.jpg";

if __name__ == '__main__':
	print "load %s ..."%fn;
	img = cv2.imread(fn);
	cv2.imshow('my fist pictures show',img);
	cv2.waitKey();
	cv2.destroyAllWindows();
