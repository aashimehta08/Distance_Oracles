class Vertex:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacentList = []
        
    def get_vertex_id(self):
        return self.vertex_id
    def get_adjacent(self):
        return self.adjacentList
    def set_adjacent(self, new_adjacent):
        self.adjacentList = new_adjacent
            
class Dart : 
    def __init__(self, head, tail):
        self.weight = 1
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

# class Graph:
#     def __init__(self):

if __name__ == '__main__':
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    
    dart_ab = Dart(a,b)
    dart_ba = Dart(b,a)
    dart_ab.set_sibling(dart_ba)
    dart_ba.set_sibling(dart_ab)

    dart_ae = Dart(a,e)
    dart_ea = Dart(e,a)
    dart_ae.set_sibling(dart_ae)
    dart_ea.set_sibling(dart_ea)
    
    dart_ad = Dart(a,d)
    dart_da= Dart(d,a)
    dart_ad.set_sibling(dart_da)
    dart_da.set_sibling(dart_ad)

    dart_ec = Dart(e,c)
    dart_ce = Dart(c,e)
    dart_ec.set_sibling(dart_ce)
    dart_ce.set_sibling(dart_ec)

    dart_cd = Dart(c,d)
    dart_dc = Dart(d,c)
    dart_cd.set_sibling(dart_dc)
    dart_dc.set_sibling(dart_cd)
    
    dart_ed = Dart(e,d)
    dart_de = Dart(d,e)
    dart_ed.set_sibling(dart_de)
    dart_de.set_sibling(dart_ed)
    
    dart_bc = Dart(b,c)
    dart_cb = Dart(c,b)
    dart_bc.set_sibling(dart_cb)
    dart_cb.set_sibling(dart_bc)

    dart_bd = Dart(e,d)
    dart_db = Dart(d,e)
    dart_bd.set_sibling(dart_db)
    dart_db.set_sibling(dart_bd)

    a.set_adjacent([dart_ab, dart_ad, dart_ae])
    b.set_adjacent([dart_bc, dart_bd, dart_ba])
    c.set_adjacent([dart_ce, dart_cd, dart_cb])
    d.set_adjacent([dart_de, dart_da, dart_db, dart_dc])
    e.set_adjacent([dart_ea, dart_ed, dart_ec])

    graph = [a,b,c,d,e]