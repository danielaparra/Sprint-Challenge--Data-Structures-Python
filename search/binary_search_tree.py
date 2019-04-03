from queue import SimpleQueue

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
  # Helper function to traverse bst.
  def _depth_first_search(self, node, cb):
    # If node is None, it has no child on that side, so return.
    if not node:
      return
    # Otherwise...
    else:
      # Perform function on node value.
      cb(node.value)
      # Traverse the left and right children.
      self._depth_first_search(node.left, cb)
      self._depth_first_search(node.right, cb)

  def depth_first_for_each(self, cb):
    # Call recursive function on root of bst.
    self._depth_first_search(self, cb)

  def breadth_first_for_each(self, cb):
    # Create a queue.
    breadth_queue = SimpleQueue()
    # Add root to queue.
    breadth_queue.put(self)

    # Check that queue isn't empty.
    while not breadth_queue.empty():
      # Pop first node from queue.
      curr_node = breadth_queue.get()
      # Perform anonymous function on value of node.
      cb(curr_node.value)
      # Add any existing child nodes to queue from left to right.
      if curr_node.left:
        breadth_queue.put(curr_node.left)
      if curr_node.right:
        breadth_queue.put(curr_node.right)
      

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
