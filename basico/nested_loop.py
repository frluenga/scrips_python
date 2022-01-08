def f(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

def main():
    numero = int(input('Escribe: '))
    print(f(numero))
           
if __name__ == '__main__':
    main()