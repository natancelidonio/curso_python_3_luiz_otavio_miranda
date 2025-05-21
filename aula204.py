# atributos de classe


class Pessoa:
    ANO_ATUAL = 2025
    atributo = 'valor'
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade
    
p1 = Pessoa('João', 32)


print(p1.__dict__)
print(vars(p1))

p1.__dict__['outra'] = 'coisa'
p1.__dict__['nome'] = 'EITA'
del p1.__dict__['idade']
 
print(p1.__dict__)
print(vars(p1))
