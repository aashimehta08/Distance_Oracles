from queue import PriorityQueue
from heapq import *
import random
import time
# class PriorityQueue(object):
#     def __init__(self, num):
#         self.heap = [None] * (num + 1)
#         self.numEle = 0
 
#     # for checking if the queue is empty
#     def compareElements(self, val1, val2):
#         if(val1[0] > val2[1]):
#             return -1
#         elif(val1[0] < val2[1]):
#             return 1
#         else:
#             return 0
    
#     def isEmpty(self):
#         return self.numEle == 0
 
#     def getLeftChildOf(self, parentIndex):
#         return 2*parentIndex ;
    

#     def getRightChildOf(self, parentIndex):
#         return 2*parentIndex + 1;
    

#     def getParentOf(self, childIndex):
#         return childIndex//2;
    
#     def swapIndices(self, index1, index2):
#         temp = self.heap[index1]
#         self.heap[index1] = self.heap[index2]
#         self.heap[index2] = temp
 
#     # for popping an element based on Priority
#     def bubbleUp(self, index):
#         while(index > 1 and self.compareElements(self.heap[self.getParentOf(index)], self.heap[index]) < 0):
#             self.swapIndices(self.getParentOf(index), index)
#             index = self.getParentOf(index)
    
#     def bubbleDown(self, index):
        
#         value = self.heap[index]
#         while(self.getLeftChildOf(index) < self.numEle ):
#             maxIndex = -1
#             maxValue = value

#             if(self.getLeftChildOf(index) < self.numEle and self.compareElements(self.heap[getLeftChildOf(index)], maxValue) > 0):
#                 maxValue = self.heap[getLeftChildOf(index)];
#                 maxIndex = self.getLeftChildOf(index);

#             if(self.getRightChildOf(index) < self.numEle and self.compareElements(self.heap[getRightChildOf(index)], maxValue) > 0):
#                 maxValue = self.heap[getRightChildOf(index)];
#                 maxIndex = self.getRightChildOf(index);

#             if(self.compareElements(maxValue, value) == 0):
#                 return
            
#             else:
#                 self.swapIndices(index, maxIndex);
#                 index = maxIndex;
            
      
#     def get(self):
#         data = self.heap[1];

#         self.swapIndices(1, self.numEle);
#         self.heap[self.numEle] = None;

#         self.bubbleDown(1);

#         self.numEle -= 1;

#         return data;

#     def put(self,value):
        
#         self.heap[self.numEle+1] = value;
#         self.numEle += 1;

#         self.bubbleUp(self.numEle);

class Node:
    def __init__(self, id, distance = 1):
        self.id = id
        self.distance = distance
        
    def get_distance(self):
        return self.distance
    
    def get_id(self):
        return self.id

class VistedTuple:
    def __init__(self, node):
        self.node = node
        self.visted = False

class Graph:
    def __init__(self, FILENAME):
        self.FILENAME = FILENAME
        self.numNode, self.graph,self.numEdge = self.load_graphs()
        # self.faces = self.count_faces()
                
        
    def load_graphs(self):
        inFile = open(self.FILENAME, 'r').readlines()
        numEdge = int(len(inFile)/2)
        numNode = -1
        for line in inFile:
            line = line.split()
            temp = int(line[2]) if int(line[2]) > int(line[1]) else int(line[1])
            numNode = temp if temp > numNode else numNode
        
        numNode += 1
        graph = [None] * numNode
        
        for line in inFile:
            if(len(line) > 1):
                line = line.split()
                start = int(line[1])
                end = int(line[2])
                distance = float(line[3])
                
                try:
                    graph[start].append(Node(end,distance))
                except:
                    graph[start] = [Node(end,distance)]
                    
                try:
                    graph[end].append(Node(start,distance))
                except:
                    graph[end] = [Node(start,distance)]
                
                
        return (numNode,graph, numEdge)

    def visted_list(self):
        visted = []
        for adjecents in self.graph:
            visted.append([VistedTuple(node) for node in adjecents])
        
        return visted
    
    # def generate_distance(self):
    #     distanceList = open(self.DITANCE_LIST,'r')
        
    #     for line in distanceList.readlines():
    #         if(len(line) > 1):
    #             line = line.split();
    #             line[1] = int(line[1])
    #             line[2] = int(line[2])
    #             line[3] = float(line[3])
                
    #             startIndex = self.indexOf(line[1],line[2])
    #             endIndex = self.indexOf(line[2],line[1])
                
    #             self.graph[line[1]][startIndex][1] = line[3]
    #             self.graph[line[2]][endIndex][1] = line[3]
        

    def count_faces(self):
        visted = self.visted_list()
        numFace = 0
        
        for node in range(len(self.graph)):
            for adjecent in range(len(self.graph[node])):
                existFace = False
                while not visted[node][adjecent][1]:
                    existFace = True
                    visted[node][adjecent][1] = True
                    curHead = self.graph[node][adjecent][0]
                    curIndex = self.indexOf(curHead, node)
                    
                    nextHead = self.graph[curHead][curIndex + 1][0] if curIndex + 1 != len(self.graph[curHead]) else self.graph[curHead][0][0]
                    node = curHead
                    adjecent = self.indexOf(node, nextHead)
    
                if existFace: numFace += 1
            
        
        return numFace

    # #Return position of endNode
    # def indexOf(self, startNode, endNode):
    #     index = 0
        
    #     for curNode in self.graph[startNode]:
    #         if(curNode[0] == endNode):
    #             return index
    #         else:
    #             index += 1
    
    def dijstrak(self, node):
        pq = PriorityQueue()
        distanceList = [float('inf')] * self.numNode
        distanceList[node] = 0
        
        pq.put((0, node))
        vistedList = [False] * self.numNode
        
        while not pq.empty():
            curNode = pq.get()[1]
            if(vistedList[curNode]):
                continue
            vistedList[curNode] = True
            
            for neighbor in self.graph[curNode]:
                curDistance = neighbor.get_distance()
                # if(not vistedList[neighbor.get_id()]):
                    # oldDistance = distanceList[neighbor.get_id()]
                    # newDistance = distanceList[curNode] + curDistance 
                if(not vistedList[neighbor.get_id()] and distanceList[curNode] + curDistance < distanceList[neighbor.get_id()] ):
                    distanceList[neighbor.get_id()] = distanceList[curNode] + curDistance
                    pq.put((distanceList[neighbor.get_id()],neighbor.get_id()))
                        
        return distanceList
        

if __name__ == '__main__':
    FILENAME = 'Cali2.txt'
    graph = Graph(FILENAME)
    
    test_data = random.sample(range(graph.numNode), 1)
    avg_time = 0
    
    
    for data in test_data:
        start_time = time.time()
        ans = graph.dijstrak(data)
        avg_time += time.time() - start_time
    

    print('Average process finished with --- %s seconds ---' % (avg_time/1))
    print('Total number of node:%s' %graph.numNode)
    print('Total number of edges:%s' % graph.numEdge)
    
    

    