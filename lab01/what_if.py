def ab(c, d):
    '''
    >>>ab(10,20)
    10
    foo
    '''
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')


>>> ab(10, 20)
def bake(cake, make):
    '''
    >>> bake(0,29)
    1
    29
    29
    >>>bake(1, "mashed potatoes")
    mashed potatoes
    'mashed potatoes'
    '''
    if cake == 0:
        cake = cake + 1
    if cake == 1:
        print(make)
    else:
        return cake
    return make
bake(0,29)

'''
>>> True and 13
13
>>> False or 0
0
>>> not 10
False
>>> not None
True

>>> True and 1 / 0 and False
ZeroDivisionError
>>> True or 1 / 0 or False
True
>>> True and 0
0
>>> True and False
False
>>> False or 1
1
>>> 1 and 3 and 6 and 10 and 15
15
>>> -1 and 1 > 0
True
>>> 0 or False or 2 or 1 / 0
2

>>> not 0
True
>>> (1 + 1) and 1
1
>>> 1/0 or True
ZeroDivisionError
>>> (True or False) and False
False
'''