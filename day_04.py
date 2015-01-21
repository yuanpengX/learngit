#implementation of  switch in python
from __future__ import division 
def add(x,y):
	return x+y
def minus(x,y):
	return x-y
def div(x,y):
	return x/y
def mul(x,y):
	return x*y
def calc(x,o,y):
	print {'+':add,'-':minus,'/':div,'*':mul}.get(o)(x,y);

calc(3,'/',4);
	
