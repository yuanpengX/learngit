#include<iostream>
#include<cmath>
using namespace std;
template<class c>
bool qsort(c *array,int low,int high)
{
	if(low >= high)return false;
	int p1 = low,p2 = high;
	c tmp = array[p2];
	while(1)
	{
		while(array[p1]<=tmp&&p1<p2)p1++;
		if(p1 == p2)break;
	        array[p2] = array[p1];
		while(array[p2]>tmp&&p2>p1)p2--;
		if(p1 == p2)break;
		array[p1] = array[p2];
	}
	array[p1] = tmp;
	if(qsort(array,low,p1-1)&qsort(array,p1+1,high))return true;
}

int main()
{
	int a[]={1,34,32,2,325,243,236,34,5,3,2};
	qsort(a,0,10);
	for(int i = 0;i<11;i++)cout<<a[i]<<endl;
	return 0 ;
}
