from collections import defaultdict
from gettext import find

  

class Node:
    def __init__(self, node):
        self.id = node
        self.adjacent = []
        
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
    def get_connections(self):
        return self.adjacent.keys()
    
    def add_addjecnt(self, jecnt):
        if jecnt not in self.adjacent:
            self.adjacent.append(jecnt)
    
    def get_id(self):
        return self.id

       
class Dart : 
    def __init__(self, tail, head, weight ):
        self.weight = weight
        self.head = head
        self.tail = tail
        self.sibling = None
        
    def get_sibling(self):
        return self.sibling
    def set_sibling(self, value):
        self.sibling = value
    def get_head(self):
        return self.head
    def set_head(self, value):
        self.head = value
    def get_tail(self):
        return self.tail
    def print_twin(self):
        print (str(self.tail.get_id()) + '<-->' + str(self.head.get_id()))
    def __str__(self):
        print (str(self.tail.get_id()) + '-->' + str(self.head.get_id()))

class Graph:
    def __init__(self):
        self.graph = defaultdict()
        self.num_dart = 0
        self.dartList = []
    
    def add_dart(self, frm, to, directed = True, weight = 1):
        if frm not in self.graph:
            self.graph[frm] = []
        if to not in self.graph:
            self.graph[to] = []
        
        dart1 = Dart(frm, to, weight)
        dart2 = Dart(to, frm, weight)
        dart1.get_tail().add_addjecnt(to)
        dart1.set_sibling(dart2)
        
        self.graph[frm].append(dart1)
        self.dartList.append(dart1);

        
    def print_graph(self):
        for f in self.graph:
            print(f.__str__())
    
    def order(self):
        return len(self.graph)
    
    def size(self):
        return int(self.num_dart/2)
            
    def print_twin(self):
        temp = {}
        for f in self.graph:
            for k in self.graph[f]:
                if k not in temp:
                    cur = k
                    sibling = cur.get_sibling()
                    
                    cur.print_twin()
                    
                    temp[cur] = sibling
                    temp[sibling] = cur
    
    def check_planarity(self):
        if self.order() > 2 and self.size() > 3 * self.order() - 6:
            return False
        
        return True
    
    def print_adj(self, node, clockwise=False):
        if node not in self.graph:
            return None
        else:
            a = self.graph[node][::-1] if clockwise else self.graph[node]
            for dart in a:
                dart.__str__()
    
    def planar(self):
        if self.check_planarity():
            return None
    def find_dart(self,dart):
        tail = dart.get_tail()
        id = dart.get_head().get_id()
        for i in range(len(self.graph[tail])):
            if(self.graph[tail][i].get_head().get_id() == id):
                return i
       
    def print_faces(self):
        visted = defaultdict()
        for node in self.graph:
            for dart in self.graph[node]:
                visted[dart] = False
        
        for curDart in graph.dartList:
            face = []
            while(not visted[curDart]):
                visted[curDart] = True
                sib = curDart.get_sibling()
                sibTail = sib.get_tail()
                face.append(sibTail.get_id())
                curIndex = self.find_dart(sib)
                nextNode = self.graph[sibTail][(curIndex + 1) if curIndex + 1 != len(self.graph[sibTail]) else 0].get_head()
                curDart = self.graph[sibTail][self.find_dart(Dart(sibTail, nextNode, 1))]
                
            if(len(face) != 0):
                print(face)
                    

    
        


if __name__ == '__main__':
    
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    
    graph = Graph()
    graph.add_dart(a,d)
    graph.add_dart(a,b)
    graph.add_dart(a,c)
    graph.add_dart(b,c)
    graph.add_dart(b,a)
    graph.add_dart(b,d)
    graph.add_dart(b,e)
    graph.add_dart(c,e)
    graph.add_dart(c,a)
    graph.add_dart(c,b)
    graph.add_dart(d,e)
    graph.add_dart(d,b)
    graph.add_dart(d,a)
    graph.add_dart(e,c)
    graph.add_dart(e,b)
    graph.add_dart(e,d)
    
    # graph.print_graph()
    # graph.print_adj(a)
    # print(graph.check_planarity())
    # graph.print_twin()
    graph.print_faces()


    
