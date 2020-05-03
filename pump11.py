#!/usr/bin/env python
# coding: utf-8

# In[51]:




import tkinter as tk
from tkinter import *
from tkinter import StringVar

window=tk.Tk()
window.title('PPC V1.1 By Jeason Shen')
window.geometry('400x550')
window.configure(bg='white') 

valueh=StringVar()
valuee=StringVar()
valuep=StringVar()
valuens=StringVar()



tk.l=Label(window,text='泵性能计算器',font='等线',foreground = 'green',bg='white').place(x=130,y=10)

def clickbtnH():
    global z
    global c
    
    
    a=float(e_pin.get())
    b=float(e_pout.get())
    c=float(e_density.get())
    d=float(e_vin.get())
    e=float(e_vout.get())
    z=float((b-a)/c/9.8+(e*e-d*d)/2/9.8)
    valueh.set(z)

def clickbtnE():
    global bb
    global cc
    aa=float(e_density.get())
    bb=float(e_flowrate.get())
    cc=float(e_rotatespeed.get())
    dd=float(e_torque.get())
    zz=float(aa*9.8*bb*z*30/cc/3.14/dd)
    zzz=float(zz*100)
    valuee.set(zzz)

def clickbtnP():
    
    pp=float(c*9.8*bb*z)
    ppp=float(pp/1000)
    valuep.set(ppp)

  
def clickbtnca():
    clickbtnP(),clickbtnE(),clickbtnH()

    

l_pin=tk.Label(window,text='P1(Pa)',font='Times',bg='white').place(x=10,y=60)
#需将所有entry的位置定义另取一行，否则会出现get()函数无法调取的现象
e_pin=tk.Entry(window,bd=3,width=8)
e_pin.place(x=100,y=60)

l_vin=tk.Label(window,text='V1(m/s)',font='Times',bg='white').place(x=200,y=60)
e_vin=tk.Entry(window,bd=3,width=8)
e_vin.place(x=280,y=60)

l_pout=tk.Label(window,text='P2(Pa)',font='Times',bg='white').place(x=10,y=120)
e_pout=tk.Entry(window,bd=3,width=8)
e_pout.place(x=100,y=120)

l_vout=tk.Label(window,text='V2(m/s)',font='Times',bg='white').place(x=200,y=120)
e_vout=tk.Entry(window,bd=3,width=8)
e_vout.place(x=280,y=120)

l_density=tk.Label(window,text='ρ(kg/m3)',font='Times',bg='white').place(x=10,y=180)
e_density=tk.Entry(window,bd=3,width=8)
e_density.place(x=100,y=180)

l_flowrate=tk.Label(window,text='Q(m3/s)',font='Times',bg='white').place(x=200,y=180)
e_flowrate=tk.Entry(window,bd=3,width=8)
e_flowrate.place(x=280,y=180)

l_rotatespeed=tk.Label(window,text='n(rpm)',font='Times',bg='white').place(x=10,y=240)
e_rotatespeed=tk.Entry(window,bd=3,width=8)
e_rotatespeed.place(x=100,y=240)

l_torque=tk.Label(window,text='T(N▪m)',font='Times',bg='white').place(x=200,y=240)
e_torque=tk.Entry(window,bd=3,width=8)
e_torque.place(x=280,y=240)



#运算区=======================================================================================
lh=tk.Label(window,text='H(m)',font='Times',bg='white',width=5)
lh.place(x=10,y=380)
e_head=tk.Entry(window,bd=3,width=8,textvariable=valueh)
e_head.place(x=90,y=380)

lp=tk.Label(window,text='P(kw)',font='Times',bg='white',width=5)
lp.place(x=10,y=440)
e_power=tk.Entry(window,bd=3,width=8,textvariable=valuep)
e_power.place(x=90,y=440)





le=tk.Label(window,text='η(%)',bg='white',width=5)
le.place(x=220,y=380)
e_efficiency=tk.Entry(window,bd=3,width=8,textvariable=valuee)
e_efficiency.place(x=280,y=380)


btnca=tk.Button(window,text='Calculate',font='Times',foreground = 'white',bg='green',width=10,command=lambda:clickbtnca())
btnca.place(x=130,y=300)








window.mainloop()


# In[ ]:





# In[ ]:




