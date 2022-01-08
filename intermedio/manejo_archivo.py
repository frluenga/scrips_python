def read():
    numbers = []
    with open('numbers.txt','r',encoding='utf-8') as f:
        for line in f:
            
            numbers.append(int(line))
    print(numbers)



def write():
    names = ['Fabian','Miguel','Pepe','Christian','maría','fernanda']
    with open('.\prueba.txt','a',encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    read()
    write()

if __name__ == '__main__':
    run()