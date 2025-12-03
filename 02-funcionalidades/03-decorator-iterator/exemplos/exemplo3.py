def decorador(fn):
    def saudacao_melhorada(*args, **kwargs):
        print("Bom dia")
        return fn(*args, **kwargs)
    return saudacao_melhorada

@decorador
def saudacao(nome):
    print(f"Olá, {nome}!")


saudacao("turma")