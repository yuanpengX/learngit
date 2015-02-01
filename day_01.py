'''n = int(raw_input('please input a num:'));
sum = 0.0;
m = 1;
while m <= n:
	sum = sum + 1.0/m;
	m = m+1;
print sum;
s = 0.0;
print range(n);
for num in range(n):
	s=s+1.0/(num+1);
print s; 

ss = 0.0;
for x in range(101):
	ss = ss+x
print ss'''

'''
#here is code of find the oldest man
n = 2;
list = [];
i = 0;
tmp_na = 0;
tmp_a = 0;
print 'please input information for 2 person:name,age'
while i<n:
	print 'information of the man'
	tmp_na = raw_input();
	tmp_a = int(raw_input());
	list.append((tmp_na,tmp_a));
	i =i+1;
print list
max =0;
m = 0;
for l in list:
	if l[-1]> max:
		m = l;		
print m
'''

'''
#dead circle

while True :
	print 304
'''


