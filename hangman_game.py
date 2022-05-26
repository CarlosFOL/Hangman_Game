#List and dicts comprehension
#Manejo de errores y de archivos
import os
import random

def hangman_game(dic, word_list):
    hidden_list = []
    random_nummber = random.choice(range(0, 118))
    for i, word in enumerate(word_list):
        if i == random_nummber:
            key = word
    print(key)
    for k, v in dic.items():
        if k == key:
            word_in_slices = v
            for i in range(len(word_in_slices)):
                hidden_list.append('-')
            print(''.join(hidden_list))
            for i in range(len(key)+3):
                attempt = input('')
                for i, character in enumerate(word_in_slices):
                    if character == attempt:
                        hidden_list[i] = attempt
                os.system('cls')
                print(''.join(hidden_list))
            
def slices(word):
    list_characters = []
    for i in range(len(word)):
        list_characters.append(word[i])
    return list_characters

def database(word_list):
    dic = {}
    for word in word_list:
        dic[word] = slices(word)
    hangman_game(dic, word_list)

def run():
    with open('./archivos/data.txt', 'r', encoding="utf-8") as f:
        words_list = [i.strip('\n') for i in f]   
    database(words_list)

if __name__=='__main__':
    run()