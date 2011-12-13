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

cpfs = '030.166.509-59 102.700.605-10 568.755.847-00'.split()

for cpf in cpfs:
    print cpf, mod11_cpf(cpf[:-2]), cpf_valido(cpf)

for i in range(10):
    s = str(i)*9
    print s, mod11_cpf(s)
