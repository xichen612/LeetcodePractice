# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:22:21 2018

@author: chenxi11
"""

#7. Reverse Integer

#class Solution:
#    def reverse(self, x):
#        """
#        :type x: int
#        :rtype: int
#        """
#        strx = str(x)
#        restrx = ""
#        
#        if strx[0] == '-':
#            sign = -1
#            strx = strx[1:]
#        else:
#            sign = 1
#            
#        for i in range(len(strx)):
#            restrx = restrx + strx[len(strx) - i - 1]
#        
#        return int(restrx) * sign

# Note: 32-bit ineger range control
                   
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        if x<0:
            str_x = '-'+str_x[::-1][:-1]
            x = int(str_x)
        else:
            str_x = str_x[::-1]
            x = int(str_x)
        neg_limit= -0x80000000
        pos_limit= 0x7fffffff

        if(x<0):
            val=x&neg_limit
            if(val==neg_limit):
                return x
            else:
                return 0
        elif(x==0):
            return x
        else:
            val = x&pos_limit
            if(val==x):
                return x
            else:
                return 0