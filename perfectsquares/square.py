#!/usr/bin/python

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
	i=0
	s=[i]
        while sum(s) < n:
	    s.pop(0)
	    ss = 0
	    while sum(ss) <= n:
	        ss += i
	    if sum(ss) == n:
	       break
	    i += 1
	    s.append(i**2)

        return len(s)
         
