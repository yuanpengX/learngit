#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int low = 0,high = 17;
	int num[18] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18};
	int key = 2;
	int mid;
	int count = 0;
	while(low<high)
	{
		mid = floor((low+high)/2);
		count++;
		if(num[mid]==key) {cout<<count<<endl;break;}
		else if(num[mid]>key)
			{
				high=mid;
			}
			else low = mid;
	}
	return 0;
}
