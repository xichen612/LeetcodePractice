# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:22:21 2018

@author: chenxi11
"""

#771. Jwewls and Stones

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        freqCount = {}
        for i in range(len(S)):
            if S[i] in freqCount.keys():
                freqCount[S[i]] += 1
            else:
                freqCount[S[i]] = 1
        
        totals = 0
        for j in range(len(J)):
            if J[j] in freqCount.keys():
                totals += freqCount[J[j]]
                
        return totals