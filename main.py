from graph import Graph

def main():
    graph = Graph('netflix_titles.csv')
    # graph.display()
    name = 'Samuel L. Jackson'
    print(graph.get_path_from_kevin(name))

if __name__ == '__main__':
    main()