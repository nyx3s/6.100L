class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []
        self.size = 0

    def Size(self):
        """
        Returns the length of the container list
        """
        # Your code here
        return self.size

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        # Your code here
        self.myList.append(elem)
        self.size += 1
    
    def __str__(self):
        return str(self.myList)

class Stack(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the container list is removed
        Returns the element removed or None if the queue contains no elements
        """
        # Your code here
        val = self.myList.pop()
        self.size -= 1
        return val


s = Stack()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(f"size = {s.Size()}")
print(s.remove())
print(s.remove())
print(s.remove())
s.add(11)
print(f"size = {s.Size()}")
print(s.remove())
