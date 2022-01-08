from operator import itemgetter, attrgetter
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name,self.grade,self.age))

def run():
    twit = 'Este es un Twitt de prueba para empezar a manejar caracteres'
    v_twit = sorted(twit.split(), key=str.lower)

    student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ]

    student_objects = [
        Student('Jhon','A',15),
        Student('Jane','B',12),
        Student('Dave','B',10)
    ]

    Obj = sorted(student_objects,key= lambda student: student.age)
    # Importando el modulo operator se hace mas facil
    sorted(student_objects,key=itemgetter(2))
    sorted(student_objects, key= attrgetter('grade','age'))
    # Importante: Si quieres hacerlo descendente o ascendente se puede
    # con un valor booleano para reverse = True
    sorted(student_objects,key=itemgetter(2),reverse=True)
if __name__ == '__main__':
    run()

