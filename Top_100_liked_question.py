from typing import List, ListNode,Optional

class Solution:
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

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_reverse= l1[::-1]
        l2_reverse= l2[::-1]


        s=[str(i) for i in l1_reverse]
        s2 = [str(i) for i in l2_reverse]
    
        # Join list items using join()
        res = int("".join(s))
        res2 = int("".join(s2))

        target = res + res2
    
    l1= [1,2,3]
    l2=[2,3,4]
    print(addTwoNumbers(l1,l2))
