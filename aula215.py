# Associação

class Escritor:
		def __init__(self, nome) -> None:
				self.nome = nome
				self._ferramenta = None
		
		@property
		def ferramenta(self):
				return self._ferramenta
		
		@ferramenta.setter
		def ferramenta(self, ferramenta):
				self._ferramenta = ferramenta

class FerramentaDeEscrever:
		def __init__(self, nome):
				self.nome = nome
		
		def escrever(self):
				return f'{self.nome} está escrevendo'

escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())    # Caneta Bic está escrevendo
print(maquina_de_escrever.escrever())    # Máquina está escrevendo
print(escritor.ferramenta.escrever())    # Máquina está escrevendo

#################################
# Agregação:

class Carrinho:
		def __init__(self):
				self._produtos = []
		
		def total(self):
				return sum([p.preco for p in self._produtos])
		
		def inserir_produtos(self, *produtos):
				# self._produtos.extend(produtos)
				# self._produtos += produtos
				for produto in produtos:
						self._produtos.append(produto)
		
		def lista_produtos(self):
				print()
				for produto in self._produtos:
						print(produto.nome, produto.preco)
				print()

class Produto:
		def __init__(self, nome, preco):
				self.nome = nome
				self.preco = preco
		
carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)  
carrinho.listar_produtos()
print(carrinho.total())

#################################
# Composição:

class Cliente:
		def __init__(self, nome):
				self.nome = nome
				self.enderecos = []
		
		def inserir_endereco(self, rua, numero):
				self.enderecos.append(Endereco(rua, numero))
		

class Endereco:
		def __init__(self, rua, numero):
				self.rua = rua
				self. numero = numero

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)

print(cliente1.enderecos)    # veremos uma lista de ponteiros para as instâncias da classe Endereco
print(cliente1.enderecos[0].rua)    # Av Brasil
print(cliente1.enderecos[1].rua)    # Rua B