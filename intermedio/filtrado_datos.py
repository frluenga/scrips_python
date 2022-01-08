from functools import reduce
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization']=='platzi']
    adults = list(filter(lambda worker:worker['age'] >= 18, DATA))
    adults = list(map(lambda worker: worker['name'],adults))
    # print(adults)
    # Unir a un diccionario con otro nuevo con py | sumar diccionarios o iterar entre ambos
    # para cada uno de los diccionarios que estan dentro de data
    # va a guardar si es verdadero o falso
    old_people = list(map(lambda worker: worker | {"old":worker['age'] > 70},DATA))
    name_old = list(filter(lambda worker: worker['old'],old_people))
    name_old_ = list(map(lambda worker: worker['name'],name_old))
    ages = list(map(lambda worker:worker['age'],DATA))
    sum_age = reduce(lambda a,b: a+b,ages)/ len(ages)
    print(sum_age)

def funcion_con_parametro(parametro):
    return parametro**2



if __name__ == '__main__':
    numero = int(input('Escribe un numero: '))
    resultado = funcion_con_parametro(numero)
    print(resultado)
