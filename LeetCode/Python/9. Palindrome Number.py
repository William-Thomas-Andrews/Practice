class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        txt = string[::-1]

        if txt == string:
            return True

        else:
            return False
