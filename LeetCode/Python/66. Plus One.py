class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return([int(i) for i in str(int(''.join(str(x) for x in digits)) + 1)])
