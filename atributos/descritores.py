class Quantidade(object):
    def __init__(self):
        self.nome_atr = self.__class__.__name__.lower()+str(id(self))
    def __set__(self, instance, valor):
        if valor < 1:
            raise TypeError('quantidade deve ser > 0')
        else:
            setattr(instance, '__'+self.nome_atr, valor)
    def __get__(self, instance, owner):
        nome_atr_real = '__'+self.nome_atr
        return getattr(instance, nome_atr_real) 
