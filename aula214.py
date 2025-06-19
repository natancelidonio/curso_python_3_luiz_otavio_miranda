class Foo:
		def __init__(self):
				self._protected = 'isso é protegido'

		def _metodo_protected(self):
				return '_metodo_protected'

f = Foo()
print(f._protected)    # isso é protegido
print(f._metodo_protected())    # _metodo_protected


########### # Name mangling

class Foo:
		def __init__(self):
				self.__private= 'isso é privado'

		def __metodo_private(self):
				return '__metodo_private'

f = Foo()
print(f.__private)    # isso é privado
print(f.__metodo_private())    # isso vai gerar um erro, pois o nome do método foi alterado, isso é chamado de name mangling

"""Traceback (most recent call last):
  File "c:\codigosEstudo\curso_python_3_luiz_otavio_miranda\aula214.py", line 23, in <module>
    print(f.__private)    # isso é privado
          ^^^^^^^^^^^
AttributeError: 'Foo' object has no attribute '__private'. Did you mean: '_Foo__private'?
"""