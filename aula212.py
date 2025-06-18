class Caneta:
    def __init__(self, cor):
            self.cor_tinta = cor
    
    @property
    def cor(self):
            print('FAZENDO QUALQUER COISA')
            return self.cor_tinta
            
    @property
    def cor_tampa(self):
            return 123456

caneta = Caneta('Azul')
print(caneta.cor)
# FAZENDO QUALQUER COISA
# Azul
print(caneta.cor_tampa)    # 123456