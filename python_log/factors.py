from __future__ import division
import math
kk = int(raw_input('please input number:'));

def is_prim(num):
	a = 2;
	while a <= math.sqrt(num):
		if num%a == 0:
			return False;
		a= a+1;
	return True;

def factor(num,k):
	if is_prim(num):
		k.append(int(num));
	else:
		tmp = 2;
		while tmp<num:
			if num%tmp==0:
				k.append(tmp)
				factor(num/tmp,k);
				break;
			else: tmp=tmp+1;
k = [];
factor(kk,k);
print k

