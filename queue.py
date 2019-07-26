#!/usr/bin/python


class queue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.data = [None] * k
        self.capacity = k
	self.size = 0
        self.head = -1
        self.tail = -1

    def enQueue(self, value):

        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """

        if self.isFull():
            # We're at capacity
            return False

        if not self.isEmpty():
            # Shift tail
	    self.tail = (self.tail + 1) % self.capacity
        else:
	    self.tail = 0
	    self.head = self.tail

        self.size += 1
        self.data[self.tail] = value

        return True

    def deQueue(self):

        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """

        if self.isEmpty():
           return False

        self.size -= 1
        self.data[self.head] = None

	if self.size == 0:
	    self.head = -1
	    self.tail = -1
	else:
            self.head = (self.head + 1) % self.capacity

        return True

    def Front(self):

        """
        Get the front item from the queue.
        :rtype: int
        """

        if self.isEmpty():
            return -1
        else:
            return self.data[self.head]

    def Rear(self):

        """
        Get the last item from the queue.
        :rtype: int
        """

        if self.isEmpty():
            return -1
        else:
            return self.data[self.tail]

    def isEmpty(self):

        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):

        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """

        return self.size == self.capacity

#funcs = ["enQueue","deQueue","enQueue","enQueue","deQueue","isFull","isFull","Front","deQueue","enQueue","Front","enQueue","enQueue","Rear","Rear","deQueue","enQueue","enQueue","Rear","Rear","Front","Rear","Rear","deQueue","enQueue","Rear","deQueue","Rear","Rear","Front","Front","enQueue","enQueue","Front","enQueue","enQueue","enQueue","Front","isEmpty","enQueue","Rear","enQueue","Front","enQueue","enQueue","Front","enQueue","deQueue","deQueue","enQueue","deQueue","Front","enQueue","Rear","isEmpty","Front","enQueue","Front","deQueue","enQueue","enQueue","deQueue","deQueue","Front","Front","deQueue","isEmpty","enQueue","Rear","Front","enQueue","isEmpty","Front","Front","enQueue","enQueue","enQueue","Rear","Front","Front","enQueue","isEmpty","deQueue","enQueue","enQueue","Rear","deQueue","Rear","Front","enQueue","deQueue","Rear","Front","Rear","deQueue","Rear","Rear","enQueue","enQueue","Rear","enQueue"]
#vals = [[69],[],[92],[12],[],[],[],[],[],[28],[],[13],[45],[],[],[],[24],[27],[],[],[],[],[],[],[88],[],[],[],[],[],[],[53],[39],[],[28],[66],[17],[],[],[47],[],[87],[],[92],[94],[],[59],[],[],[99],[],[],[84],[],[],[],[52],[],[],[86],[30],[],[],[],[],[],[],[45],[],[],[83],[],[],[],[22],[77],[23],[],[],[],[14],[],[],[90],[57],[],[],[],[],[34],[],[],[],[],[],[],[],[49],[59],[],[71]]

#obj = MyCircularQueue(81)
#results = []
#for i in range(0, len(funcs)):
#    if funcs[i] == "enQueue":
#        results.append(obj.enQueue(vals[i]))
#        print str(obj.data) + " " + str(obj.head) + " " + str(obj.tail)
#    elif funcs[i] == "deQueue":
#        results.append(obj.deQueue())
#        print str(obj.data) + " " + str(obj.head) + " " + str(obj.tail)
#    elif funcs[i] == "isFull":
#        results.append(obj.isFull())
#    elif funcs[i] == "isEmpty":
#        results.append(obj.isEmpty())
#    elif funcs[i] == "Front":
#        results.append(obj.Front())
#    elif funcs[i] == "Rear":
#        results.append(obj.Rear())
#
#print results
