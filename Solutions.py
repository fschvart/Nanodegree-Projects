# -*- coding: utf-8 -*-

import itertools

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)
        
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
        
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
        
def question1(s,t) :
    lent = len(t)
    lens = len(s)
    dic = {}
    for i in range(lent) :
        if t[i] not in s : 
            return False   # added for efficiency purposes
    for i in range(lens) :
        if s[i] in t :    
            dic[i]= t.index(s[i])
    for key,value in dic.items() :
        if key + lent - 1 in dic :
            temparr = []
            for i in range(lent) :
                if dic[key+i] in temparr :
                    break
                else:
                    temparr.append(dic[key+i])
            if len(temparr) == lent :
                return True
    return False

def question2(a) :
    leng  = len(a)
    pal_len = 1
    pal_loc = 0
    for i in range(leng) :
        for j in range(i,leng) :
            pal = palindrom(a[i:j+1])
            if pal > pal_len :
                pal_len = pal
                pal_loc = i
    return a[pal_loc:pal_loc+pal_len]
          
def palindrom(a) :
    c = len(a)
    counter = 1
    if c == 1 :
        return 1
    elif c % 2 == 0 :
        counter = 0
        t = int(c/2)
        for i in range(1,t+1) :
            if a[t-i] == a[t+i-1] :
                counter+=2
            else :
                return 0
        return counter
    else : 
        t = int(c/2)
        for i in range(1,t+1) :
            if a[t-i] == a[t+i] :
                counter+=2
            else : 
                return 0
        return counter

def question3(G)  :
    result ={} 
    parent = {}
    rank = {}
    G.edges = sorted(G.edges, key=lambda x: x.value) 

    for node in G.nodes:
            parent[node] = node
            rank[node] = 0
    for edge in G.edges :
        value = edge.value
        node_from = edge.node_from
        node_to = edge.node_to
        if G.find(parent,node_from) != G.find(parent,node_to) :
            G.union(parent,rank,node_from,node_to)
            if node_from.value in result :
                result[node_from.value].append((node_to.value,value))
            else :
                result[node_from.value] = [(node_to.value,value)]
            if node_to.value in result :
                result[node_to.value].append((node_from.value,value))
            else :
                result[node_to.value] = [(node_from.value,value)]
        
    return result

    





 
      
    
    
  

def question4(T, r, n1, n2) :
    small = min(n1,n2)
    large = max(n1,n2) 
    leng = len(T[0])
    if ( n1 > r and r > n2) or (n1 < r and n2 > r) or n1 == r or n2 == r:
        return r
    else :
        while True :
            for i in range(leng) :
                if T[i][small] == 1 :
                    if i > large :
                        return small
                    else :
                        small = i


def question5(ll,m) :
    count = 0
    current = ll.head   
    while current :
        count+=1
        current=current.next
    if count < m :
        return "error, m is larget than the linked list size"
    else :
        current = ll.head
        for i in range(count - m-1) :
            current=current.next
        
        return current.value
    

    
print (question1('ucdiaciity','ic'))
""" True"""
print (question1('udacity','ya'))
""" False"""
print (question1('udacity','ac'))
""" True"""

print(question2("helaalo"))
""" laal"""
print(question2("hello"))
"""ll"""
print(question2("helalo"))
"""lal"""



graph1 = Graph()
graph1.insert_edge(2, 'a', 'b')    
graph1.insert_edge(3, 'a', 'c')    
graph1.insert_edge(3, 'a', 'd')   
graph1.insert_edge(4, 'b', 'c')   
graph1.insert_edge(3, 'b', 'e') 
graph1.insert_edge(5, 'c', 'd') 
graph1.insert_edge(1, 'c', 'e') 
graph1.insert_edge(7, 'd', 'f')   
graph1.insert_edge(8, 'e', 'f') 
graph1.insert_edge(9, 'f', 'g')

print(question3(graph1))
# {'d': [('a', 3), ('f', 7)], 'e': [('c', 1)], 'g': [('f', 9)], 'f': [('d', 7), ('g', 9)], 'a': [('b', 2), ('c', 3), ('d', 3)], 'b': [('a', 2)], 'c': [('e', 1), ('a', 3)]}

graph2 = Graph([],[])
graph2.insert_edge(7, 'a', 'b')    
graph2.insert_edge(5, 'a', 'd')    
graph2.insert_edge(8, 'b', 'c')   
graph2.insert_edge(9, 'b', 'd')   
graph2.insert_edge(7, 'b', 'e') 
graph2.insert_edge(5, 'c', 'e') 
graph2.insert_edge(15, 'd', 'e') 
graph2.insert_edge(6, 'd', 'f')   
graph2.insert_edge(8, 'e', 'f') 
graph2.insert_edge(9, 'e', 'g')
graph2.insert_edge(11, 'f', 'g')

print(question3(graph2))
# {'a': [('d', 5), ('b', 7)], 'e': [('c', 5), ('b', 7), ('g', 9)], 'g': [('e', 9)], 'f': [('d', 6)], 'd': [('a', 5), ('f', 6)], 'b': [('a', 7), ('e', 7)], 'c': [('e', 5)]}

graph3 = Graph([],[])
graph3.insert_edge(6, 'a', 'b')    
graph3.insert_edge(3, 'a', 'c')    
graph3.insert_edge(7, 'a', 's')   
graph3.insert_edge(4, 'b', 'c')   
graph3.insert_edge(2, 'b', 'd') 
graph3.insert_edge(5, 'b', 't') 
graph3.insert_edge(3, 'c', 'd') 
graph3.insert_edge(8, 'c', 's')   
graph3.insert_edge(2, 'd', 't') 


print(question3(graph3))
# {'d': [('b', 2), ('t', 2), ('c', 3)], 's': [('a', 7)], 'a': [('c', 3), ('s', 7)], 'b': [('d', 2)], 't': [('d', 2)], 'c': [('a', 3), ('d', 3)]}




print (question4([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0]],
          4,
          1,
          3))
"""2"""
print (question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4))
"""3"""
print (question4([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0]],
          4,
          1,
          5))
"""4"""

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
print (question5(ll,3)) 
#1  
print (question5(ll,2))  
#2
print (question5(ll,7))      
#error, m is larget than the linked list size

 