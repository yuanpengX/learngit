import re
import os
s = raw_input('please input expression:');
ss = re.split(r'[+-]',s);
l = len(ss);
index = len(ss[0]);
ans = long(ss[0]);
i =1;
while i<l:
	op1 = long(ss[i]) 
	
        op = s[index];
	index = index +1+len(ss[i]);

	if op == '+':
		ans = ans+op1;
	else:
		ans = ans-op1;

	i = i+1;
str = 'the answer is:'+str(ans);
print str;
