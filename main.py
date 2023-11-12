from graph import Graph

def main():
    graph = Graph('netflix_titles.csv')
    # graph.display()
    while True:
        name = input("Digite o nome do ator: ")
        path = graph.get_path_from_kevin(name)
        print(f"\nO número de conexões entre Kevin Bacon e {name} é {len(path)}\nAqui está o caminho entre eles: {path}.\n")
        print("O que deseja agora?\na. Buscar outra conexão\nb. Sair\n")
        next_step = input("Selecione 'a' ou 'b': ").lower().strip()
        while next_step != 'a' and next_step != 'b':
            next_step = input("Selecione uma opção válida: ")
        if next_step == 'b':
            break
        
            

if __name__ == '__main__':
    main()