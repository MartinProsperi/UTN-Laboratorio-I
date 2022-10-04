import json
import copy

from sympy import li

def cargar_json(path:str):
    '''

    '''
    with open(path,"r") as file:
        lista_personajes = json.load(file)
    return lista_personajes
'''
def personajes_por_altura(lista:list)->list:
    
    Recibe una lista
    Ordena los elementos a partir del parametro 'altura'
    Devuelve una copia de la lista con los elementos reordenados
    
    lista_a_ordenar = copy.deepcopy(lista)
    
    maximo = lista[0]["height"]
    for elemento in lista:
        if(elemento["height"] > maximo)
'''
def set_de_keys(lista:list, key:str)->set:
    '''
    Recibe una lista cuyos elementos sean diccionarios
    Agrupa a una key de los diccionarios en una lista y la cambia a un set, para eliminar repeticiones
    Devuelve un set de todos los valores unicos entre las keys
    '''
    set_de_keys = []

    for elementos in lista:
        set_de_keys.append(elementos[key])
    
    set_de_keys = set(set_de_keys)
    return set_de_keys

def mas_alto_por_cada_genero(lista:list)->list:
    set_de_generos = set_de_keys(lista, "gender")

    for elementos in set_de_generos:
        set_de_generos{elementos} = {}
        for personajes in lista:
            if(set_de_generos{elementos} == personajes["gender"])
                set_de_generos{elementos}.append()
                set_de_generos{elementos}.append()
