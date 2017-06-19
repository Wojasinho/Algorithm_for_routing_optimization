class Optimizing(object):
    """Object from these class can find shortest (fastest way) between Cities. It can be usefull for optimizing network 
    routing. For defined topology, we can find best connection ex. City A -> City B. It's a script for extra exercise
    for Student Project 'Desing and Implement Network for company with 6 department and within 1  Central Department
    
    """

    def __init__(self, graph_dict=None):

        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict



    def find_all_paths(self, cityA, cityB, path=[]):

        """ Find all paths from cityA to cityB in defined topology """

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


        self.bestpaths=paths
        return self.bestpaths



    def choose_path(self):
        """Choose shortest path from all paths."""
        self.fastestpath= min(self.bestpaths, key=len)
        print (self.fastestpath)

    def count_delay(self):
        """Count delay, it depends how many cities are between our start and destination city """

        total_delay=0
        generated_network_traffic=0
        channel_bandwidth=196000

        # Generated traffic from Central Department in MB (ex. From Jelenia Gora -> Gniezno)
        if self.fastestpath[0]=='Jelenia':
            generated_network_traffic = 200

        # Generated traffic to Central Department in MB (ex. From Bydgoszcz -> Jelenia Gora)
        if self.fastestpath[-1] == 'Jelenia':
            generated_network_traffic = 250
        # Genereted traffic between two Department in MB (ex. From Wroclaw -> Legnica)
        if not (self.fastestpath[0]=='Jelenia' or self.fastestpath[-1] == 'Jelenia'):
            generated_network_traffic=40



        total_traffic = generated_network_traffic * (len(self.fastestpath)-1)
        flow = (total_traffic * 1000000*8/(9*3600))
        total_packets = flow / 1024
        coefficient_delay = (flow /(channel_bandwidth-flow))
        total_delay = ((1/total_packets)*coefficient_delay)

        # print ("Najkrótsze połączenie, opóźnienie na trasie wynosi : " + str(round(total_delay,5) ))
        print("Shortest/Fastest connection, delay is equal " + str(round(total_delay, 5)))


cities = {
     "Gniezno": ["Konin", "Poznan"],
     "Konin": ["Poznan", "Wroclaw", "Gniezno"],
     "Poznan": ["Gniezno", "Legnica", "Konin"],
     "Legnica": ["Poznan", "Wroclaw", "Jelenia"],
     "Jelenia": ["Legnica", "Walbrzych", ],
     "Walbrzych": ["Jelenia", "Wroclaw"],
     "Wroclaw": ["Legnica", "Konin", "Walbrzych"]
     }



# Defined here interested city
cityA="Wroclaw"
cityB="Poznan"

find_connection = Optimizing(cities)
find_connection.find_all_paths(cityA, cityB)
find_connection.choose_path()
find_connection.count_delay()
