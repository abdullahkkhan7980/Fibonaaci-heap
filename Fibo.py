#!/usr/bin/env python
# coding: utf-8

# In[11]:


import math

# Creating fibonacci tree
class Fibo:
    def __init__(self, value):
        self.value = value
        self.child = []
        self.order = 0

    # Adding tree at the end of the tree
    def add_at_end(self, c):
        self.child.append(c)
        self.order = self.order + 1


# Creating Fibonacci heap
class Heap:
    def __init__(self):
        self.trees = []
        self.low = None
        self.count = 0

    # Insert a node
    def insert_node(self, value):
        new_tree = Fibo(value)
        self.trees.append(new_tree)
        if (self.low is None or value < self.low.value):
            self.low = new_tree
        self.count = self.count + 1

    # Get minimum value
    def get_min(self):
        if self.low is None:
            return None
        return self.low.value

    # Extract the minimum value
    def extract_min(self):
        smallest = self.low
        if smallest is not None:
            for child in smallest.child:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.low = None
            else:
                self.low = self.trees[0]
                self.work()
            self.count = self.count - 1
            return smallest.value

    # Consolidate the tree
    def work(self):
        a = (Do(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while a[order] is not None:
                y = a[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                a[order] = None
                order = order + 1
            a[order] = x

        self.least = None
        for k in a:
            if k is not None:
                self.trees.append(k)
                if (self.least is None
                        or k.value < self.low.value):
                    self.low = k

    def print(self):
        
        self.trees.append(new_tree)
        if (self.low is None or value < self.low.value):
            self.low = new_tree
        self.count = self.count + 1

        return insert_node

def Do(x):
    return math.frexp(x)[1] - 1


fibonacci_heap = Heap()
fibonacci_heap.insert_node(7)
fibonacci_heap.insert_node(4)
fibonacci_heap.insert_node(17)
fibonacci_heap.insert_node(24)

print('Min Value: {}'.format(fibonacci_heap.get_min()))

print('Removed Min Value: {}'.format(fibonacci_heap.extract_min()))

print(fibonacci_heap.insert_node)
