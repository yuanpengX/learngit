#include<iostream>
#include<cmath>
using namespace std;

template<class c>
bool merge_sort(c *array,int low,int high)
{
	if(low>=high)return false;
	int mid = round((low+high)/2);
	merge_sort(array,low,mid);
	merge_sort(array,mid+1;high);
}
