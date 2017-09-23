# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:16:43 2017

@author: Vlad
"""
import laba1var1 as ciph
import tkinter
from tkinter.filedialog import *

maincolor = 'gray'

class window:
    def __init__(self):
        Label(root,text = 'Путь к файлу:',bg=maincolor,fg = 'white').pack(fill = X)
        self.path = tkinter.Entry(root,width=100,bd=3)
        self.path.pack(fill = X)
        #self.path.insert(END,askopenfilename())
        
         #кнопка
        self.pathbtn = tkinter.Button(root,text = "Выбрать путь к файлу",width = 85,height = 2,bg = '#D3D3D3')
        self.pathbtn.bind('<Button-1>',self.opendialog)
        self.pathbtn.pack(fill = X)
        
        
        Label(root,text = 'Ввод ключа \n  Введите строку для Виженера и Столбцового метода \n Для Изгороди - число (высоту изгороди), для Касиски - число (l в l-грамме)',bg=maincolor,fg = 'white').pack()
        #линия для ввода текста
        self.key = tkinter.Entry(root,width=100,bd=3)
        self.key.pack(fill = X)
        
        
        #радиокнопки
        self.var = IntVar()
        self.var.set(1)
        Label(root,text = 'Выберите метод:',bg=maincolor,fg = 'white').pack(fill = X)
        Radiobutton(root, text="Изгородь", variable = self.var, value = 1,bg = maincolor,fg = 'white', selectcolor = 'black',activebackground= maincolor).pack(anchor=W,fill = X)
        Radiobutton(root, text="Столбцовый", variable = self.var, value = 2,bg = maincolor,fg = 'white', selectcolor = 'black',activebackground= maincolor).pack(anchor=W,fill = X)
        Radiobutton(root, text="Виженер", variable = self.var, value = 3,bg = maincolor,fg = 'white', selectcolor = 'black',activebackground= maincolor).pack(anchor=W,fill = X)
        
        Label(root,text = 'Выберите что вы хотите сделать с файлом:',bg=maincolor,fg = 'white').pack()
        self.var_1 = IntVar()
        self.var_1.set(1)
        Radiobutton(root, text="Зашифровать", variable = self.var_1, value = 1,bg = maincolor,fg = 'white', selectcolor = 'black',activebackground= maincolor).pack(anchor=W,fill = X)
        Radiobutton(root, text="Расшифровать", variable = self.var_1, value = 2,bg = maincolor,fg = 'white', selectcolor = 'black',activebackground= maincolor).pack(anchor=W,fill = X)
        
        
        #кнопка
        self.btn = tkinter.Button(root,text = "Старт",width = 85,height = 2,bg = '#D3D3D3')
        self.btn.bind('<Button-1>',self.press_run_button)
        self.btn.pack(fill = BOTH,expand = True)
        
        #кнопка
        self.btn = tkinter.Button(root,text = "Метод Касиски",width = 85,height = 2,bg = '#D3D3D3')
        self.btn.bind('<Button-1>',self.press_kassiski_button)
        self.btn.pack(fill = BOTH,expand = True)
        
        
        
        
        
    def printer(self,event):
        print(self.var.get(),self.var_2.get(),self.ent.get())
        
    def opendialog(self,event):
        self.path.delete(0, END)
        self.path.insert(END,askopenfilename())
        
    def press_run_button(self,event):
        
        if self.path.get() == '':
            self.path.delete(0, END)
            self.path.insert(END,"Вы не выбрали файл")
        elif self.key.get() == '':
            self.key.insert(END,"Введите сюда ключ")
        else:
            if self.var.get() == 1 and self.var_1.get() == 1:
                ciph.rail_encipher(self.path.get(),self.key.get())
            elif self.var.get() == 1 and self.var_1.get() == 2:
                ciph.rail_decipher(self.path.get(),self.key.get())
            elif self.var.get() == 2 and self.var_1.get() == 1:
                ciph.column_encipher(self.path.get(),self.key.get())
            elif self.var.get() == 2 and self.var_1.get() == 2:
                ciph.column_decipher(self.path.get(),self.key.get())
            elif self.var.get() == 3 and self.var_1.get() == 1:
                ciph.vignere_encipher(self.path.get(),self.key.get())
            elif self.var.get() == 3 and self.var_1.get() == 2:
                ciph.vignere_decipher(self.path.get(),self.key.get())
    
    def press_kassiski_button(self,event):
        if self.path.get() == '':
            self.path.delete(0, END)
            self.path.insert(END,"Вы не выбрали файл")
        elif self.key.get() == '0' or self.key.get() == '1' or self.key.get() == '2':
            self.key.delete(0, END)
            self.key.insert(END,"Слишком малая длина l-граммы, введите больше 2")
        elif not self.key.get().isdigit():
            self.key.delete(0, END)
            self.key.insert(END,"Вы ввели не число")
        elif int(self.key.get()) > 10:
            self.key.delete(0, END)
            self.key.insert(END,"Слишком большое, не даст результата, введите до 10")
        else:
            ciph.final_kassiski(self.path.get(),self.key.get())
        

    



root = tkinter.Tk()
root['bg'] = maincolor
obj = window()
root.mainloop()
    
    

