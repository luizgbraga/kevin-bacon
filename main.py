from graph import Graph
from colorama import Fore

def output_path(path):
    print("")
    for index, node in enumerate(path):
        if index == 0:
            print(Fore.GREEN + f"{node[0]}" + Fore.RESET + f" trabalhou com {path[index+1][0]} em {path[index+1][1]}.")
            continue
        elif index == len(path)-2:
            print(f"{node[0]} trabalhou com " + Fore.RED + f"{path[index+1][0]}" + Fore.RESET + f" em {path[index+1][1]}.")
            break
        print(f"{node[0]} trabalhou com {path[index+1][0]} em {path[index+1][1]}.")
    print("")

def main():
    graph = Graph('netflix_titles.csv')
    # graph.display()
    while True:
        name = input("Digite o nome do ator: ")
        path = graph.get_path_from_kevin(name)
        output_path(path=path)
        print("O que deseja agora?\na. Buscar outra conexão\nb. Sair\n")
        next_step = input("Selecione 'a' ou 'b': ").lower().strip()
        while next_step != 'a' and next_step != 'b':
            next_step = input("Selecione uma opção válida: ")
        if next_step == 'b':
            break
        
            

if __name__ == '__main__':
    main()