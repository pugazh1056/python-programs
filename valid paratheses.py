class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        a={')':'(',']':'[','}':'{'}
        for i in s:
            if i in a:
                if stack and stack[-1]==a[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
        