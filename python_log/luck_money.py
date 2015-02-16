import random

def get_money(total,num):
        x = [0];
	for i in range(num-1):
		x.append(round((random.random())*total,2));
	x.sort();
	x.append(total)
	money  = [];
	for i  in range(num):
		money.append(x[i+1]-x[i]);
        return money

total = float(raw_input("please input total money:"));
num = int(raw_input("please input total num:"));
money = get_money(total,num);
n = 1;
for mon in money:
	print "the %d person get %.2f yuan"%(n,mon);
	n = n+1;

	
		




