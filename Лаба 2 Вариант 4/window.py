# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:46:01 2017

@author: Vlad
"""

import procedures as pr
import tkinter 

from tkinter.filedialog import *

maincolor = 'gray'

class Window:
    def __init__(self):
        Label(root,text = '',bg=maincolor,fg = 'white',height = 1).pack()
        Label(root,text = 'Путь к файлу:',bg=maincolor,fg = 'white').pack(fill = X)
        self.path = tkinter.Entry(root,width=70,bd=3)
        self.path.bind('<KeyPress>',self.noKeyPress)
        self.path.pack()
        #self.path.insert(END,askopenfilename())
        
         #кнопка
        Label(root,text = '',bg=maincolor,fg = 'white',height = 1).pack()
        self.pathbtn = tkinter.Button(root,text = "Выбрать путь к файлу",width = 60,height = 2,bg = '#D3D3D3')
        self.pathbtn.bind('<Button-1>',self.opendialog)
        self.pathbtn.pack()
        
        #радиокнопки
        self.var = IntVar()
        self.var.set(1)
        
        
        Label(root,text = '',bg=maincolor,fg = 'white',height = 1).pack()
        Label(root,text = 'Выберите метод:',bg=maincolor,fg = 'white').pack(fill = X)
        Radiobutton(root, text="LFSR", variable = self.var, value = 1,bg = maincolor,fg = 'white', selectcolor = 'black',activebackground= maincolor).pack(anchor=W,fill = X)
        
        Label(root,text = 'Ввод ключа (сюда вводить ключ для LFSR )',bg=maincolor,fg = 'white').pack()
        #линия для ввода текста
        self.key0 = tkinter.Entry(root,width=70,bd=3)
        self.key0.bind('<KeyPress>',self.keyPress)
        self.key0.pack()
        
        Label(root,text = '',bg=maincolor,fg = 'white',height = 1).pack()
        
        #поле для текста
        self.frame0=tkinter.Frame(root,bg = maincolor,bd=5,width = 100)
        self.frame0.pack()
        

        Label(self.frame0,text = 'Ключ 1',bg=maincolor,fg = 'white',width = 15).pack(side="left")
        Label(self.frame0,text = 'Ключ 2',bg=maincolor,fg = 'white',width =16).pack(side="left")
        Label(self.frame0,text = 'Ключ 3',bg=maincolor,fg = 'white',width = 15).pack(side="left")
        Label(self.frame0,text = 'Ключ Геффе',bg=maincolor,fg = 'white',width = 15).pack(side="left")
        
        
        
        
        self.frame1=tkinter.Frame(root,bg = maincolor,bd=5,width = 100)
        self.frame1.pack()
        
        self.txt = tkinter.Text(self.frame1,height = 10,width = 8, bd = 3 )
        self.txt1 = tkinter.Text(self.frame1,height = 10,width = 8, bd = 3 )
        self.txt2 = tkinter.Text(self.frame1,height = 10,width = 8, bd = 3 )
        self.txt3 = tkinter.Text(self.frame1,height = 10,width = 8, bd = 3 )
        
        self.txt.bind('<KeyPress>',self.noKeyPress)
        self.txt1.bind('<KeyPress>',self.noKeyPress)
        self.txt2.bind('<KeyPress>',self.noKeyPress)
        self.txt3.bind('<KeyPress>',self.noKeyPress)
        
        self.txt.pack(side = "left")
        Label(self.frame1,text = '',bg=maincolor,width = 5).pack(side="left")
        self.txt1.pack(side="left")
        Label(self.frame1,text = '',bg=maincolor,width = 5).pack(side="left")
        self.txt2.pack(side="left")
        Label(self.frame1,text = '',bg=maincolor,width = 5).pack(side="left")
        self.txt3.pack(side="left")
        
        
        ##########################################33
        Label(root,text = '',bg=maincolor,fg = 'white',height = 1).pack()
        Radiobutton(root, text="Геффе", variable = self.var, value = 2,bg = maincolor,fg = 'white', selectcolor = 'black',activebackground= maincolor).pack(anchor=W,fill = X)
        
        
        Label(root,text = 'Регистр 1 (для Геффе)',bg=maincolor,fg = 'white').pack()
        self.key1 = tkinter.Entry(root,width=70,bd=3)
        self.key1.bind('<KeyPress>',self.keyPress1)
        self.key1.pack()
        Label(root,text = 'Регистр 2 (для Геффе)',bg=maincolor,fg = 'white').pack()
        self.key2 = tkinter.Entry(root,width=70,bd=3)
        self.key2.bind('<KeyPress>',self.keyPress2)
        self.key2.pack()
        Label(root,text = 'Регистр 3 (для Геффе)',bg=maincolor,fg = 'white').pack()
        self.key3 = tkinter.Entry(root,width=70,bd=3)
        self.key3.bind('<KeyPress>',self.keyPress3)
        self.key3.pack()
        
        
        
        Label(root,text = '',bg=maincolor,fg = 'white',height = 2).pack()
        
        Radiobutton(root, text="RS4", variable = self.var, value = 3,bg = maincolor,fg = 'white', selectcolor = 'black',activebackground= maincolor).pack(anchor=W,fill = X)
        
        Label(root,text = 'Ввод ключа (сюда вводить ключ для LFSR )',bg=maincolor,fg = 'white').pack()
        self.key4 = tkinter.Entry(root,width=70,bd=3)
        self.key4.pack()
        
        
        Label(root,text = '',bg=maincolor,fg = 'white',height = 2,width = 70).pack()
        #кнопка
        self.btn = tkinter.Button(root,text = "Старт",width = 60,height = 2,bg = '#D3D3D3')
        self.btn.bind('<Button-1>',self.press_run_button)
        self.btn.pack(expand = True)
        
        Label(root,text = '',bg=maincolor,fg = 'white',height = 2).pack()
        
        
        
    
    def keyPress(self,event):
        if len(self.key0.get()) >= 26:
            if event.char not in ('\10'):
                return 'break'
        if event.char not in ('1', '0','\10'):
            return 'break'
        
    def keyPress1(self,event):
        if len(self.key1.get()) >= 26:
            if event.char not in ('\10'):
                return 'break'
        if event.char not in ('1', '0','\10'):
            return 'break'
        
    def keyPress2(self,event):
        if len(self.key2.get()) >= 34:
            if event.char not in ('\10'):
                return 'break'
        if event.char not in ('1', '0','\10'):
            return 'break'
        
    def keyPress3(self,event):
        if len(self.key3.get()) >= 24:
            if event.char not in ('\10'):
                return 'break'
        if event.char not in ('1', '0','\10'):
            return 'break'
                
    
        
    def noKeyPress(self,event):
        if event.char not in ():
            return 'break'
        
    def opendialog(self,event):
        self.path.delete(0, END)
        self.path.insert(END,askopenfilename())
        
    def press_run_button(self,event):
        
        if self.path.get() == '':
            self.path.delete(0, END)
            self.path.insert(END,"Вы не выбрали файл")
        else:
            if self.var.get() == 1:
                key = pr.lfsr_for_file(self.path.get(),self.key0.get())
                self.txt.delete(1.0, END)
                self.txt.insert(END,key[:600])
                
                self.txt1.delete(1.0, END)
                self.txt2.delete(1.0, END)
                self.txt3.delete(1.0, END)
                pass
            elif self.var.get() == 2:
                tupl = pr.geffe_for_file(self.path.get(),self.key1.get(),self.key2.get(),self.key3.get())
                geffe_key = tupl[1]
                key1 = tupl[2]
                key2 = tupl[3]
                key3 = tupl[4]
                
                self.txt.delete(1.0, END)
                self.txt.insert(END,key1[:600])
                
                self.txt1.delete(1.0, END)
                self.txt1.insert(END,key2[:600])
                
                self.txt2.delete(1.0, END)
                self.txt2.insert(END,key3[:600])
                
                self.txt3.delete(1.0, END)
                self.txt3.insert(END,geffe_key[:600])
                pass
            elif self.var.get() == 3:
                
                tupl = pr.rc4_for_file(self.path.get(),self.key4.get())
                key4 = tupl[1]
                self.txt.delete(1.0, END)
                self.txt.insert(END,key4[:600])
                self.txt1.delete(1.0, END)
                self.txt2.delete(1.0, END)
                self.txt3.delete(1.0, END)
                pass
    
    
    



root = tkinter.Tk()
root['bg'] = maincolor
obj = Window()
root.mainloop()
    
    

