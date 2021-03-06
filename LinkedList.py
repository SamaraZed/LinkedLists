class Node:
  data = None
  next_node = None
  
  def __init__(self, data):
    self.data = data
    
  def __repr__(self):
    return "<Node data: %s>" % self.data
    
class LinkedList:
  
  def __init__(self):
    self.head = None

  def __repr__(self):
    nodes = []
    current = self.head
    
    while current:
      if current is self.head:
        nodes.append("[Head: %s]" % current.data)
      elif current.next_node is None:
        nodes.append("[Tail: %s]" % current.data)
      else:
        nodes.append("[%s]" % current.data)
      
      current = current.next_node
    return '-> '.join(nodes)
    
  def is_empty(self):
    return self.head == None
  
  def size(self):
    
    current = self.head
    count = 0
    
    while current:
      count += 1
      current = current.next_node
      
    return count

  def add(self, data):
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node
    
  def remove(self,key):
    current = self.head
    previous = None
    found = False

    while current and not found:
      if current.data == key and current is self.head:
        found = True
        self.head = current.next_node
      elif current.data == key:
        found = True
        previous.next_node = current.next_node
      else:
        previous = current
        current = current.next_node

    def search(self, key):
      
      current = self.head
      
      while current:
        if current.data == key:
          return current
        else:
          current = current.next_node
      return None

a = LinkedList()

a.add('abc')
a.add('abc1')
a.add('abc2')
a.add('abc3')
a.add('abc4')
print(a)
a.remove('abc2')
print(a)
