def make_multiplier(x):
    def multiplier(n):
        return x*n
    return multiplier

def run():
    times10 = make_multiplier(10)
    times4 = make_multiplier(4)

    print(times10(3))
    print(times4(5))
    print(times10(times4(2)))


if __name__ == '__main__':
    run()
