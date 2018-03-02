# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:22:21 2018

@author: chenxi11
"""

#791. Custom Sort String

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        tdict = {}
        for i in range(len(T)):
            if T[i] in tdict.keys():
                tdict[T[i]] += 1
            else:
                tdict[T[i]] = 1
                
        sdict = {}        
        for j in range(len(S)):
            if S[j] in tdict.keys():
                sdict[S[j]] = tdict[S[j]]
                tdict[S[j]] = 0
                    
            else:
                print("invalid")
        leftstring = ""
        for k, v in tdict.items():
            if v >= 1:
                for t in range(v):
                    leftstring = leftstring + k
                    
        newS = ''
        for q in range(len(S)):
            for p in range(sdict[S[q]]):
                newS = newS + S[q]
        
        
        return newS + leftstring