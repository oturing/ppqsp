# coding: utf-8

import string

def mod11(digitos):
    digitos = reversed([int(d) for d in str(digitos) if d in string.digits])
    soma = sum((mult+2)*digito for mult, digito in enumerate(digitos))
    dv = (11 - soma % 11)
    return str(dv) if dv < 10 else '0'

def mod11_cpf(digitos):
    dv1 = mod11(digitos)
    dv2 = mod11(digitos+dv1)
    return dv1+dv2

def cpf_valido(digitos):
    digitos = ''.join([d for d in str(digitos) if d in string.digits])
    if len(digitos) != 11:
        return False
    dv = mod11_cpf(digitos[:-2])
    return dv == digitos[-2:]

def testes():
    # CPFs de deputados listados em um processo publicado na Web
    cpfs = '''102.700.605-10 216.307.552-49 242.544.011-91 568.755.847-00
              006.375.133-04 348.780.507-30 244.884.451-87 254.052.509-10
              030.880.653-00 117.703.681-91 825.025.018-49
              030.166.509-59'''.split()

    for cpf in cpfs:
        assert cpf_valido(cpf)
        print cpf, mod11_cpf(cpf[:-2]), cpf_valido(cpf)

    for i in range(10):
        s = str(i)*9
        print s, mod11_cpf(s)

    s = '012345678'
    print s, mod11_cpf(s)
    s = s[::-1]
    print s, mod11_cpf(s)
    s = '123456789'
    print s, mod11_cpf(s)
    s = s[::-1]
    print s, mod11_cpf(s)
    s = '123454321'
    print s, mod11_cpf(s)
    s = '010101010'
    print s, mod11_cpf(s)
    s = '101010101'
    print s, mod11_cpf(s)

if __name__=='__main__':
    testes()