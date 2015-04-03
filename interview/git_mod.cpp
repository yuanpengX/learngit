#include<iostream>
#include<cstring>
#include<windows.h>
#include<ctime>
#include<conio.h>

const int N = 1000;
typedef struct history
{
	int top;
	t_time *t[N];
}HIS;

void commit(HIS &his)
{
	char command[100];
	sprintf(command,"copy foobar.txt %d.txt",(his.top)+1);
	system(command);
	cout<<"new version "<<(his.top++)<<" created"<<endl;
}

void history(HIS &his)
{
	int id = his.top;
	while(id>0)
	{
		struct tm *t = gmtime(his.t[id]);
		cout<<t->tm_year<<"-"<<t->tm_mon<<"-"<<t->tm_day;
		cout<<" "<<t->tm_hour<<":"<<t->tm_min<<":"<<t->tm_sec<<" "<<id<<endl;	
	}	
}

void rollback(int ver)
{
	char command[100];
	sprintf(command,"copy %d.txt foobar.txt");
	system(command);
	cout<<"rollback "<<ver<<endl;
}

int main()
{
	char ch;
	HIS his;
	his.top = 0;
	while(1)
	{
		ch = getch();
		system("cls");
		if(ch==27)//command mode
		{
			char command[100];
			cin>>command;
			if(!strcmp(command,"commit"))commit(his);
			else if(!strcmp(command,"history"))history(his);
				else if(!strcmp(command,"rollback")){int id;cout<<ID;cin>>id;rollback(id);}
				else{cout<<"mode error";}		
		}
		else
		{
			ofstream file("foobar.txt");
			cout<<"please input file context";
			char context[10000];
			file.write(context,strlen(context));
			file.close();
		}
	}
	return 0;
}
