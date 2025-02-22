class MinhaClasse:
    def __enter__(self):
        print('Entrei...')
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Saindo...')
        
        
with MinhaClasse() as mc:
    print('Dentro do bloco with...')