from __future__ import division
from math import sqrt
a = int(raw_input('please input lower bound:'));
b = int(raw_input('please input upper bound:'));
if a<3:
	a = 3;
while a <=b:
	k = round(sqrt(a))
	flag = 1;
	tmp = 2;
	while tmp<=k:
		if a%tmp == 0:
			flag = 0;
		tmp=tmp+1;
	if flag:
		print a;
	a = a+1;
