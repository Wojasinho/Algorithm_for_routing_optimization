class Optimizing(object):
    
    def __init__(self, graph_dict=None):

        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict



    def find_all_paths(self, cityA, cityB, path=[]):
        """ find all paths from cityA to 
            cityB in graph """
        self.cityA=cityA
        self.cityB=cityB

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
        self.bestpaths=paths
        return self.bestpaths
        # return paths


    def choose_path(self):
        self.fastestpath= min(self.bestpaths, key=len)
        print (self.fastestpath)

    def count_delay(self):

        total_delay=0
        generated_network_traffic=0
        channel_bandwidth=196000

        if self.fastestpath[0]=='Jelenia':
            generated_network_traffic = 200

        if self.fastestpath[-1] == 'Jelenia':
            generated_network_traffic = 250

        if not (self.fastestpath[0]=='Jelenia' or self.fastestpath[-1] == 'Jelenia'):
            generated_network_traffic=40



        total_traffic = generated_network_traffic * (len(self.fastestpath)-1)
        flow = (total_traffic * 1000000*8/(9*3600))
        total_packets = flow / 1024
        coefficient_delay = (flow /(channel_bandwidth-flow))
        total_delay = ((1/total_packets)*coefficient_delay)

        print ("Najkrótsze połączenie, opóźnienie na trasie wynosi" + str(round(total_delay,5)))








cities = {
     "Gniezno": ["Konin", "Poznan"],
     "Konin": ["Poznan", "Wroclaw", "Gniezno"],
     "Poznan": ["Gniezno", "Legnica", "Konin"],
     "Legnica": ["Poznan", "Wroclaw", "Jelenia"],
     "Jelenia": ["Legnica", "Walbrzych", ],
     "Walbrzych": ["Jelenia", "Wroclaw"],
     "Wroclaw": ["Legnica", "Konin", "Walbrzych"]
     }




cityA="Poznan"
cityB="Wroclaw"

find_connection = Optimizing(cities)
find_connection.find_all_paths(cityA, cityB)
find_connection.choose_path()
find_connection.count_delay()

# find_connection.choose_path()
# print("Path from " + cityA + " to " + cityB + " :" )
# a = min(bestpaths, key=len)
# print (a)

# print(find_connection)

# print("""A path from "P" to "J":""")
# print(graph.find_path("P", "J"))




# graph.choose_path()