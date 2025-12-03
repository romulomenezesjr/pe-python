def decorador(fn):
    def saudacao_melhorada():
        print("Bom dia")
        return fn()
    return saudacao_melhorada

def saudacao():
    print("Olá, mundo!")


saudacao_melhorada = decorador(saudacao)
saudacao_melhorada()