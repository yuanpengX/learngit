'''#!/usr/bin/pyton
def calc_diao():
	i = 1;
	while i<=9:
		j = 1;
		while j<=9:
			print "%d*%d=%d"%(i,j,i*j);
			j = j+1;
		print "\n";
		i = i+1;
calc_diao();'''	

'''
a = 100; #this is a global variant
def diaodiao():
	a = 200;  # here we have a local variant
	print a;
	global a # here is not just reset,we just cover global with local
        print a
diaodiao()
print a;
'''

'''
#test default value
def diao(x,y='hello'):
	print x,y
diao('diaodiao');
diao(4,'diaodiao');
'''

'''
#return value
def min_d(x,y,z):
	if x>y: 
		if y>z:
			return z;
		else:
			return y;
	else:
		if x>z:
			return z;
		else:
			return x; 
m = min_d(4,6,1);
print m;
'''

'''
#variant in python is just regarded as one thing
#how to print elemets in a list?

def fun(x,y):
	print "%d,%d" % (x,y)

l = [2,3];
fun(*l) #to print eles in list
fun(y=10,x=100);  #something called key world param,actualy dic was passed here
which is regarded as maping
d = {'y':100,'x':20}; # use eles in dic, python will match auto
fun(**d);
'''

#has nothing to do with the order 
# how to deal with spare params
def fun(x,*arg):
	print x
	print arg
def fun1(d,**dd):
	print d;
	print dd;
fun(1,23,3,4,354);
fun1(1,a=243434,k=45);
fun1(1,z=34);

