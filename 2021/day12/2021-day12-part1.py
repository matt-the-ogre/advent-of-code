# Advent of Code - 2021 - Day 12

# https://adventofcode.com/2021/day/12

# References

# https://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python

# note: requires NetworkX: "pip3 install networkx"
import time, math, logging, os
import networkx as nx


from collections import defaultdict


# class Graph(object):
#     """ Graph data structure, undirected by default. """

#     def __init__(self, connections = [], directed=False):
#         self._graph = defaultdict(set)
#         self._directed = directed
#         self.add_connections(connections)

#     def add_connections(self, connections):
#         """ Add connections (list of tuple pairs) to graph """

#         for node1, node2 in connections:
#             self.add(node1, node2)

#     def add(self, node1, node2):
#         """ Add connection between node1 and node2 """

#         self._graph[node1].add(node2)
#         if not self._directed:
#             self._graph[node2].add(node1)

#     def remove(self, node):
#         """ Remove all references to node """

#         for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
#             try:
#                 cxns.remove(node)
#             except KeyError:
#                 pass
#         try:
#             del self._graph[node]
#         except KeyError:
#             pass

#     def is_connected(self, node1, node2):
#         """ Is node1 directly connected to node2 """

#         return node1 in self._graph and node2 in self._graph[node1]

#     def find_path(self, node1, node2, path=[]):
#         """ Find any path between node1 and node2 (may not be shortest) """

#         path = path + [node1]
#         if node1 == node2:
#             return path
#         if node1 not in self._graph:
#             return None
#         for node in self._graph[node1]:
#             if node not in path:
#                 new_path = self.find_path(node, node2, path)
#                 if new_path:
#                     return new_path
#         return None

#     def __str__(self):
#         return(f"{self._graph}")

def readInput(inputTextFileName):
    # global inputList
    global g
    g = nx.Graph()

    with open(inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    inputList = [listItem.rstrip() for listItem in inputList]
    
    for line in inputList:
        node1, node2 = line.split('-')
        # logging.debug(f"{node1 =} \t {node2 = }")
        if node1[0].isupper():
            node1Size = "big"
        else:
            node1Size = "small"
        if node2[0].isupper():
            node2Size = "big"
        else:
            node2Size = "small"
        # if node1[0].isupper():
        #     g.add_node((node1, {"size": "big"}))
        # else:
        #     g.add_node((node1, {"size": "small"}))
        # if node2[0].isupper():
        #     g.add_node((node2, {"size": "big"}))
        # else:
        #     g.add_node((node2, {"size": "small"}))
        nodesList = [(node1, {"size": node1Size}), (node2, {"size": node2Size})]
        g.add_nodes_from(nodesList)
        g.add_edge(node1, node2)
        if node1Size == 'big':
            g.add_edge(node1, node1)
        if node2Size == 'big':
            g.add_edge(node2, node2)
    
    logging.debug(f"{g}")
    return(g)

def processInput(inputList):

    global g

    # don't forget to reference global variables here if needed
    # ---
    
    # for listItem in inputList:
    #     logging.debug(f"listItem: {listItem}")
    #     pass
    # sp = dict(nx.all_pairs_shortest_path(g))
    allSimplePaths = nx.all_simple_paths(g, 'start', 'end')
    logging.debug(f"{list(allSimplePaths) = }")

    # for path in nx.all_simple_paths(g, source='start' target='end'):
    #     print(path)
    for path in nx.all_simple_paths(g, 'start', 'end'):
        logging.debug(f"{path = }")
        for pathNode in path:
            nodeAttributes = nx.get_node_attributes(g, "size")[pathNode]
            # logging.debug(f"{pathNode = }\t{nodeAttributes =}")
            if nodeAttributes == 'big':
                myNeighbors = nx.neighbors(g, pathNode)
                myNeighborsList = list(nx.neighbors(g, pathNode))
                logging.debug(f"{pathNode = }\t{myNeighborsList = }")
                for nodeItem in (myNeighbors):
                    if nodeItem != 'start' and nodeItem != 'end':
                        logging.debug(f"{nodeItem = }")
                        newSimplePaths = nx.all_simple_paths(g, pathNode, nodeItem)
                        logging.debug(f"{list(newSimplePaths) =}")


    # for path in nx.all_simple_paths(g, 'start', 'end'):
    #     # print(path)
    #     logging.debug(f"{path = }")
    #     # logging.debug(f"{zip(path, path[1:])}")
    #     for index, tupleItem in enumerate(zip(path, path[1:])):
    #         node1 = tupleItem[0]
    #         node2 = tupleItem[1]
    #         logging.debug(f"{index = }\t{tupleItem = }")
    #         if node1 != 'start' and node1 != 'end' and node2 != 'start' and node2 != 'end':
    #             for sub_path in nx.all_simple_paths(g, node1, node2):
    #                 logging.debug(f"{sub_path =}")

        # for n, X, Y in enumerate(zip(path, path[1:])):
            # logging.debug(f"{n = }\t{X = }\t{Y = }")
    return()

def main():
    startTime = time.perf_counter() # time in seconds (float)

    level = logging.DEBUG
    # level = logging.INFO
    # level = logging.ERROR
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    # get the filepath to load the input files
    filepath = os.path.dirname(__file__)

    timing = True
    unitTesting = True
    unitTest = '1'
    inputList = []

    # day-specific variables go here
    global g
    # g = Graph([])
    # ---
    
    if unitTesting:
        logging.info("Unit Testing")
        readInput(f"{filepath}/unit-test-input{unitTest}.txt")
    else:
        # read the input text file into a variable
        readInput(f"{filepath}/input.txt")

    numberOfPaths = processInput(g)

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        if unitTest == '1':
            testPass = (numberOfPaths == 10)
        elif unitTest == '2':
            testPass = (numberOfPaths == 19)
        elif unitTest == '3':
            testPass == (numberOfPaths ==  226)
        else:
            logging.error(f"error: invalid {testPass = }")

        print("testPass:", testPass)
    else:
        # print the answer here
        logging.debug("Don't forget to update your print statement of the output here.")
        print(math.nan)

    # this answer for my input is 

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
