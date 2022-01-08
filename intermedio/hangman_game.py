from random import randint
import os

def read():
    words = []
    with open('data.txt','r',encoding='utf-8') as f:
        for line in f:
            words.append(line.strip('\n'))
    return words

def accents(list):
    new_list = list.maketrans('áéíóú','aeiou')
    n_list = list.translate(new_list)
    return n_list

def select_word(list):
    n = randint(1,len(list))
    return list[n]
    
def print_main():
    print('- '*10)
    print(' 1.JUGAR\n','2.SALIR')
    print('- '*10)
    sel = int(input('Por favor, Selecciona una opción [1/2]: '))
    assert sel == 1 or sel == 2, 'Selecciona una opción correcta'
    return sel

def chars(word):
    dict_ = {i:i for i in range(1,len(word)+1)}
    k = 1
    for c in word:
        dict_[k] = c
        k += 1      
    return dict_

def input_char():
    char_ = input('Escribe una letra: ')
    if len(char_) == 0:
        raise ValueError()
    elif len(char_) >= 2:
        raise ValueError()
    return char_

def show_char(word_dict):
    char_ = len(word_dict)
    dic_temp = {i:'_' for i in range(1,char_+1)}
    while dic_temp != word_dict:
        a = input_char()
        dic_temp = eval_char(word_dict,a,dic_temp)
        print(dic_temp.values())
    return dic_temp

def eval_char(word_dict,a,dic_temp):
    for key,value in word_dict.items():
        if a in value:
            dic_temp[key] = value
    os.system("cls")
    return dic_temp
 
def run():
    words = read()
    words = [accents(word) for word in words]
    word_select = select_word(words)
    dict_ = chars(word_select)

    try:
        while True:
            opc = print_main()
            if opc == 1:
                list_ = show_char(dict_)
                print(f'Ganaste, La palabra era {word_select.upper()}' )
            elif opc == 2:
                break
    except ValueError:
        print('Selecciona una opción correcta')

    
        
if __name__ == '__main__':
    run()