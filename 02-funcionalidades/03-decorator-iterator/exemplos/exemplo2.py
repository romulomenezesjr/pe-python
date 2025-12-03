def decorador(fn):
    def saudacao_melhorada():
        print("Bom dia")
        return fn()
    return saudacao_melhorada

@decorador
def saudacao():
    print("Olá, mundo!")


saudacao()