import os

def sef(pattern,alter,filename1,filename2):
	print pattern
	try:
		fp1 = open(filename1,'r');
		fp2 = open(filename2,'w');
		str1 = fp1.read();
		while (str1!=''):
			print str1
			if (cmp(str1,pattern)==0):
				fp2.write(alter);
			else:
				fp2.write(str1);
			str1 = fp1.read();
	except:
		print 'something went wrong';
sef('hello','nonono','test1','test2');

