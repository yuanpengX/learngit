'''
#spider

import urllib
import re
set_url = raw_input("please input url:");
page = urllib.urlopen(set_url).read();
rr = re.compile(r'src="(.*?.\jpg) width"');
imglist = rr.findall(page);
x = 1;
for url in imglist:
	urllib.retrieve(url,'%s.jpg'%x);
	x+=1;
'''

'''
#file operation in python

f_p = open('/home/diao/github/diao','a+');
ss = f_p.read()
print ss;
f_p.write('bufdsfdsadsfse python');
f_p.close()

'''

import os
#os.mkdir('/home/diao/github/diaodiao');
print os.listdir(os.getcwd());
