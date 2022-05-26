#List and dicts comprehension
#Manejo de errores y de archivos
def run():
     
    dic = {}
    dic_characters = {}
    with open('./archivos/data.txt', 'r', encoding="utf-8") as f:
        words_list = [i.strip('\n') for i in f]
    for i, word in enumerate(words_list, 1):
        dic[i] = word
    for word in dic.values():
        list_characters = []
        for i in range (len(word)):
            list_characters.append(word[i])
            dic_characters[word] = list_characters
    print(dic_characters)

    """
    word = 'sexo'
    lista = []
    for i in range(len(word)):
        lista.append(word[i])
    print(lista)
    """ 
    
if __name__=='__main__':
    run()

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
    