class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        print('ENTER - ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
    
    def __exit__(self, class_excepction, exception_, traceback_):
        print('EXIT - FECHANDO ARQUIVO')
        self._arquivo.close()

instancia = MyOpen('aula240.txt', 'w')

with instancia as alguma_coisa:
    alguma_coisa.write('Escrevendo na linha 1\n')
    alguma_coisa.write('Escrevendo na linha 2\n')
    alguma_coisa.write('Escrevendo na linha 3, e assim por diante...\n')
    print('WITH', alguma_coisa)