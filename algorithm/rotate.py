# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:22:21 2018

@author: chenxi11
"""

#189. Rotate Array

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        lens = len(nums)
        if lens == 1:
            move = 0
        else:
            move = k % lens


            spoint = lens - move - 1
            
            snums = nums[:spoint + 1]
            len1 = len(snums)
            rnums = nums[spoint + 1:]
            len2 = len(rnums)
            
            nums[-len1:] = snums
            nums[: len2] = rnums