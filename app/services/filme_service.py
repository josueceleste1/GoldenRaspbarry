from app.repositories import filme_repository

def criar_tabela():
    return filme_repository.criar_tabela()

def importar_dados():
    return filme_repository.importar_dados()
    
def mostrar_dados():
    return filme_repository.mostrar_dados()

def obter_maior_intervalo_e_premio_mais_rapido():
    return filme_repository.obter_maior_intervalo_e_premio_mais_rapido()
