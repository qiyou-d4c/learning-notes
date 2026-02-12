import turtle as t
import random
import math
from collections import defaultdict
t.pensize(5)
t.pencolor("green")
t.shape("turtle")
z=int(input("请输入行数"))
pos_num_dict={}
num_list=[]
pos_list=[]
c=z * z + 1
pos_num_dict=defaultdict(int)
for b in range(1,c):
    num_list.append(b)
t.tracer(False)#迅速出图
def tap(x,y):
    x=math.floor(x / 100) * 100
    y=math.floor(y / 100) * 100
    if  pos_num_dict[(x, y+100)] == c - 1:
        d=pos_num_dict[(x, y)]
        e=y+100
        del pos_num_dict[(x, e)]
        del pos_num_dict[(x, y)]
        pos_num_dict[(x, y+100)]=d
        pos_num_dict[(x, y)]=c-1
    elif pos_num_dict[(x, y-100)] == c - 1:
        d=pos_num_dict[(x, y)]
        e=y-100
        del pos_num_dict[(x, e)]
        del pos_num_dict[(x, y)]
        pos_num_dict[(x, y-100)]=d
        pos_num_dict[(x, y)]=c-1
    elif pos_num_dict[(x+100, y)] == c - 1:
        d=pos_num_dict[(x, y)]
        e=x+100
        del pos_num_dict[(e, y)]
        del pos_num_dict[(x, y)]
        pos_num_dict[(x+100, y)]=d
        pos_num_dict[(x, y)]=c-1
    elif pos_num_dict[(x-100, y)] == c - 1:
        d=pos_num_dict[(x, y)]
        e=x-100
        del pos_num_dict[(e, y)]
        del pos_num_dict[(x, y)]
        pos_num_dict[(x-100, y)]=d
        pos_num_dict[(x, y)]=c - 1
    else :
        print("cuowu")
    t.clear()
    for k in range(z):
        for i in range(z):
            t.up()
            t.goto(-200 + i * 100,200 - k * 100)
            a=pos_num_dict[(-200 + i * 100,200 - k * 100)]
            if a < c - 1:
                if a >= 10:
                    t.write(a,move=False,align='left',font=('arial',56,'normal'))
                else:
                    t.forward(30)
                    t.write(a,move=False,align='left',font=('arial',56,'normal'))
                    t.forward(-30)
                t.down()
                drawsquare()
            else:
                t.down()
                drawsquare()
    t.update()
    check(z,pos_num_dict)
def check(z: int,pos: dict):
    n=1
    for l in range(z):
        for m in range(z):
            if pos[(-200 + m * 100,200 - l * 100)]==n:
                n=n+1
                continue
            else:
                break
    if n == c:
        t.up()
        t.goto(-200,0)
        t.write("你赢了",move=False,align='left',font=('arial',108,'normal'))
        t.down
def drawsquare():
    #画正方形
    for j in range(4):
            t.forward(100)
            t.left(90)
def start(z: int):
    for k in range(z):
        for i in range(z):
            t.up()
            t.goto(-200 + i * 100,200 - k * 100)
            pos_list.append((-200 + i * 100,200 - k * 100))#历史遗留问题，没起任何作用
            random.shuffle(num_list)
            a=num_list[0]
            pos_num_dict[(-200 + i * 100,200 - k * 100)]=a
            if a < c - 1:
                if a >= 10:
                    t.write(a,move=False,align='left',font=('arial',56,'normal'))
                else:
                    t.forward(30)
                    t.write(a,move=False,align='left',font=('arial',56,'normal'))
                    t.forward(-30)
                t.down()
                drawsquare()
                del num_list[0]
            else:
                t.down()
                drawsquare()
                del num_list[0]
start(z)
t.onscreenclick(tap)
t.update()#刷新
t.done()
