#include<iostream>
#include<cstring>
using namespace std;

template<class c>
int LCS(c *s,c *p)
{
	int m = strlen(s)-1,n = strlen(p)-1;
	int l[100][100];
	for(int i = 0;i<=m;i++)
	l[i][0] = 0;
	for(int j = 0;j<=n;j++)
	l[0][j] = 0;
	for(int i = 1;i<=m;i++)
		for(int j = 1;j<=n;j++)
			{
				if(s[i]==p[j])l[i][j] = l[i-1][j-1]+1;		
				else{l[i][j] = l[i-1][j]>l[i][j-1]?l[i-1][j]:l[i][j-1];}
			}
	return l[m][n];
}

int main()
{
	char a[11] = {1,1,243,5,4,34,23,53,224,52,3};
	char b[11] = {1,1,223,5,32,4,32,53,242,3,23};
	cout<<LCS(a,b)<<endl;
}
