#include<iostream>
#include<cstring>
using namespace std;

int KMP(char *s,char *p,int f[])
{
	int i,j;
	int n = strlen(s),m = strlen(p);
	i = 0;
	j = 0;
	while(i<n-m+1)
	{
		if(s[i]==p[j])
		{
			if(j == m-1)
			{
				return i-m+1;	
			}
			j++;
			i++;
		}
		else if(j>0)
			{
				j = f[j-1];
			}
		else
		{
			j=0;
			i++;
		}
	}	
return -1;
}

void failure(int f[],char *p)
{
	int i = 1,j=1;
	int m = strlen(p);
	f[0] = 0;
	while(i<m)
	{
		if(p[j]==p[i])
		{	
			i++;
			j++;
			f[i] = j+1;
		}
		else if(j>0)
			{
				j = f[j-1];
			}
		else 
		{
			f[i] = 0;
			i++;	
		}
	}
}


int main()
{
	char s[] = "idongtfdsakfjsd";
	char p[] = "tfdsa";
	int f[100];
	failure(f,p);
	cout<<KMP(s,p,f)<<endl;
	return 0;
}

