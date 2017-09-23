# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 22:36:44 2017

@author: Vlad
"""


def encrypt_rails(plaintext,height):
    """принимает строку которая состоящую только из символов языка, возвращает зашифрованную строку"""
    buff = dict.fromkeys(range(height),'')
    temp = 1
    index = 0
    
    #добавляем в словарь по индексу, меняем направление когда на краях изгороди
    for i in plaintext:
        #print(index,temp,i)
        buff[index] += i
        index += temp
        if index in [0,height-1]:
            temp *= -1
    
    
    #создание зашифрованной строки
    cyphertext = ''
    for key in buff.keys():
        cyphertext += buff[key]
        
    return cyphertext

def decrypt_rails(ciphertext,height):
    """принимает зашифрованнуб строку и высоту изгороди, возвращает расшифрованную строку текста"""
    buff = dict.fromkeys(range(height),'')
    temp = 1
    index = 0
    
    # создаем строку длины ciphertext но с * вместо знака, а потом таким же алгоритмом, как в шифровании, делаем словарь со строками
    bufftext = '*' * len(ciphertext)
    for i in bufftext:
        #print(index,temp,i)
        buff[index] += i
        index += temp
        
        if index in [0,height-1]:
            temp *= -1
            
    #создание словаря с запполненными данными из зашифрованной строки
    index = 0
    for key in buff.keys():
        buffstr = ''
        for i in range(len(buff[key])):
            buffstr += ciphertext[index]
            index +=  1
        buff[key] = buffstr
    """
    #заполнение словаря ненужным символом * для удоства расшифровки
    max_len = 0
    for key in buff.keys():
        if len(buff[key]) > max_len:
            max_len = len(buff[key])
    for key in buff.keys():
        while len(buff[key]) != max_len:
            buff[key] += "*"
    """
    
    #проход по словарю, точно так же как заполнялся он, только в этот раз в обратном порядке
    plaintext = ''
    index = 0
    temp = 1
    for i in range(len(ciphertext)):
        #print(index,temp,i)
        plaintext += buff[index][0]
        buff[index] = buff[index][1:]
        index += temp
        if index in [0,height-1]:
            temp *= -1
   
    return plaintext


def encrypt_column(plaintext,key):
    '''
    buff = dict.fromkeys(key,'')
    
    for i in range(len(plaintext)):
        buff[key[i % len(key)]] += plaintext[i]
    
    buff = sorted(buff.items(), key=lambda item: item[0])  
    '''
    alpha = [chr(i) for i in range(65,91)]
    
    #заполнение словаря
    buff = list(key)
    for i in range(len(plaintext)):
        buff[i%len(key)] += plaintext[i]
    
    
    #присваивание каждой букве числа в зависимости от алфавита и их 
    index = 0
    
    for letter in alpha:
        for i in range(len(buff)):
            if (not buff[i][0].isnumeric()) and buff[i][0].upper()==letter:
                buff[i] = str(index) +'*' + buff[i][1:].upper()
                index += 1
                
            
    #разделение строк в списке на список числа и строки
    for i in range(len(buff)):
        buff[i] = buff[i].split('*')
        buff[i][0] = int(buff[i][0])
    
    buff = sorted(buff, key = lambda x: x[0])
    
    #возвращение строчки
    ciphertext = ''
    for i in range(len(buff)):
        ciphertext += buff[i][1]
    return ciphertext


def decrypt_column(ciphertext, key):
    alpha = [chr(i) for i in range(65,91)]
    
    #заполнение словаря
    buff = list(key)
    for i in range(len(ciphertext)):
        buff[i%len(key)] += '+'
    
    #присваивание каждой букве числа в зависимости от алфавита и их 
    index = 1
    for letter in alpha:
        for i in range(len(buff)):
            if (not buff[i][0].isnumeric()) and buff[i][0].upper()==letter:
                buff[i] = str(index) +'*' + buff[i][1:].upper()
                index += 1
    
    #разделение строк в списке на список числа и строки
    for i in range(len(buff)):
        buff[i] = buff[i].split('*')
        buff[i][0] = int(buff[i][0])
        
    buff = sorted(buff, key = lambda x: x[0])
    
    #заполнение списка из строки шифротекста
    index = 0
    
    for i in range(len(buff)):
        buffstr = ''
        for j in range(len(buff[i][1])):
            buffstr += ciphertext[index]
            index += 1
        buff[i][1] = buffstr
        
    #создание списка с первым элементом буквой а вторым с цифрой
    index = 1
    buffdict = dict.fromkeys(range(1,len(key)+1),'')
    for letter in alpha:
        for i in range(len(key)):
            if key[i].upper() == letter and buffdict[index] =='':
                buffdict[index] = letter
                index += 1
    
    #print(buffdict)       
    final = []
    for letter in key:
        for i in range(1,len(buffdict)+1):
            if letter.upper() == buffdict[i]:
                buffdict[i] = ''
                final.append([letter,i])
                break
    #print(final)
    
    finallist = []
    for i in range(len(final)):
        finallist.append(buff[final[i][1]-1][1])
        
    plaintext = ''
    index = 0
    #print(finallist)
    for i in range(len(ciphertext)):
        plaintext += finallist[i%len(key)][:1]
        finallist[i%len(key)] = finallist[i%len(key)][1:]
        
            
        
    
    return plaintext


def encrypt_vignere(plaintext,key):
    '''принимает строку  и ключ, шифрует по шифру вижнере, приводит все к капслоку'''
    def symbol_shift_r(ch,ch2):
        """берет символ из plaintext и из ключа и делает сдвиг как в шифре цезаря"""
        step = ord(ch2) % 1039
        if ord(ch)+ step > 1072:
            buff = chr(ord(ch)+step - 32)
        else:
            buff = chr(ord(ch) + step)
        
        ##print(ch,ch2,step,buff)
        
        return buff
    
    plaintext = plaintext.upper()
    key = key.upper()
    
    ciphertext = ''
    index = 0
    for symbol in plaintext:
        ciphertext += symbol_shift_r(symbol, key[index % len(key)])
        index+=1
    return ciphertext


def decrypt_vignere(ciphertext,key):
    
    def symbol_shift_l(ch,ch2):
        """берет символ из ciphertext и из ключа и делает сдвиг но влево, как в шифре цезаря"""
        step = ord(ch2) % 1039
        if ord(ch) - step < 1040:
            buff = chr(ord(ch) - step + 32)
        else:
            buff = chr(ord(ch) - step)
        
        return buff

    
    ciphertext = ciphertext.upper()
    key = key.upper()
    
    plaintext = ''
    index = 0
    for symbol in ciphertext:
        plaintext += symbol_shift_l(symbol, key[index % len(key)])
        index+=1
        
    return plaintext


def kassiski(ciphertext,size):
    '''реализация медода касииски, возвращает словарь расстояний между постореними и их НОД'''
    ciphertext = ciphertext.upper()
    
    
    def get_dict_l_gramms(text, size):
        '''возвращает словарь лграмм, повторяющихся более чем 2 раза'''
        lgramms = {}
        for i in range(len(ciphertext)-size):
            buff = ciphertext[i:i+size]
            
            count = ciphertext.count(buff) 
            if count > 2:
                lgramms[buff] = count
        return lgramms
    
    def get_step_list(ciphertext,dict_l_gramms):
        """возвращает список индексов встречающихся лграмм"""
        for val in dict_l_gramms.keys():
            string = ciphertext
            r = list()
            
            while (string.rfind(val) != -1):
                index = string.rfind(val)
                string = string[:index]
                r.append(index)
            
            dict_l_gramms[val] = r
        
        return dict_l_gramms
    
    def get_nod_list(dictionary):
        """возвращает список расстояний между соседними  индексами встречания лграмм"""
        for val in dictionary.keys():
            steps = []
            for i in range(len(dictionary[val])-1):
                steps.append(dictionary[val][i] - dictionary[val][i+1])
            
            dictionary[val] = steps
            
        return dictionary
    
    
    def nod(a,b):
        """поиск нода"""
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    
    
    def get_sum_nod(dictionary):
        """возвращает нод для списка расстояний"""
        for val in dictionary.keys():
            
            k = nod(dictionary[val][0],dictionary[val][1])
            for i in range(2,len(dictionary[val])):
                k = nod(k,dictionary[val][i])
            
            dictionary[val] = [dictionary[val],k]  ####################
        return dictionary
        
    a = get_dict_l_gramms(ciphertext,size)
    b = get_step_list(ciphertext,a)
    c = get_nod_list(b)
    d = get_sum_nod(c)
    return d
    

def clear_text_from_symbols(text,_range):
    """очень некрасивая , но работающая очистка от лишних символов в тексте"""
    string = text.upper()
    for symbol in text:
        if  not (ord(symbol) in _range):
            string = string.replace(symbol,'')
    return string

def replace_letters(text,_range):
    """очень некрасивая , но работающая очистка от лишних символов в тексте"""
    string = text.upper()
    for symbol in text:
        if  (ord(symbol) in _range):
            string = string.replace(symbol,'∴')
    return string 


def put_letters_back(text,secrettext):
    inputtext = ''
    index = 0
    for i in range(len(secrettext)):
        if secrettext[i] == '∴':
            inputtext += text[index]
            index += 1
        else:
            inputtext += secrettext[i]
            
    
    return inputtext


def clear_text_from_symbols_vignere(text,_range):
    """очень некрасивая , но работающая очистка от лишних символов в тексте"""
    string = text.upper()
    for symbol in text:
        if  not (symbol in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
            string = string.replace(symbol,'')
    return string

def replace_letters_vignere(text,_range):
    """очень некрасивая , но работающая очистка от лишних символов в тексте"""
    string = text.upper()
    for symbol in text:
        if  (symbol in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
            string = string.replace(symbol,'∴')
    return string 

def put_letters_back_vignere(text,secrettext):
    inputtext = ''
    index = 0
    for i in range(len(secrettext)):
        if secrettext[i] == '∴':
            inputtext += text[index]
            index += 1
        else:
            inputtext += secrettext[i]
            
    
    return inputtext
'''        
#проверка на английском
def check(name,key):
    f = open(name,'r')
    ciphertext = f.read()
    ciphertext = clear_text_from_symbols(ciphertext,range(65,91))
    #ciphertext = encrypt_vignere(plaintext,key)
    b = kassiski(ciphertext)
    return b
'''  
    


def final_kassiski(filename,size):
    def nod(a,b):
        """поиск нода"""
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    

    def analysis(lst):
        dct = {}
        for i in lst:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1  
        return dct
            
    size = int(size)
    f = open(filename,'r')
    ciphertext = f.read()
    ciphertext = clear_text_from_symbols_vignere(ciphertext,range(1040,1072))
    kdict = kassiski(ciphertext,size)
    f.close()
    
    f = open( filename + "-kassiski-analyse.txt","w")
    for key in kdict.keys():
        buff = str(key)+'   НОД: ' + str(kdict[key][1]) + ' Список шагов: ' + str(kdict[key][0]) + '\n' 
        f.write(buff)
       
    
    #здесь у меня много кода о том как я искал предполагаемое значение ключа
    buff_list = kdict.values()    
    #print(buff_list)
    nod_list = []
    for i in buff_list:
        if i[1] != 1:
            nod_list.append(i[1])
    
    nod_dict = analysis(nod_list)
    
    #print(nod_dict)
    b = {}
    for i in nod_dict.keys():
        b[nod_dict[i]] = i
        
    
    #найти нок двух самых частых ключей
    if len(b.keys()) > 1:
        rr = list(sorted(b.keys(),reverse = True))
        f.write('\n Предполагаемая длина ключа:' + str(nod(b[rr[0]],b[rr[1]])))
    elif len(b.keys()) == 1:
        f.write('\n Предполагаемая длина ключа:'+str(list(b.keys())[0]))
    else:
        f.write('\n'+"ДЛИНА КЛЮЧА НЕ НАЙДЕНА")
        
    
    
    
    ###############################
    
    f.close()
    return kdict

def get_filename(fullname):
    lst = fullname.split('\\')
    name = lst[len(lst)-1]
    return name
    
# НА АНГЛИЙСКОМ
def rail_encipher(filename,height):
    height = int(height)
    #print(filename)
    f = open(filename,'r')
    plaintext = f.read()
    plaintext = plaintext.upper()
    f.close()
    
    eng_range = range(65,91)
    #заменить символы на звездочки
    secrettext = replace_letters(plaintext,eng_range)
    #удалить лишние символы
    plaintext = clear_text_from_symbols(plaintext,eng_range)
    #шифрование
    ciphertext = encrypt_rails(plaintext,height)
    ciphertext = put_letters_back(ciphertext,secrettext)
    #сохранение файла в рабочей директории
    f = open(filename+ "-rails-decoded.txt","w")
    f.write(ciphertext)
    return ciphertext
   

def rail_decipher(filename,height):
    height = int(height)
    f = open(filename,'r')
    plaintext = f.read()
    plaintext = plaintext.upper()
    f.close()
    
    eng_range = range(65,91)
    #заменить символы на звездочки
    secrettext = replace_letters(plaintext,eng_range)
    #удалить лишние символы
    plaintext = clear_text_from_symbols(plaintext,eng_range)
    #шифрование
    ciphertext = decrypt_rails(plaintext,height)
    ciphertext = put_letters_back(ciphertext,secrettext)
    #сохранение файла в рабочей директории
    f = open(filename+ "-rails-encoded.txt","w")
    f.write(ciphertext)
    return ciphertext

    
#НА АНГЛИЙСКОМ
def column_encipher(filename,key):
    f = open(filename,'r')
    plaintext = f.read()
    plaintext = plaintext.upper()
    f.close()
    eng_range = range(65,91)
    #заменить символы на звездочки
    secrettext = replace_letters(plaintext,eng_range)
    ##print(secrettext)
    #удалить лишние символы
    plaintext = clear_text_from_symbols(plaintext,eng_range)
    #шифрование
    ciphertext = encrypt_column(plaintext,key)
    ciphertext = put_letters_back(ciphertext,secrettext)
    #сохранение файла в рабочей директории
    f = open(filename+ "-column-decoded.txt","w")
    f.write(ciphertext)
    return ciphertext
    
  
    
def column_decipher(filename,key):
    f = open(filename,'r')
    plaintext = f.read()
    plaintext = plaintext.upper()
    f.close()
    eng_range = range(65,91)
    #заменить символы на звездочки
    secrettext = replace_letters(plaintext,eng_range)
    ##print(secrettext)
    #удалить лишние символы
    plaintext = clear_text_from_symbols(plaintext,eng_range)
    #шифрование
    ciphertext = decrypt_column(plaintext,key)
    ciphertext = put_letters_back(ciphertext,secrettext)
    #сохранение файла в рабочей директории
    f = open(filename + "-column-decoded.txt","w")
    f.write(ciphertext)
    return ciphertext

#НА АНГЛИЙСКОМ

def vignere_encipher(filename,key):
    f = open(filename,'r')
    plaintext = f.read()
    plaintext = plaintext.upper()
    f.close()
    #заменить символы на звездочки
    secrettext = replace_letters_vignere(plaintext,range(1040,1072))
    #удалить лишние символы
    plaintext = clear_text_from_symbols_vignere(plaintext,range(1040,1072))
    #шифрование
    #print(secrettext)
    ciphertext = vignere_new_encrypt(plaintext,key)
    #print(ciphertext)
    ciphertext = put_letters_back_vignere(ciphertext,secrettext)
    #print(ciphertext)
    #сохранение файла в рабочей директории
    f = open(filename+ "-vignere-encoded.txt","w")
    f.write(ciphertext)
    return ciphertext

def vignere_decipher(filename,key):
    f = open(filename,'r')
    plaintext = f.read()
    plaintext = plaintext.upper()
    f.close()
    #заменить символы на звездочки
    secrettext = replace_letters_vignere(plaintext,range(1040,1072))
    #print(secrettext)
    #удалить лишние символы
    plaintext = clear_text_from_symbols_vignere(plaintext,range(1040,1072))
    #print(plaintext)
    #шифрование
    ciphertext = vignere_new_decrypt(plaintext,key)
    #print(ciphertext)
    ciphertext = put_letters_back_vignere(ciphertext,secrettext)
    #print(ciphertext)
    #сохранение файла в рабочей директории
    f = open(filename+ "-vignere-decoded.txt","w")
    f.write(ciphertext)
    return ciphertext
    
    
    
    
    
    
    
    
def vignere_new_encrypt(plaintext,key):
    
    
    def symbol_shift_r(ch,ch2):
        
        alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        """берет символ из ciphertext и из ключа и делает сдвиг но влево, как в шифре цезаря"""
        
        pos1 = alpha.find(ch)
        pos2 = alpha.find(ch2)
        
        if (pos1+pos2) > len(alpha)-1:
            buff = alpha[pos1+pos2-len(alpha)]
        else:
            buff = alpha[pos1+pos2]
        
        return buff
    
    
    plaintext = plaintext.upper()
    key = key.upper()
    
    ciphertext = ''
    index = 0
    
    for symbol in plaintext:
        ciphertext += symbol_shift_r(symbol, key[index % len(key)])
        index += 1
        
    return ciphertext


def vignere_new_decrypt(plaintext,key):
    
    
    def symbol_shift_l(ch,ch2):
        
        alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        """берет символ из ciphertext и из ключа и делает сдвиг но влево, как в шифре цезаря"""
        
        pos1 = alpha.find(ch)
        pos2 = alpha.find(ch2)
        
        if (pos1-pos2) < 0:
            buff = alpha[pos1-pos2+len(alpha)]
        else:
            buff = alpha[pos1-pos2]
        
        return buff
    
    
    plaintext = plaintext.upper()
    key = key.upper()
    
    ciphertext = ''
    index = 0
    
    for symbol in plaintext:
        ciphertext += symbol_shift_l(symbol, key[index % len(key)])
        index += 1
        
    return ciphertext
    
    
    
    
    
    
    
    
    
    
    
    