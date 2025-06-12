caminho_arquivo = 'C:\\codigosEstudo\\curso_python_3_luiz_otavio_miranda\\'
caminho_arquivo += 'aula186_criando_arquivo.txt'

# arquivo = open(caminho_arquivo, 'w')
# 
# arquivo.close()

with open(caminho_arquivo, 'w') as arquivo:
		print('Olá Mundo')
		print('O arquivo será fechado.')