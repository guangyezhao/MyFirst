# 题目介绍
## 要求写一个可以生成数独终局并且可以求解数度问题的控制台程序

# 算法介绍
## 回溯 不管是生成终局还是求解问题 都是用到了回溯
```
// 数独工程.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include "pch.h"
#include <iostream>
#include<math.h>
#include<random>
#include<string>
#include<fstream>
#include<time.h>
#include<stdlib.h>

using namespace std;
//ofstream file1("终局.txt");
int a[9][9] = {4,0};//a里存放了每次我们查看终局里每个空的候选值
int zhongju[9][9] = {4,0};
int Line=0;//行
int Row=1;//列
int question[9][9] = { 0 };
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
static int Znum=0;//已经生成的终局
static int flag = 1;
/*void Print(int x[9][9])
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
}*/
void Print2(int x[9][9],ofstream &file4)
{//ofstream file1("终局.txt");
	//ofstream file4("解.txt");
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			file4 << x[i][j] << " ";
		}
		file4 << "\n";
	}
	file4 << "\n";
	//file4.close();
}
void tianshu(int row,int line,int sum,ofstream &file1)//,row line==next
{
	//ofstream file1("终局.txt");
	int templ[9] = {0};//模板，每次清0，查看是否十个数都已经遍历过
	int sym =check(row, line, templ);
		int i,j,i1,i2,j2,j3,j1;
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
				//Print(zhongju);
					//num++;
					if (Znum == sum)
						flag = 0;
					//接下来是进行代码改进
					int hang[9] = { 0,1,2,3,4,5,6,7,8 }, lie[9] = {0,1,2,3,4,5,6,7,8};//这两个数组可以帮助我们制作出更多的矩阵！刚开始都是默认的顺序
					for (i = 1; i <=2; i++)
					{
						if (flag == 0)
							break;						
						for (j = 0; j <= 2; j++)
						{
							if (i != 0 && j == 0)
								continue;
							if (flag == 0)
								break;
							for (int spec = 1; spec <= 2; spec++)
							{
								hang[spec] = spec;
							}
							if (((i + j) % 3) < (i % 3))
							{
								break;
							}
							else
							{
								int h;//容器
								h = hang[i];
								hang[i] = hang[i + j];
								hang[i + j] = h;
								for (i1 = 0; i1 <= 2; i1++)
								{
									if (flag == 0)
										break;									
									for (j1 = 0; j1 <= 2; j1++)
									{
										if (i1 != 0 && j1 == 0)
											continue;
										if (flag == 0)
											break;
										for (int spec = 0; spec <= 2; spec++)
										{
											hang[3+spec] = 3+spec;
										}
										if (((i1 + j1) % 3) < (i1 % 3))
										{
											break;
										}
										else
										{
											h = hang[3+i1];
											hang[3+i1] = hang[3+i1 + j1];
											hang[3+i1 + j1] = h;
											for (i2 = 0; i2 <= 2; i2++)
											{
												if (flag == 0)
													break;												
												for (j3 = 0; j3 <= 2; j3++)
												{
													if (i2 != 0 && j3 == 0)
														continue;
													if (flag == 0)
														break;
													/*for (int spec = 0; spec <= 2; spec++)
													{
														hang[6+spec] = 6+spec;
													}*/
													if (((i2 + j3) % 3) < (i2 % 3))
													{
														break;
													}
													else
													{
												        //行的变换结束了，接下来是列的变换
														int h;//容器
														h = lie[i2];
														lie[i2] = lie[i2 + j3];
														lie[i2 + j3] = h;
														for (i = 1; i <= 2; i++)
														{
															if (flag == 0)
																break;															
															for (j = 0; j <= 2; j++)
															{
																if (i != 0 && j == 0)
																	continue;
																if (flag == 0)
																	break;
																for (int spec = 1; spec <= 2; spec++)
																{
																	lie[spec] = spec;
																}
																if (((i + j) % 3) < (i % 3))
																{
																	break;
																}
																else
																{
																	int h;//容器
																	h = lie[i];
																	lie[i] = lie[i + j];
																    lie[i + j] = h;
																	for ( i1 = 0; i1 <= 2; i1++)
																	{
																		if (flag == 0)
																			break;																		
																		for (j1 = 0; j1 <= 2; j1++)
																		{
																			if (i1 != 0 && j1 == 0)
																				continue;
																			if (flag == 0)
																				break;
																			for (int spec = 0; spec <= 2; spec++)
																			{
																				lie[3 + spec] = 3 + spec;
																			}
																			if (((i1 + j1) % 3) < (i1 % 3))
																			{
																				break;
																			}
																			else
																			{
																				h = lie[3 + i1];
																				lie[3 + i1] = lie[3 + i1 + j1];
																				lie[3 + i1 + j1] = h;
																				for ( i2 = 0; i2 <= 2; i2++)
																				{
																					if (flag == 0)
																						break;
																					for (j3 = 0; j3 <= 2; j3++)
																					{
																						if (i2 != 0 && j3 == 0)
																							continue;

																						if (flag == 0)
																							break;
																						for (int spec = 0; spec <= 2; spec++)
																						{
																							lie[6 + spec] = 6 + spec;
																						}
																						if (((i2 + j3) % 3) <(i2 % 3))
																						{
																							break;
																						}
																						else
																						{
																							h = lie[6+i2];
																							lie[6+i2] = lie[6+i2 + j3];
																							lie[6+i2 + j3] = h;
																							for (int drawline = 0; drawline < 9; drawline++)
																							{
																								for (int drawrow = 0; drawrow < 9; drawrow++)
																								{
																									file1 << zhongju[hang[drawline]][lie[drawrow]]<<" ";
																									
																								}
																								
																								file1 << "\n";
																							}
																							file1 << "\n";
																							Znum++;
																							if (Znum == sum)
																								flag = 0;
																							/*for (int drawline = 0; drawline < 9; drawline++)
																							{
																								hang[drawline] = drawline;
																								lie[drawline] = drawline;
																								
																							}*/
																						}
																					}
																				}
																			}
																		}
																	}
																}
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
					return;
			}
			else
			{
				//row = 0;
				//line++;
				tianshu(0, line+1,sum,file1);
				i = 0;
			}
		}
		else
		{
			//row++;
			tianshu(row+1, line,sum,file1);
			i = 0;
		}
			if (flag == 0)
				break;
		}
}
static int Qnum=0;
int check2(int row, int line, int *templ2)
{
	int blocklinenum, blockrownum;
	blocklinenum = line / 3;//块行数
	blockrownum = row / 3;//块列数
	//int innerlinenum = line % 3;
	//int innerrownum = row % 3;
	int startaddline = blocklinenum * 3;//块的起始行地址
	int startaddrow = blockrownum * 3;//块的起始列地址
	int i = 0; int j = 0;int sum=0;
	sum = startaddline * 9 + startaddrow;
		for (i = 0; i <= 20; i++)
		{
		    int tempsum=sum+i;
			if (question[tempsum / 9][startaddrow+(tempsum % 3)] != 0)
				templ2[question[tempsum / 9][startaddrow+tempsum % 3] - 1] = 1;
		}
		for (i = 0; i < 9; i++)
		{
			if (question[line][i] != 0)
			{
				templ2[question[line][i] - 1] = 1;
			}
			if (question[i][row] != 0)
				templ2[question[i][row] - 1] = 1;
		}
		for (i = 0; i < 9; i++)
		{
			if (templ2[i] == 0)
				j++;
		}
		return j;//j代表了我们会有多少的候选值
}

void jieti(int row,int line,ofstream &file4)//再调用此函数之前必须先找到题目矩阵中，第一个空，并用这个点的参数调用这个函数和
{//默认输入的所有的题目都是有解的；
	int numth = line * 9 + row;//我们的起始是第几个空
	int biaozhi = numth;
	int flag = 0;
	int templ2[9] = {0};
	int sys=check2(row, line, templ2);
	if (sys == 0)
		return;
	while (sys--)
	{
		for (int i = 0; i < 9; i++)
		{
			if (templ2[i] == 0)
			{
				templ2[i] = 1;
				question[line][row] = i + 1;
				break;
			}
		}
for (int i = 0; i < 81-biaozhi; i++)
		//虽然我们在解决问题的时候，我们把这个数组看作是一维的，但是我们的数据还是二维数据。二位数据的检查函数相对来说简单一些
	{
		numth =biaozhi+ i;
		int transline = numth / 9;
		int transrow = numth % 9;
		if (question[transline][transrow] == 0)
		{
			jieti(transrow, transline,file4);
			flag = 1;
			break;
		}
	}
	if (Qnum != 0)
	{
		return;
	}
	if (flag == 0)
	{
		Print2(question,file4);
		Qnum++;
		return;
	}
	}
	question[line][row] = 0;

}

int main(int argc, char * argv[])
{
	
string a, b;//a存放第一个参数，b存放第二个参数
	a = argv[1];
	b = argv[2];
	
	int num = 0;
	if (argc != 3)
	{
		ofstream file1("终局.txt");
file1 << "输入正确数量参数！" << endl;
file1.close();
	}
		
	else
	{
		if (a[1] == 'c')//如果输入的指令是-c
		{
			int flag = 0;//flag用来标志输入是否合法
			for (int i = 0; i < b.length(); i++)
			{
				if (b[i] - '0' < 0 || b[i] - '9'>0 || i > 6)
				{
					flag = 1;//除了我们要生成格局数的大小我们没有确定之外，其他非法情况都已经剔除
				}

			}
			if (flag == 0)
			{
				int j = b.length() - 1;

				for (int i = 0; i < b.length(); i++)
				{
					num += (b[i] - '0') * pow(10, j);//num 就是我们要生成的格局数
					j--;

				}
				if (num > 1000000)
				{
					flag = 1;
				}
			}
			if (flag == 1)
				cout << "输入参数错误！" << endl;
			else//如果我们输入的参数是正确的，那么我们就可以生成格局了，我的学号尾号计算得4
			{ofstream file1("终局.txt");
				//ofstream file1("终局.txt");
				file1 << num<< "\n";
				
				tianshu(1, 0, num,file1);
				file1.close();
			}
		}
		if (a[1] == 's')
		{ifstream file2(b);ofstream file4("解.txt");
		//ofstream file4("解.txt");
			while (!file2.eof())
			{
				for (int i = 0; i < 81; i++)
				{
					file2 >> question[i / 9][i % 9];
						
				}
				int flag1 = 0;
				int i, j;
				for (i = 0; i < 9; i++)
				{
					for (j = 0; j < 9; j++)
					{
						if (question[i][j] == 0)
						{
							flag1 = 1;
							break;
						}

					}
					if (flag1 == 1)
						break;
				}
				Qnum = 0;
				jieti(j, i,file4);
				
				
			}

file2.close();
file4.close();
		}
	}	
/*	ifstream file2("C:\\Users\\59111\\source\\repos\\数独工程\\Debug\\问题.txt"); ofstream file4("解.txt");
	//ofstream file4("解.txt");
	while (!file2.eof())
	{
		for (int i = 0; i < 81; i++)
		{
			file2 >> question[i / 9][i % 9];

		}
		int flag1 = 0;
		int i, j;
		for (i = 0; i < 9; i++)
		{
			for (j = 0; j < 9; j++)
			{
				if (question[i][j] == 0)
				{
					flag1 = 1;
					break;
				}

			}
			if (flag1 == 1)
				break;
		}
		Qnum = 0;
		jieti(j, i, file4);
		file4 << "**";

	}

	file2.close();
	file4.close();*/
/*ofstream file1("终局.txt");
int num;
cin >> num;
//ofstream file1("终局.txt");
file1 << num << "\n";

tianshu(1, 0, num, file1);
file1.close();*/
}
```
