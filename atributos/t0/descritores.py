class Quantidade(object):
    def __init__(self, nome_atr):
        self.nome_atr = nome_atr
        self.nome_atr_interno = '__'+nome_atr

    def __get__(self, instance, owner):
        return getattr(instance, self.nome_atr_interno)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.nome_atr_interno, value)
        else:
            raise TypeError('%s deve ser > 0' % self.nome_atr)
