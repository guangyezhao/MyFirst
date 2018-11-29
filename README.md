# 题目介绍
## 要求写一个可以生成数独终局并且可以求解数度问题的控制台程序
# 算法介绍
## 回溯 不管是生成终局还是求解问题 都是用到了回溯
```
# MyFirst
软件工程作业
#include "pch.h"
#include <iostream>
#include<math.h>
#include<random>
#include<string>
#include<fstream>
#include<time.h>
#include<stdlib.h>

using namespace std;
ofstream file1("终局.txt");
int a[9][9] = {4,0};//a里存放了每次我们查看终局里每个空的候选值
int zhongju[9][9] = {4,0};
int Line=0;//行
int Row=1;//列
int check(int row, int line,int *templ)//检查函数，查看这个点填上这个数字之后满足不满足要求
{
	int blocklinenum, blockrownum;
	blocklinenum = line / 3;//块行数
	blockrownum = row / 3;//块列数

	int startaddline = blocklinenum * 3;//块的起始行地址
	int startaddrow = blockrownum * 3;//块的起始列地址
	int i = 0; int j = 0;
	while (1)
	{
		if (j == 3)
		{
			j = 0;
			i++;
		}
		//if(zhongju[startaddline+i][startaddrow+j]==zhongju[line][row]&&line!= startaddline + i&& row!=startaddrow + j&&(startaddline+i < line || (startaddline +i== line && startaddrow +j< row)))
		if (((startaddline + i) * 9 + (startaddrow + j)) < (line * 9 + row))
		{
			templ[zhongju[startaddline + i][startaddrow + j] - 1] = 1;
			j++;
		}
		else
			break;
	}
	for (i = 0; i < line; i++)
	{
		templ[zhongju[i][row] - 1] = 1;
	}
	for (j = 0; j < row; j++)
	{
		templ[zhongju[line][j] - 1] = 1;
	}
	//int usespot = 1;//标识是否有可以用的值
	j = 0;
	for (i = 0; i < 9; i++)
	{
		if (templ[i] == 0)
		{
			//zhongju[line][row] = 0;
			j++;
		}
	}
	return j;
}
static int num=0;//已经生成的终局
static int flag = 1;
void Print(int x[9][9])
{//ofstream file1("终局.txt");
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9;j++)
		{
			file1<< x[i][j]<<" ";
	    }
		file1<<"\n";	
	}
	file1<<"\n";
	//file1.close();
}
void Print2()
{
}
void tianshu(int row,int line,int sum)//,row line==next
{
	//ofstream file1("终局.txt");
	int templ[9] = {0};//模板，每次清0，查看是否十个数都已经遍历过
	int sym =check(row, line, templ);
		int i;
		while (sym--)
		{
			for (i = 0; i < 9; i++)
			{
				if (templ[i] == 0)
				{
        templ[i] = 1;
		zhongju[line][row] = i + 1;
		break;
				}
			}
			if (row==8)
		{
			if (line==8)
			{
				Print(zhongju);
					num++;
					if (num == sum)
						flag = 0;
					return;
			}
			else
			{
				//row = 0;
				//line++;
				tianshu(0, line+1,sum);
				i = 0;
			}
		}
		else
		{
			//row++;
			tianshu(row+1, line,sum);
			i = 0;
		}
			if (flag == 0)
				break;
		}
}
int check2()
{

}
void jieti()
{

}
int main(int argc, char * argv[])
{	

}
```
