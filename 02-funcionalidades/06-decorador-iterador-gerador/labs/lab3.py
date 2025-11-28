class Contador:
    def __init__(self, limite):
        self.atual = 0
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual >= self.limite:
            raise StopIteration
        valor = self.atual
        self.atual += 1
        return valor

for numero in Contador(5):
    print(numero)