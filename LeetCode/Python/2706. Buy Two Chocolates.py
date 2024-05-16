from itertools import combinations

class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        scores_to_minimize = [(x + y) for x, y in combinations(prices, 2)]
        final_scores_to_minimize = []
        for i in range(0, (len(scores_to_minimize))):
            if scores_to_minimize[i] <= money:
                final_scores_to_minimize.append(scores_to_minimize[i])        
        if sum(final_scores_to_minimize) == 0:
            return(money)
        else:
            return(money - min(final_scores_to_minimize))
