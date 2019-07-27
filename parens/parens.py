#!/usr/bin/python

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
     
        parens = []

	s = list(s)

        error = False
	for c in s:
	    if c in ['(', '{', '[']:
	        parens.append(c)
	    if c in [')', '}', ']'] and len(parens) > 0:
	        if parens[-1] == '(' and c == ')':
		    del parens[-1]
	        elif parens[-1] == '{' and c == '}':
		    del parens[-1]
	        elif parens[-1] == '[' and c == ']':
		    del parens[-1]
		else:
		    error = True
	    elif c in [')', '}', ']'] and len(parens) == 0:
	        error = True

        if len(parens) == 0 and not error:
	    return True
	else:
	    return False

sol = Solution()
print sol.isValid("]")
