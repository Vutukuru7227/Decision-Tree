#!/usr/bin/python

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

#class Node:
#    def __init__(self, val):
#        self.attribute = ""
#        self.leftNode = None
#        self.rightNode = None
#        self.label = ""
#        self.mostCommonLabel = ""

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val, decision):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root, decision)

    def _add(self, val, node, decision):
        if(decision == 0):
            if(node.l != None):
                self._add(val, node.l, decision)
            else:
                node.l = Node(val)
        else:
            if(decision == 1):
                self._add(val, node.r, decision)
            else:
                node.r = Node(val)

    #def find(self, val):
    #        return

    #def _find(self, val, node): 
    #        return

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)