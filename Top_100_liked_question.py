
import math
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
        # return print(res)
    lengthOfLongestSubstring("abbbsssbbbd")

class Solution4:
    def findMedianSortedArrays( nums1, nums2):
        # merge two list
        num3=nums1 + nums2
        num3.sort()
        # find the length of list

        # if even add middle numbers and divide by 2
        if(len(num3) % 2 == 0):

            middle = (len(num3) / 2)
            median = (num3[int(middle - 1)]+num3[int(middle)])/2
            return median
        # if odd divide by 2
        else:
            middle = math.floor((len(num3) / 2))
            return num3[middle]

        # return number
    l=[1,3]
    l2=[2]
    findMedianSortedArrays(l,l2)

class Solution5:
    def longestPalindrome(s):
        # read the string
        mylist = list(s)

        # reverse the string
        reverseList = mylist[::-1]

        # loop through the list
        result = []
        for i in range(len(mylist)):
            if(mylist[i] == reverseList[i]):
                result.append(mylist[i])
        return ("".join(result))
    longestPalindrome("babad")

class Solution6:
    # did not solve this
    def convert(s : str, numRows: int) :
        if numRows == 1:
            return s 
        
        n = len(s)
        section = math.ceil(n/(2*numRows - 2.0))
        num_cols = section * (numRows - 1)

        matrix = [[" "] * num_cols for _ in range(numRows)]

        curr_row, curr_col = 0,0
        curr_string_index = 0

        # iterate in zig-zag pattern on matrix and fill it with string characters
        while curr_string_index < n :
            # move down
            while curr_row < numRows and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row += 1
                curr_string_index += 1

            curr_row -= 2
            curr_col += 1

            # Move up (with moving right also).
            while curr_row > 0 and curr_col < num_cols and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row -= 1
                curr_col += 1
                curr_string_index += 1
        
        answer = ""
        for row in matrix:
            answer += "".join(row)
            
        return answer.replace(" ", "")

class Solution7:
    def reverse(x):
        l = list(str(x))
        if(l[0] == "-"):
            l.pop(0)
            reverse=l[::-1]
            new_int = int("".join(reverse))

            return -new_int
            


        reverse = l[::-1]
        new_int = int(''.join(reverse))
        return new_int
    
    reverse(-123)

class Solution8:
    def myAtoi(s):
        # read the string
        l = list(s)
        neg=[]
        # check wether there is - or +
        if "-" in l:
            l.remove("-")
            numList = [ str (x) for x in l if x.isdigit() ]
            result = int("".join(numList))

        # return -result
            return -result
        # extarpulate the number
        numList = [ str (x) for x in l if x.isdigit() ]
        result = int("".join(numList))
        return result

        # return the number
    myAtoi("-4193 with words")

class Solution9:
    def isPalindrome(x:int):
        if(x < 0): return False

        l=list(str (x))
        reverse = l[::-1]

        num=int("".join(l))
        num2=int("".join(reverse))

        if(num == num2):
            print( True)
        else:
            print(False)

    isPalindrome(121)





