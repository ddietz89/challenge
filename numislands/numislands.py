#!/usr/bin/python

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
	# Create checked grid
	if grid == []:
	    return 0
	self.xSize = len(grid)
	self.ySize = len(grid[0])
	self.checked = [] * self.xSize
	self.checked = [[False for i in range(self.ySize)] for j in range(self.xSize)]
	self.grid = grid

	islands = 0

        # init queue

        for i in range(0, self.xSize, 1):
            for j in range(0, self.ySize, 1):
	        if not self.checked[i][j] and self.isIsland(i,j):
		    queue = []
	            queue.append([i,j])
	            while not len(queue) == 0:
	               self.checkNodes(queue)
        
	            islands += 1

	return islands

    def isIsland(self, x, y):
	return self.grid[x][y] == "1"

    def checkNodes(self, queue):
        x, y = queue.pop(0)

        if self.checked[x][y]:
	    return queue
        if not self.isIsland(x, y):
	    return queue

	self.checked[x][y] = True

        # This is land, go check neighbors
        # Look at surrounding nodes
	if x-1 >= 0 and self.isIsland(x-1,y):
           queue.append([x-1,y])
	if x+1 < self.xSize and self.isIsland(x+1,y):
           queue.append([x+1,y])
	if y-1 >= 0 and self.isIsland(x,y-1):
           queue.append([x,y-1])
	if y+1 < self.ySize and self.isIsland(x,y+1):
           queue.append([x,y+1])

	return queue

	
	
sol = Solution()
