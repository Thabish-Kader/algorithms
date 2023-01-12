
from itertools import product
import math
from typing import List, Optional

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i] + nums[j] == target):
        #             return [i,j]
        seen = {} 
        for i,value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [i,seen[remaining]]
            else:
                seen[value] = i


        

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

class TwoSum(): # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        seen = {}
        for i,value in enumerate(numbers):
            remaining = target - numbers[i]

            if remaining in seen:
                return [seen[remaining]+1, i+1]
            else :
                 seen[value] = i
sol = TwoSum()
sol.twoSum([2,7,11,15],9)
        # compare the letters in sts
class Solution15:  
    def threeSum(self, nums: List[int]):

        # nums.sort()
        # res = []

        # for i in range(len(nums) -2): #1

        #     if i > 0 and nums[i] == nums[i-1]: #2
        #         continue
        #     left = i + 1 #3
        #     right = len(nums) - 1 #4
            
        #     while left < right:  
        #         temp = nums[i] + nums[left] + nums[right]
                                    
        #         if temp > 0:
        #             right -= 1
                    
        #         elif temp < 0:
        #             left += 1
                
        #         else:
        #             res.append([nums[i], nums[left], nums[right]]) #5
        #             while left < right and nums[left] == nums[left + 1]: #6
        #                 left += 1
        #             while left < right and nums[right] == nums[right-1]:#7
        #                 right -= 1    #8
                
        #             right -= 1 #9 
        #             left += 1 #10
        nums.sort()
        res = []

        for i in range(len(nums) -2):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            left = i +1
            right = len(nums)-1

            while left < right:
                temp = nums[i] + nums[left] + nums[right]

                if temp > 0:
                    right -=1
                elif temp < 0:
                    left +=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    right -=1
                    left +=1
                    


sol15 = Solution15()

sol15.threeSum([-1,0,1,2,-1,-4])

class Solution16:
    # TODO: redo
    def threeSumCloset(self, nums:List[int], target):
        n = len(nums)
        if n == 0:
            return 0
        if n < 3:
            return sum(nums)
        nums_up = sorted(nums)
        res = sum(nums_up[0:3]) # initialze the result 
        i, lo, hi = 0, 0, 0
        for i in range(n):            
            diff_tar = target - nums_up[i]  # difference to target
            lo, hi = i+1, n-1   # two pointers
            # two-pointer search
            while lo < hi:
                sum_two = nums_up[lo] + nums_up[hi] # current sum of the two
                if abs(nums_up[i]+sum_two-target) < abs(res-target):    # update result if current sum of the three is closer than current result
                    res = nums_up[i] + sum_two
                if sum_two == diff_tar: # sum of the three equals target
                    return target
                elif sum_two < diff_tar: # sum is smaller than target, we try bigger 'lo' to move closer to target. (not certainly closer, but possible) 
                    lo += 1
                else:   # sum is bigger than target, we try smaller 'hi' to move closer to target. (not certainly closer, but possible)
                    hi -= 1
        
        return res


# sol16 = Solution16()
# sol16.threeSumCloset([-1,2,1,-4],1)

class Solution17:
    def letterCombinations(self, digits: str):

        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv", "9":"wxyz"}

        res = []
        iterables = [dic[i] for i in digits ]
        # for x in product(*iterables):
        #     element = "".join(x)
        #     res.append(element)
        # print(res)
        res = ["".join(x) for x in product(*iterables)]
        print(res)

# sol17 = Solution17()
# sol17.letterCombinations("23")

class Solution18:
    # A very helpful guide for sum problems https://leetcode.com/problems/4sum/solutions/737096/sum-megapost-python3-solution-with-a-detailed-explanation/
    def fourSum(self, nums:List[int], target:int):
        # n = len(nums)
        # seen = set()
        # ans = set()
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             lastNumber = target - nums[i] - nums[j] - nums[k]
        #             if lastNumber in seen:
        #                 arr = sorted([nums[i], nums[j], nums[k], lastNumber])
        #                 ans.add((arr[0], arr[1], arr[2], arr[3]))
        #     seen.add(nums[i])
        # return(ans)

        n= len(nums)
        seen = set()
        ans= set()

        for i in range(n):
            for j in range (i+1,n):
                for k in range (j+1,n):
                    remaining = target - nums[i] - nums[j] - nums[k]
                    if remaining in seen:
                        arr = sorted([nums[i], nums[j], nums[k], remaining])
                        ans.add((arr[0], arr[1], arr[2], arr[3]))
            seen.add(nums[i])
        return ans

# sol18 = Solution18()
# print(sol18.fourSum([1,0,-1,0,-2,2],8))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution19: #https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#      def removeNthFromEnd(self, head, n: int):

class Solution20: #https://leetcode.com/problems/valid-parentheses/
    def isValid(self,s):
        ack = []
        lookfor = {')':'(', '}':'{', ']':'['}

        lookUp = {'(':')', '{':'}', '[':']'}
        print(lookfor.keys())
        # for char in s:
        #     if char in lookfor.values():
        #         ack.append(char)
        #     elif ack and lookfor[char] == ack[-1]:
        #         ack.pop()
        #     else:
        #         print(False)    
        # print( ack == [])
        for char in s:
            # print(lookfor[char])
            if char in lookUp.keys():
                ack.append(char)
            elif ack and lookfor[char] == ack[-1]:
                ack.pop()
            else:
                return False
        print( ack == [])


# sol20 = Solution20()
# sol20.isValid("{[[]]}")
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution21 :
    #TODO: redo
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) :
        newHead = dummyHead = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        return newHead.next


# sol21 = Solution21()
# print(sol21.mergeTwoLists([1,2,4],[1,3,4]))

class Solution22:
    def generateParenthesis(self,n:int):

        def backtrack(open,close,s):
            if len(s) == n*2:
                res.append(s)
                return
        
            if open < n : 
                backtrack(open+1,close,s+"(")

            if close < open : 
                backtrack(open,close + 1,s +")")

        res = []
        backtrack(0,0,"")
        print(res)
        
# sol22 = Solution22()
# sol22.generateParenthesis(3)

class Solution23:
    def mergeKLists(self, lists):
        head = temp = ListNode()
        arr = []

        for l in lists:
            while l !=None:
                arr.append(l.val)
                l = l.next

        for val in sorted(arr):
            temp.next = ListNode()
            temp= temp.next
            temp.val = val

        return head.next


sol23 = Solution23()
sol23.mergeKLists([[1,4,5],[1,3,4],[2,6]])