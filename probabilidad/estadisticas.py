import random
import numpy as np

def media(x):
    return np.mean(x)

def var(x):
    return np.var(x)

def desviacionstd(x):
    return np.std(x)

if __name__ == '__main__':
    X = [random.randint(1,10) for i in range(20)]
    mu = media(X)
    varianza = var(X)
    stdar = desviacionstd(X)

    print(X)
    print(mu)
    print(varianza)
    print(stdar)

    