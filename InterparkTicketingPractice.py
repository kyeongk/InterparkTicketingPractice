import tkinter as tr
import tkinter.messagebox as wmsg
import time
import random
from tkinter import font

c=0
d=0
e=0
a=0
es=0
start=0
end=0
jeongdab=0
odab=0
nam=10
x=1

q='AAAAAA'

def randomtext():

    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M',
              'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    text1=random.choice(alphabet)
    text2=random.choice(alphabet)
    text3=random.choice(alphabet)
    text4=random.choice(alphabet)
    text5=random.choice(alphabet)
    text6=random.choice(alphabet)

    global q

    q=text1+text2+text3+text4+text5+text6
    label2.configure(text=q)

    return q


    #label2.configure(text=n)

def munjae(event):
    global c,d,e,a,es,start,end,jeongdab,odab,nam,x,q
    label1.config(text="STAGE %s"%x)
    #q=randomtext()
    #a=label2.cget("text")
    d=input1.get()
    e=d.upper()
    

    #label2.configure(text=q)
    end=time.time()

    if e==q:
        #end=time.time()
        
        es=(end-start)
        es=format(es,".2f")
        label4.config(text="타자시간: %s초"%es)
        text.insert(tr.END,"정답\n")
        
        jeongdab=jeongdab+1
        nam=nam-1
        label3.config(text="정답:%s, 오답:%s, 남은개수:%s"%(jeongdab,odab,nam))
        c=c+1
        q=randomtext()
        label2.config(text=q)
        #start=time.time()
        input1.delete(0,10)


    else:
        es=end-start
        es=format(es,".2f")
        label4.config(text="타자시간: %s초"%es)
        text.insert(tr.END,"오답\n")
        odab=odab+1
        nam=nam-1
        label3.config(text="정답:%s, 오답:%s, 남은개수:%s"%(jeongdab,odab,nam))
        c=c+1
        q=randomtext()
        label2.config(text=q)
        input1.delete(0,10)

    start=time.time()


    if c==10:
        msgbox=wmsg.askquestion("팝업","모두 완료하였습니다.\n계속하시겠습니까?")
        #label4.config(text="타자시간:%s초"%round(es))
        #jeongdab=0
        #odab=0
        nam=10
        c=0
        es=0
        start=0
        end=0
        if msgbox!='yes':
            root.destroy()
        else:
            x+=1
            label1.config(text="STAGE %s"%x)
            input1.delete(0,10)
            text.delete(1.0,tr.END)
            label2.config(text=q)







root=tr.Tk()
root.title("인터파크 보안문자 입력 연습")
root.geometry('600x400')

font=font.Font(size=20, weight='bold')

label1=tr.Label() #레벨
label1.place(x=5,y=60)
label2=tr.Label(font=font) #문제나오는창
label2.place(x=80,y=20)
label3=tr.Label() #정답,오답,남은갯수 나오는 창
label3.place(x=5,y=80)
label4=tr.Label() #타자시간
label4.place(x=5,y=100)

input1=tr.Entry(width="20")
input1.place(x=60,y=60)
input1.bind("<Return>",munjae)

text=tr.Text()
text.place(x=300,y=0,width='300')

button1=tr.Button(text='START',command=randomtext)
button1.place(x=220, y=60)

#label2.config(text=q)

root.mainloop()
