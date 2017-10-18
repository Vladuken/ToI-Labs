# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:07:01 2017

@author: Tom
"""

def bytereadfile(filename):
    f = open(filename,'br')
    bytetext = f.read()
    return bytetext
    
def bytestr_to_binstr(line):
    '''Принимает битовую строку, превращает ее в строку из 0 и 1 (битов)'''
    final = ''
    for byte in line:
        
        res = bin(byte)[2:]
        res =(8-len(res))*'0' + res
        final += res
    return final
############################################################################


def get_xor_for_list(list_of_bites):
    '''Берет массив 1 и 0 (целых чисел), и находит их суммарное исключающее или'''
    xor = 0
    for i in list_of_bites:
        xor = xor ^ i
    return xor


def get_register_shift(register,set_indexes):
    '''Принимает регистр (строку 0 и 1), массив индексов - элементов регистра,
    учавствующих в расчете вставляемого символа.
    Возворащает строку со сдвигом на один влево'''
    index = 1
    symbols_for_count = []
    for symbol in register[::-1]:
        if index in set_indexes:
            symbols_for_count.append(int(symbol))
        index += 1
    #count incert symbol
    xor = get_xor_for_list(symbols_for_count)
    
    register = register[1:] + str(xor)
    
    return register


def generate_key_for_lfsr(register,set_indexes,length):
    '''Принимает регистр (строку битов),массив индексов - элементов регистра, 
    учавствующих в расчете вставляемого символа и длину исходного текста.
    Возвращает ключ'''
    buff_register = register
    key = ''
    for i in range(length):
        
        bff = ''
        for k in range(len(buff_register)):
            if k+1 in set_indexes:
                bff += ' '+ buff_register[k] + ' '
            else:
                bff+= buff_register[k]
        if i % 1000 == 0:
            print(i / length)
        #print(bff)
        #print(i)
        key += buff_register[:1]
        #if (i+1) % 8 == 0:
         #   key+=' '
            
        buff_register = get_register_shift(buff_register,set_indexes)
        
    return key


def lfsr(register,byteplaintext,set_indexes):
    '''Принимает регистр (строку из 0 и 1),массив индексов - элементов регистра, 
    учавствующих в расчете вставляемого символа и  исходный текст
    возвращает зашифрованный байттекст'''
    plaintext = bytestr_to_binstr(byteplaintext)
    key = generate_key_for_lfsr(register,set_indexes,len(plaintext))
    ciphertext = ''
    for i in range(len(key)):
        ciphertext += str(int(plaintext[i]) ^ int(key[i]))
    
    a = []
    
    for i in range(0,len(ciphertext),8): 
        a.append(int(ciphertext[i:i+8],2))
        
    ciphertext = bytes(a)    
    return (ciphertext,key)

def lfsr_for_file(filename,register):
    '''Для взаимодействия с окном. 
    Принимает имя файла, открывает, считывает его, шифрует и записывает в файл рядом'''
    
    f = open(filename,'br')
    plaintext = f.read()
    f.close()
    
    set_indexes = [26,8,7,1]
    tupl = lfsr(register,plaintext,set_indexes)
    ciphertext = tupl[0]
    key = tupl[1]
    f = open(filename + '-lfsr.' + filename.split('.')[-1],'bw')
    f.write(ciphertext)
    f.close()
    
    f = open(filename + '-lfsr_generatedkey.txt','w')
    f.write(key[:5000]);
    f.close()
    return key





########################################################################################33
def generate_geffe_key(plaintext,register_0,register_1,register_2,sets):
    '''Принимает текст, 3 регистра, и список списков индексов - элементов регистра для расчетов
    возвращает шифротекст'''
    
    key_0 = generate_key_for_lfsr(register_0,sets[0],len(plaintext))
    key_1 = generate_key_for_lfsr(register_1,sets[1],len(plaintext))
    key_2 = generate_key_for_lfsr(register_2,sets[2],len(plaintext))
    #print(key_0)
    #print(key_1)
    #print(key_2)
    geffe_key = ''
    
    for i in range(len(key_0)):
        geffe_key += str((int(key_0[i]) & int(key_1[i])) | ((int(~int(key_0[i]))) & int(key_2[i])))
    
    #print(geffe_key)
    return (geffe_key,key_0,key_1,key_2)


def geffe(byteplaintext,register_0,register_1,register_2,sets):
    ########################################33
    plaintext = bytestr_to_binstr(byteplaintext)
    tupl = generate_geffe_key(plaintext,register_0,register_1,register_2,sets)
    #print(tupl)
    geffe_key = tupl[0]
    ciphertext = ''
    for i in range(len(geffe_key)):
        ciphertext += str(int(plaintext[i]) ^ int(geffe_key[i]))
        
        
    a = []
    
    #print(ciphertext)
    for i in range(0,len(ciphertext),8): 
        a.append(int(ciphertext[i:i+8],2))
        
    ciphertext = bytes(a)  
    
    return (ciphertext,geffe_key,tupl[1],tupl[2],tupl[3])


def geffe_for_file(filename,register_0,register_1,register_2):
    
    f = open(filename,'br')
    plaintext = f.read()
    f.close()
    
    sets = [[26,8,7,1],[34,15.14,1],[24,4,3,1]]
 
    tupl = geffe(plaintext,register_0,register_1,register_2,sets)
    ciphertext = tupl[0]
    
    f = open(filename + '-geffe.' + filename.split('.')[-1],'bw')
    f.write(ciphertext)
    f.close()
    print(tupl)
    return tupl




###################################################################
    
def generate_rc4_s_block(key):
    '''Принимает строку - ключ, создает s-блок по ключу (список)'''
    S = []
    for i in range(256):
        S.append(i)
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i],S[j] = S[j],S[i] 
        
    return S

def generate_rc4_k(S,length):
    '''Принимает список (S-блок). Генерирует по нему псевдослучайный список K длины length'''
    
    i,j = 0,0
    K = []
    for r in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i],S[j] = S[j],S[i] 
        K.append(S[ (S[i] + S[j]) % 256 ])

    return K

def rc4(plaintext,key):
    '''принимает текст и ключ и шифрует RC4'''
    S = generate_rc4_s_block(key) 
    K = generate_rc4_k(S,len(plaintext))
    
    ciphertext = b''
    for i in range(len(K)):
        ciphertext += bytes([plaintext[i] ^ K[i]])
        
    return (ciphertext,K)



def rc4_for_file(filename,key):
    
    f = open(filename,'br')
    plaintext = f.read()
    f.close()
    
 
    tupl = rc4(plaintext,key)
    
    ciphertext = tupl[0]  
    key = str(tupl[1])
    f = open(filename + '-geffe.' + filename.split('.')[-1],'bw')
    f.write(ciphertext)
    f.close()
    #print(tupl)
    return (ciphertext,key)
