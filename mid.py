import sys

result = 0


def euclid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def gcdex(a, b):
    global result
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        result = y
        return d, y, x - y * (a // b)


def mid(a, b):
    n = a * b
    fi = (a-1)*(b-1)

    '''for e in range(69, fi):
        if euclid(e, fi) == 1:
            break'''

    e = 433

    gcdex(e, fi)
    d = result
    open_key = (e, n)
    secret_key = (d, n)
    m = 1488
    c = (pow(m, e) % n)
    decyph = (pow(c, d) % n)
    print('Open key= {} \nSecret Key= {} \nMessage = {} \n'
          'Cypher = {} \nDecyphered = {} \nFi = {}'.format(open_key, secret_key, m, c, decyph, fi))



if __name__ == '__main__':
    mid(int(sys.argv[1]), int(sys.argv[2]))
