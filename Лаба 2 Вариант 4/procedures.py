# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:18:04 2017

@author: Vlad
"""

def get_xor_for_list(list_of_bites):
    '''Берет массив 1 и 0 (целых чисел), и находит их суммарное исключающее или'''
    xor = 0
    for i in list_of_bites:
        xor = xor ^ i
    return xor
    
def get_register_shift(register,set_indexes):
    '''Принимает регистр (строку битов), массив индексов - элементов регистра, учавствующих в расчете вставляемого символа.
    Возворащает строку со сдвигом на один влево'''
    index = 1
    symbols_for_count = []
    for symbol in register:
        if index in set_indexes:
            symbols_for_count.append(int(symbol))
        index += 1
    #count incert symbol
    xor = get_xor_for_list(symbols_for_count)
    
    register = register[1:] + str(xor)
    
    return register
    

def generate_key_for_lfsr(register,set_indexes,length):
    '''Принимает регистр (строку битов),массив индексов - элементов регистра, учавствующих в расчете вставляемого символа и длину исходного текста.
    Возвращает ключ'''
    buff_register = register
    key = ''
    for i in range(length):
        key += buff_register[:1]
        buff_register = get_register_shift(buff_register,set_indexes)
    
    return key

def lfsr(register,plaintext,set_indexes):
    '''Принимает регистр (строку битов),массив индексов - элементов регистра, учавствующих в расчете вставляемого символа и  исходный текст
    возвращает зашифрованный текст'''
    
    key = generate_key_for_lfsr(register,set_indexes,len(plaintext))
    ciphertext = ''
    for i in range(len(key)):
        ciphertext += chr(ord(plaintext[i]) ^ int(key[i]))
        
    return ciphertext

def lfsr_for_file(filename,register):
    '''Для взаимодействия с окном. 
    Принимает имя файла, открывает, считывает его, шифрует и записывает в файл рядом'''
    
    f = open(filename,'r')
    plaintext = f.read()
    f.close()
    
    set_indexes = [26,8,7,1]
    ciphertext = lfsr(register,plaintext,set_indexes)
    
    f = open(filename + '-lfsr.txt','w')
    f.write(ciphertext)
    f.close()
    
    return ciphertext

def generate_geffe_key(plaintext,register_0,register_1,register_2,sets):
    '''Принимает текст, 3 регистра, и список списков индексов - элементов регистра для расчетов
    возвращает шифротекст'''
    
    key_0 = generate_key_for_lfsr(register_0,sets[0],len(plaintext))
    key_1 = generate_key_for_lfsr(register_1,sets[1],len(plaintext))
    key_2 = generate_key_for_lfsr(register_2,sets[2],len(plaintext))
    
    geffe_key = ''
    
    for i in range(len(key_0)):
        geffe_key += str((int(key_0[i]) & int(key_1[i])) | ((int(not int(key_0[i]))) & int(key_2[i])))
    
    return geffe_key



def geffe(plaintext,register_0,register_1,register_2,sets):
    
    key = generate_geffe_key(plaintext,register_0,register_1,register_2,sets)
    ciphertext = ''
    for i in range(len(key)):
        ciphertext += chr(ord(plaintext[i]) ^ int(key[i]))
        
    return ciphertext


def geffe_for_file(filename,register_0,register_1,register_2):
    
    f = open(filename,'r')
    plaintext = f.read()
    f.close()
    
    sets = [[26,8,7,1],[34,15.14,1],[24,4,3,1]]
    ciphertext = geffe(plaintext,register_0,register_1,register_2,sets)
    
    f = open(filename + '-lfsr.txt','w')
    f.write(ciphertext)
    f.close()
    
    return ciphertext
