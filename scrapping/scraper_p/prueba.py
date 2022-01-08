
links = [1,2,3,4,5]
hosts = [1,2,3,4,5]

section = []

def run():
    for link in links:
        for host in hosts:
            section.append(_build_link(host,link))
    return section

def _build_link(host,link):
    return f'{host}{link}'


if __name__ == '__main__':
    print(run())