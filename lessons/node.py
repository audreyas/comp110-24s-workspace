from __future__ import annotations

class Node: 

    data: int
    next: Node | None 

    def __init(self, data: int, next: Node | None): 
        self.data = data 
        self.next = next

node_c: Node = Node(7, None)
node_b: Node = Node(6, node_c)
node_a; Node = Node(5, node_b) 