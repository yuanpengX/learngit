#include<iostream>
#include<cmath>
using namespace std;


template<class c>
void adjust(c *h,int head,int n)
{
	int i;
	if(head*2>n)return;
	if(head*2+1<=n)
	i = h[head*2]<h[head*2+1]?head*2:head*2+1;
	else
	i = head*2;
	if(h[i]<h[head])
	{
		c tmp = h[head];
		h[head] = h[i];
		h[i] = tmp;
		adjust(h,i,n);
	}
}

template<class c>
void heap(c *h,int n)
{
	int head = round(n/2);
	while(head>0)
	{
		adjust(h,head--,n);
		disp(h);
	}	

}

int main()
{
	int a[11] = {0,2332,343,43244,435,36,47,438,9,13,2};
	heap(a,10);
	disp(a);
	return 0;
}
