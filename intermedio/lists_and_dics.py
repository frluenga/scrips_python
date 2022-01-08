def run():
    from functools import reduce
    my_list = [1,2,3,4,5,6,7,8,9,10]
    my_dict = {'Firstname':'Fabian','Lastname':'Luengas'}
    super_list = [
        {'Firstname':'Fabian','Lastname':'Luengas'},
        {'Firstname':'Miguel','Lastname':'Torres'},
        {'Firstname':'Pepe','Lastname':'Rodelo'},
        {'Firstname':'Susana','Lastname':'Martinez'},
        {'Firstname':'Jose','Lastname':'García'}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    # for key,value in super_dict.items():
    #     print(f'{key} - {value }')

    list_ = [x for x in range(101) if x % 3 != 0]
    list_1 = list(map(lambda x:x**2,range(10)))
    list_2 = [x for x in range(1000) if x % 4 == 0 if x % 6 == 0 if x % 9 == 0]
    
    dict_ = {x: x**3 for x in range(100) if x % 3 != 0}
    dict_1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
    dict_tripleCond = {k:('even' if v%2==0 else 'odd') for k,v in dict_1.items()}

    nested_dict = {'first':{'a':1}, 'second':{'b':2}}
    float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} 
                        for (outer_k, outer_v) in nested_dict.items()}
    # print(float_dict)


    # FUNCIONES ANONIMAS:
    # despues de declararla como lambda se coloca los argumentos.
    
    palindrome = lambda string: string == string[::-1]
    

    # FUNCIONES DE ORDEN SUPERIOR (map, filter, reduce):

    # FILTER: Aplica una función de filtro a un iterable,
    # el cual devuelve un iterable ya filtrado, la función
    # interna esta retornando valores boolean, es decir
    # revisa dentro del iterable cuales cumplen la condición
    # el segundo parametro que recibe 'list' es el iterable
    # toca convertirlo en list, porque filter por si sola devuelve
    # es un iterador
    odd_ = list(filter(lambda x: x%2 != 0, my_list))


    # MAP: Aplica una función a un iterable, retorna un iterable
    # ya modificado o afectado por la función que ingreso como 
    # parametro a la función map. toca convertirlo en list, porque 
    # map por si sola devuelve es un iterador
    sq_ = list(map(lambda x: x**2,my_list))


    # REDUCE: opera todo los valores del iterable agrupando el resultado,
    # en un solo resultado
    rd_ = reduce(lambda a, b: a*b , my_list)
    print(rd_)


    # print(dict_tripleCond)

if __name__ == '__main__':
    run()