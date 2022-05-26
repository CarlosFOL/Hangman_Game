#List and dicts comprehension
#Manejo de errores y de archivos
def slices(word):
    list_characters = []
    for i in range(len(word)):
        list_characters.append(word[i])
    return list_characters

def database(word_list):
    dic = {}
    for word in word_list:
        dic[word] = slices(word)
    print(dic)

def run():
    with open('./archivos/data.txt', 'r', encoding="utf-8") as f:
        words_list = [i.strip('\n') for i in f]   
    database(words_list)

if __name__=='__main__':
    run()

"""
import os
import random

def run():
    lista_random = ['car', 'aire']
    dic = {
        'car': ['c', 'a', 'r'],
        'aire': ['a','i','r','e']
    }
    lista_2 = []
    palabra_aleatoria = random.choice(range(0, 2))
    print(palabra_aleatoria)
    for i, word in enumerate(lista_random):
        if i == palabra_aleatoria:
            llave = word
            print(llave)
    for k, v in dic.items():
        if llave == k:
            lista = v
            for i in range(len(lista)):
                lista_2.append('-')
            print(''.join(lista_2))
            for i in range(4):
                attempt = input('')
                for i, c in enumerate(lista):
                    if c == attempt:
                        lista_2[i] = attempt
                os.system('cls')
                print(''.join(lista_2))
            if ((''.join(lista_2))== (''.join(lista))):
                print('Ganaste')
                break
            else:
                print('Malardo')

if __name__=='__main__':
    run()
"""


"""
#FUNCION ENUMERATE
lista = ['C++', 'JavaScript', 'Python']
    for i,  lenguaje in enumerate(lista):
        print(i, lenguaje) => [(0, 'C++'), (1, 'JavaScript'), (2, 'Python')]
#METODO GET
    dic = {
        1: 'Hola',
        2:'Que tal',
        3: 'La sacas a bailar',
        4: 'Sexo'
    }
    print(dic.get(5, "The key doesn't exist")) => 'The key doesn't exist'| Because 5 isn't in the dict
"""

