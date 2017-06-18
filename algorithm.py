class Optimizing(object):
    
    def __init__(self, graph_dict=None):

        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict


  

    # def find_path(self, cityA, cityB, path=[]):
    #     """ find a path from cityA to cityB
    #         in graph """
    #     graph = self.__graph_dict
    #     path = path + [cityA]
    #     if cityA == cityB:
    #         return path
    #     if cityA not in graph:
    #         return None
    #     for i in graph[cityA]:
    #         if i not in path:
    #             extended_path = self.find_path(i,
    #                                            cityB,
    #                                            path)
    #             if extended_path:
    #                 return extended_path
    #     return None

    def find_all_paths(self, cityA, cityB, path=[]):
        """ find all paths from cityA to 
            cityB in graph """
        graph = self.__graph_dict
        self.bestpaths=[]
        path = path + [cityA]
        if cityA == cityB:
            return [path]
        if cityA not in graph:
            return []
        paths = []
        for i in graph[cityA]:
            if i not in path:
                extended_paths = self.find_all_paths(i,cityB,path)
                for p in extended_paths:
                    paths.append(p)

        # print min(paths, key=len)
        # paths=self.bestpaths
        return paths

    def choose_path(self):
        print min(self.bestpaths, key=len)


g = {"Gniezno": ["Konin", "Poznan"],
     "Konin": ["Poznan", "Wroclaw", "Gniezno"],
     "Poznan": ["Gniezno", "Legnica", "Konin"],
     "Legnica": ["Poznan", "Wroclaw", "Jelenia"],
     "Jelenia": ["Legnica", "Walbrzych", ],
     "Walbrzych": ["Jelenia", "Wroclaw"],
     "Wroclaw": ["Legnica", "Konin", "Walbrzych"]
     }

find_connection = Optimizing(g)
print(find_connection)

# print("""A path from "P" to "J":""")
# print(graph.find_path("P", "J"))

print("""Path from "" to "":""")
a=find_connection.find_all_paths("Gniezno", "Walbrzych")
a=min(a, key=len)
print (a[1:])


# graph.choose_path()