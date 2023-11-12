from reader import Reader

class Graph:
    def __init__(self, csv_name):
        self.df = Reader(csv_name).drop_na().important_columns(['title', 'cast']).df
        self.graph = {}
        for _, row in self.df.iterrows():
            actors = row['cast'].split(', ')
            for actor in actors:
                if actor not in self.graph:
                    self.graph[actor] = set()
                for other_actor in actors:
                    if other_actor != actor and other_actor not in [tuple[0] for tuple in self.graph[actor]]:
                        self.graph[actor].add((other_actor, row['title']))
                    
    def display(self):
        for actor in self.graph:
            print(actor, self.graph[actor])
        
    def get_path(self, actor_a, actor_b):
        try:
            visited = []
            queue = [[(actor_a, '_')]]
            while queue:
                path = queue.pop(0)
                node = path[-1]
                if node not in visited:
                    neighbours = self.graph[node[0]]
                    for neighbour in neighbours:
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)
                        if neighbour[0] == actor_b:
                            return new_path
                    visited.append(node)
            return []
        except Exception:
            return -1
    
    def get_path_from_kevin(self, actor):
        return self.get_path(actor, 'Kevin Bacon')