from __future__ import (nested_scopes, generators, division, absolute_import, with_statement,
                        print_function, unicode_literals)

from copy import deepcopy
from color import *

class BTree(object):
  """A BTree implementation with search and insert functions. Capable of any order t."""

  class Node(object):
    """A simple B-Tree Node."""

    def __init__(self, t):
      self.keys = []
      self.children = []
      self.leaf = True
      # t is the order of the parent B-Tree. Nodes need this value to define max size and splitting.
      self._t = t

    def split(self, parent, payload):
      """Split a node and reassign keys/children."""
      new_node = self.__class__(self._t)

      mid_point = self.size//2
      split_value = self.keys[mid_point]
      parent.add_key(split_value)

      # Add keys and children to appropriate nodes
      new_node.children = self.children[mid_point + 1:]
      self.children = self.children[:mid_point + 1]
      new_node.keys = self.keys[mid_point+1:]
      self.keys = self.keys[:mid_point]

      # If the new_node has children, set it as internal node
      if len(new_node.children) > 0:
        new_node.leaf = False

      parent.children = parent.add_child(new_node)
      if payload < split_value:
        return self
      else:
        return new_node

    @property
    def _is_full(self):
      return self.size == 2 * self._t - 1

    @property
    def size(self):
      return len(self.keys)

    def add_key(self, value):
      """Add a key to a node. The node will have room for the key by definition."""
      self.keys.append(value)
      self.keys.sort()

    def add_child(self, new_node):
      """
      Add a child to a node. This will sort the node's children, allowing for children
      to be ordered even after middle nodes are split.
      returns: an order list of child nodes
      """
      i = len(self.children) - 1
      while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
        i -= 1
      return self.children[:i + 1]+ [new_node] + self.children[i + 1:]


  def __init__(self, t):
    """
    Create the B-tree. t is the order of the tree. Tree has no keys when created.
    This implementation allows duplicate key values, although that hasn't been checked
    strenuously.
    """
    self._t = t
    if self._t <= 1:
      raise ValueError("B-Tree must have a degree of 2 or more.")
    self.root = self.Node(t)

  def insert(self, payload):
    """Insert a new key of value payload into the B-Tree."""
    node = self.root
    # Root is handled explicitly since it requires creating 2 new nodes instead of the usual one.
    if node._is_full:
      new_root = self.Node(self._t)
      new_root.children.append(self.root)
      new_root.leaf = False
      # node is being set to the node containing the ranges we want for payload insertion.
      node = node.split(new_root, payload)
      self.root = new_root
    while not node.leaf:
      i = node.size - 1
      while i > 0 and payload < node.keys[i] :
        i -= 1
      if payload > node.keys[i]:
        i += 1

      next = node.children[i]
      if next._is_full:
        node = next.split(node, payload)
      else:
        node = next
    # Since we split all full nodes on the way down, we can simply insert the payload in the leaf.
    node.add_key(payload)

  def search(self, value, node=None):
    """Return True if the B-Tree contains a key that matches the value."""
    if node is None:
      node = self.root

    if node.keys:
      return True

    elif node.leaf:
      # If we are in a leaf, there is no more to check.
      return False

    else:
      i = 0
      while i < node.size:
        i += 1
      return self.search(value, node.children[i])

  
  def print_order(self):
    """Print an level-order representation."""
    this_level = [self.root]
    while this_level:
      next_level = []
      output = ""
      for node in this_level:
        if node.children:
          next_level.extend(node.children)
        output += str(node.keys) + " <--> "
      print(output.center(200, ' '))
      this_level = next_level
    
  # FUNCOES PARA O TRABALHO DE ED2
  def print_seq(self, x):
    """ Exibe todas as chaves da árvore """
    for i in x.keys:
      print(i)

    if x.children:
      for i in x.children:
        self.print_seq(i)
      
  def seach_by_interval(self, x, value0, value1):
    """ Busca por intervalos: [valor inicial, valor final] """
    if value0 >= value1:
      return False

    for i in range(len(x.keys)):
      if x.keys[i][0] >= value0 and x.keys[i][0] <= value1:
        print(x.keys[i])

    if x.children:
      for i in x.children:
        self.seach_by_interval(i, value0, value1)
  
  def seach_by_value(self, x, value, type_seach):
    """ Busca por maior ou menor que uma determinada chave """
    if type_seach == "maior":
      for i in range(len(x.keys)):
        if x.keys[i][0] > value:
          print(x.keys[i])
    elif type_seach == "menor":
      for i in range(len(x.keys)):
        if x.keys[i][0] < value:
          print(x.keys[i])

    if x.children:
      for i in x.children:
        self.seach_by_value(i, value, type_seach)

  def search_bt(self, x, value):
    """ Retorna true se a chave passada pra função está contida na árvore. Ps: função adaptada para 
    verificar apenas a parte após a vírgula (a chave em si) do registro. """
    for i in x.keys:
        if value in i:
	        return i[1]

    if x.children:
      for i in x.children:
        index = self.search_bt(i, value)
        if index != None:
            return index
  
  def seq_press(self, root_origin):
    root = deepcopy(root_origin)
    if root.children:
      for child in root.children:
        if child.keys[0][0] > root.keys[0][0]:
          print(root.keys[0])
          del root.keys[0]
        #print("filho",child.keys)
        self.seq_press(child)
    #Impressão de fato:
    for no in root.keys:
      print(no)


def main():  

    bt = BTree(2)
    l = range(20,0, -1)

    bt.insert(["AAAAA", 19])
    bt.insert(["AAAAB", 18])
    bt.insert(["AAABB", 1])
    bt.insert(["AABBB", 15])
    bt.insert(["ABBBB", 1544])
    bt.insert(["BBBBB", 145])
    bt.insert(["BBBBC", 195])
    bt.insert(["BBBCC", 5])
    bt.insert(["BBCCC", 159])
    bt.insert(["BCCCC", 99])
    bt.insert(["CCCCC", 75])
    bt.insert(["CCCCD", 7])
    bt.insert(["CCCDD", 10])
    bt.insert(["CCDDD", 11])
    bt.insert(["CDDDD", 200])
    bt.insert(["DDDDD", 21])
    bt.insert(["DDDDE", 37])
    bt.insert(["DDDEE", 12])
    bt.insert(["DEEEE", 147])
    
    #print(bt.search_bt(bt.root, "CCDDD"))
    #print(index_arqSeq)
    #bt.print_order()
    #print("\n\n")
    #bt.seq_press(bt.root)
    #bt.print_seq(bt.root)
    #bt.seach_by_interval(bt.root, "BBBCC", "DDDDE")
    #print("\n")
    #bt.seach_by_value(bt.root, "CDDDD", "maior")

if __name__ == '__main__':
	main()   