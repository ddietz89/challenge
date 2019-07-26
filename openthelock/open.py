#!/usr/bin/python

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        
	#self.target = [int(c) for c in target]
	#self.deadends = []
	#for i in range(len(deadends)):
	#    self.deadends.append([int(c) for c in deadends[i]])
	self.target = target
	self.deadends = deadends

	turns = []
	if "0000" not in deadends:
            turns.append("0000")
            self.deadends.append("0000")
	num_turns = 0
	while turns:

            for i in range(len(turns)):
	        turn = turns.pop(0)
	        if turn == self.target:
		    return num_turns

		new_turns = self.next_turns(turn)
                for turn in new_turns:
	            if not turn in self.deadends:
		        self.deadends.append(turn)
			turns.append(turn)
	    num_turns += 1


	return -1

    def next_turns(self, start):

        turns = []
	# possible moves
	for i in range(4):
            for j in {-1,1}:
	        turns.append( start[:i] + str((int(start[i])+j) % 10) + start[i+1:] )
	return turns
	   
sol = Solution()
print sol.openLock(["1131","1303","3113","0132","1301","1303","2200","0232","0020","2223"], "3312")
