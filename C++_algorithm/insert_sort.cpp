#include<iostream>
#include<cmath>

template<class c>
bool insert_sort(c *array,int low,int high)
{
	int j;
	if(high<=low)return false;
	for(int i= low+1;i<=high;i++)
	{
		c tmp = array[i];
		for(j = i-1;j>0;j--)
		{
			if(array[j]>tmp)array[j+1] = array[j];
			else break;
		}
		array[j+1] = tmp;
	}
	return true;
}
using namespace std;
int main()
{
	int a[]={1,3,45,3,4,532,324,322,2};
	insert_sort(a,0,8);
	for(int i =0;i<=8;i++)cout<<a[i]<<endl;
	return 0;
}
