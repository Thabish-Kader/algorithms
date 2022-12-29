
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
        y=str(x)[::-1]
        if y == str(x): return True
        else: return False
    isPalindrome(-121)

class Solution10:
    # def isMatch(s,p):
    #     string = list(s)
    #     pattern = list(p)
    #     new_Stirng= []
    #     # check if patter is *
    #     if("*" in pattern):
    #         index = pattern.index("*") - 1
    #         # print (string[index])
    #         for string[index] in string:
    #             new_Stirng.append(string[index])
    #             return True
    #         print(new_Stirng)
    #     elif("." in pattern):
    #         index = pattern.index(".") -1
    #         print (string[index])
    #         for string[index] in string:
    #             new_Stirng.append(string[index])
    #             return True

    #     else:
    #         return False
        # Then fo the logic

        # check if patter is .
        # compute logic
    # isMatch("aa",".a")
    def isMatch(self,text,pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], "."}


        if len(pattern) >= 2 and pattern[1] == "*":
            return(self.isMatch(text,pattern[2:]) or
             first_match and self.isMatch(text[1:],pattern))
        
        else:
            return first_match and self.isMatch(text[1:],pattern[1:])

    
# sol = Solution10()
# print(sol.isMatch("aa",".*"))

class Solution11:
    # def maxArea(h):
        # maxArea = 0
        # for left in range(len(h)):
        #     for right in range(left + 1,len(h)):
        #         width = right - left
        #         maxArea = max(maxArea, min(h[left], h[right])*width)
        # print(maxArea)
        def maxArea(h):
            maxarea = 0
            left = 0
            right = len(h) - 1
            while left < right:
                width = right - left
                maxarea = max(maxarea, min(h[left], h[right] )* width)


                if h[left] <= h[right]:
                    left +=1
                else:
                    right -=1

        maxArea([1,8,6,2,5,4,8,3,7])

class Solution12:
    def intToRoman(self, num:int):
        place = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym=["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        symbol = ""
        i =12

        while num :
            div = num // place[i]
            num %= place[i]
            print(div)

            while div:
                symbol += sym[i]
                div -=1
            i-=1
        return symbol  


sol = Solution12()
# print(sol.intToRoman(1994))

class Solution13:
    def romanToInt(self, s:str) : 
        charToNum = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        curr = 0
        prev = 0
        total = 0
        for i in s[::-1]:
            curr = charToNum[i]
            total +=curr if curr>prev else -1*curr
            prev = curr

class Solution14:
    def longestCommonPrefix(self, strs: List[str]):

    #     if not strs:
    #         return ""
    #     count=0
    #     for letter_group in zip(*strs):
    #         print(letter_group)
    #         if(len(set(letter_group))>1):
    #             break
    #         count = count + 1

    #     return(strs[0][0:count])
        if not strs:
            return ""
        
        letters = ""
        for letter in zip(*strs):
            if (len(set(letter)) == 1):
                letters += letter[0]

            else: break
        print(letters)
                

                

        # compare the letters in sts

sol14 = Solution14()
sol14.longestCommonPrefix(["flower","flow","flight"])





