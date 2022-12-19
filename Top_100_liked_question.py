
from typing import List, Optional

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]

class Solution2:
    def addTwoNumbers( l1, l2):
        l1_reverse= l1[::-1]
        l2_reverse= l2[::-1]


        s=[str(i) for i in l1_reverse]
        s2=[str(i) for i in l2_reverse]
    
        # Join list items using join()
        res = int("".join(s))
        res2 = int("".join(s2))

        result = res + res2
        target = [int(x) for x in str(result)]
        desired_target = target[::-1]
        
        return desired_target
    
    l1= [2,4,3]
    l2=[5,6,4]
    # print(addTwoNumbers(l1,l2))

class Solution3:
    # def lengthOfLongestSubstring(s):
    #     # convert a sting to list
    #     list = [str (x) for x in s]
    #     list2=[]
    #     # check wether the letters exist new list
    #     for i,v in enumerate(list):
    #         try:
    #             if(list[i] and list[i+1] != v):
    #                 list2.append(v)
    #         except IndexError:
    #             pass

    #     # add letters to new list 
    #     print(len(list2))


    # lengthOfLongestSubstring("abcabcbb")

    def lengthOfLongestSubstring(s):
        def allUnique(start,end):
            chars = set()
            for i in range(start,end):
                c=s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True
        
        n=len(s)
        res=0
        for i in range(n):
            for j in range(i,n):
                if allUnique(i,j):
                    res = max(res,j-i+1)
        return print(res)


    
    lengthOfLongestSubstring("abbbsssbbbd")

        



