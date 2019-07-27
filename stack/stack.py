#!/usr/bin/python

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = [] 
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        if len(self.data) > 0:
            m = self.getMin()
	else:
	    m = 9999999999
	if (x < m):
	    self.data.append((x, x))
	else:
	    self.data.append((x, m))
        
	return None

    def pop(self):
        """
        :rtype: None
        """
        
	self.data.pop(-1)

	return None

    def top(self):
        """
        :rtype: int
        """

        if len(self.data) > 0:
	   x, m = self.data[-1]
	   return x
	return None

        

    def getMin(self):
        """
        :rtype: int
        """
	x, m = self.data[-1]

        return m
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print obj.getMin()
obj.pop()
print obj.getMin()
