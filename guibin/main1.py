# -*- coding: utf-8 -*-
from _ctypes import byref
from tkinter import *
from ctypes import *
import random
rhole=random.randint(30,60)#随机挖洞数
def fun2():
    lib.tianshu();
    aa = []
    cc = []
    with open('D:\\火线时刻\\数独游戏\\1.txt', 'r')as f:
        for line in f:
            for dd in line:
                aa.append(dd)  # 问题矩阵
                cc.append(dd)  # 解题矩阵
    # def fun1():
    for i in range(9):
        fhole1 = random.randint(0, 8);
        # blocklinenum = line / 3; # 块行数
        # blockrownum = row / 3; #块列数
        # startaddline = blocklinenum * 3; #块的起始行地址
        # startaddrow = blockrownum * 3; #块的起始列地址
        aa[int(i / 3) * 27 + int(fhole1 / 3) * 9 + fhole1 % 3] = 0
        while 1:
            fhole2 = random.randint(0,8)
            if fhole1 == fhole2:
                continue
            else:
                aa[int(i / 3) * 27 + int(fhole2 / 3) * 9 + fhole2 % 3] = 0
                break;

    for i in range(rhole - 18):
        while (1):
            dele = random.randint(0, 80);
            if aa[dele] == 0:
                continue;
            else:
                break
        aa[dele] = 0
    print(aa)
    print(cc)
    root = Tk()
    root.geometry('80x80+10+10')
    zeronum = 4
    j = 0
    v = []
    B = []
    C = []
    for i in range(rhole):
        B.append(0)
    for i in range(81):
        if aa[i] == 0:
            B = Entry(root, width=3)
            B.grid(row=int(i / 9), column=int(i % 9))
            j = j + 1
            continue;
        else:
            l1 = Label(root, text=str(aa[i]), width=3, height=3)
            l1.grid(row=int(i / 9), column=int(i % 9))
            BU = Button(root, text='下一题', command=fun2)
            BU.grid(row=13, column=13)
            BU2 = Button(root, text='做完了！', command=fun3)
            BU2.grid(row=16, column=13)
######################################
zhongju= c_int(81)
lib = windll.LoadLibrary("D:\火线时刻\数独游戏\数独工程链接库.dll")
flag=1
lib.tianshu();
#lib.func(
aa=[]
cc=[]
with open ('D:\\火线时刻\\数独游戏\\1.txt','r')as f:
    for line in f:
        for dd in line:
            aa.append(dd)#问题矩阵
            cc.append(dd)#解题矩阵
#def fun1():
for i in range(9):
        fhole1=random.randint(0,8);
    #blocklinenum = line / 3; # 块行数
    #blockrownum = row / 3; #块列数
    #startaddline = blocklinenum * 3; #块的起始行地址
    #startaddrow = blockrownum * 3; #块的起始列地址
        aa[int(i/3)*27+int(fhole1/3)*9+fhole1%3]=0
        while 1:
            fhole2=random.randint(0,8)
            if fhole1==fhole2:
                continue
            else:
                aa[int(i / 3) * 27 + int(fhole2 / 3) * 9 + fhole2 % 3] = 0
                break;

for i in range(rhole-18):
    while(1):
        dele=random.randint(0, 80);
        if aa[dele]==0:
            continue;
        else:
            break
    aa[dele]=0
print(aa)
print(cc)
root = Tk()
root.geometry('80x80+10+10')
j=0
v=[]
B=[]
C=[]
for i in range(rhole):
    B.append(0)
for i in range(81):
    if aa[i]==0:
        B[j]=Entry(root,width=3)
        B[j].grid(row=int(i/9), column=int(i%9))
        j=j+1
        continue;
    else:
        l1 = Label(root, text=str(aa[i]),width =3,height=3)
        l1.grid(row=int(i/9), column=int(i%9))
BU=Button(root,text='下一题',command=fun2)
BU.grid(row=13,column=13)
j=0
def fun3():
    j=0;
    flag=0
    for i in range(81):
        if aa[i]==0:
            xy=B[j].get()
            if(xy==''):
                root = Tk()
                root.geometry('80x80+10+10')
                root.title("你没做完！")
                flag=1
                break
            print(int(xy))
            if(int(xy)==int(cc[i])):
                j=j+1
                continue;
            else:
                root = Tk()
                root.geometry('80x80+10+10')
                root.title("你做错了！")
                flag=1
                break
    if flag==0:
        root = Tk()
        root.geometry('80x80+10+10')
        root.title("你做对了！")
BU2=Button(root,text='做完了！',command=fun3)
BU2.grid(row=16,column=13)
print(B[0].get)
print(B[1].get)
root.mainloop()
