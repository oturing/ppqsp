#!/usr/bin/env python

a = 10
b = 20
c = 30
d = 40

def func_a():
    print a # this is a reference to the global variable
    return 'result of func_a'

def func_b():
    print b # referencing 'b' here causes UnboundLocalError
    assert False, 'this line is never executed'
    b = 22
    return 'result of func_b'

def func_c():
    print c # referencing 'c' here causes UnboundLocalError
    if False:
        c = 33 # this line is unreachable, but the compiler sees c on the
        # left side of an assignment, and treats it as a local variable
    return 'result of func_c'

def func_d():
    print d # this is a reference to the global variable
    def inner():
        d = 33 # this creates a variable local to inner
    inner()
    return 'result of func_d'

def test_a():
    res_a = ''
    res_a = func_a()
    assert res_a == 'result of func_a'

def test_b():
    res_b = ''
    try:
        res_b = func_b()
    except UnboundLocalError as e:
        assert e.args[0] == "local variable 'b' referenced before assignment"
    else:
        assert False, 'an UnboundLocalError excepion was expected but not raised'
    assert res_b == ''

def test_c():
    res_c = ''
    try:
        res_c = func_c()
    except UnboundLocalError as e:
        assert e.args[0] == "local variable 'c' referenced before assignment"
    else:
        assert False, 'an UnboundLocalError excepion was expected but not raised'
    assert res_c == ''

def test_d():
    res_d = ''
    res_d = func_d()
    assert res_d == 'result of func_d'

if __name__=='__main__':
    test_a()
    test_b()
    test_c()
    test_d()
    '''
    import dis
    dis.dis(func_a.__code__.co_code)
    print '*' * 70
    dis.dis(func_b.__code__.co_code)
    '''
