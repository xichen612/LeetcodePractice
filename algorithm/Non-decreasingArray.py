# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:22:21 2018

@author: chenxi11
"""

#665. Non-decreasing Array

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lows = 0
        point = 0
        for i in range(len(nums) - 1):
            if nums[i+1] < nums[i]:
                lows += 1
                point = i
                if lows >= 2:
                    return False
        newnums = nums[:point+1]
        
        if len(newnums) == 1 or (len(newnums)+1 == len(nums)):
            return True
        
        else:
            
            if newnums[-2] < nums[point+1]:
                return True
        
            for j in range(len(newnums)):
                if newnums[j] >=nums[point+2]:
                    return False
            
            return True
