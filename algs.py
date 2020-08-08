from typing import List, Dict, Tuple, Sequence

# 在for i in range(x)中，想要skip一个i，改成用while,然后 if i == skip-1, i+=2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution:
    ##################################################################################
    # brute force O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]

    # one pass
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in seen:
                seen[num] = i
            else:
                return [seen[diff], i]

##################################################################################
    # reverse a int, if int overflow, return 0. return sign correctly.
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31:
            return 0
        else:
            strg = str(x)
            if x >= 0:
                revst = strg[::-1]
            else:
                temp = strg[1:]
                temp2 = temp[::-1]
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31:
                return 0
            else:
                return int(revst)

##################################################################################
    def isPalindrome(self, x: int) -> bool:
            if x < 0:
                return False
            else:
                s = str(x)
                for i in range(int(len(s)/2)):
                    if s[i] != s[len(s)-1-i]:
                        return False
                return True

##################################################################################
    # brute force
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if s[i] == "I":
                if i + 1 < len(s) and s[i + 1] == "V":
                    total += 4
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == "X":
                    total += 9
                    i += 2
                else:
                    total += 1
                    i += 1
            elif s[i] == "X":
                if i + 1 < len(s) and s[i + 1] == "L":
                    total += 40
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == "C":
                    total += 90
                    i += 2
                else:
                    total += 10
                    i += 1
            elif s[i] == "C":
                if i + 1 < len(s) and s[i + 1] == "D":
                    total += 400
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == "M":
                    total += 900
                    i += 2
                else:
                    total += 100
                    i += 1
            elif s[i] == "V":
                total += 5
                i += 1
            elif s[i] == "L":
                total += 50
                i += 1
            elif s[i] == "D":
                total += 500
                i += 1
            elif s[i] == "M":
                total += 1000
                i += 1
        return total

    #smart:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]

##################################################################################
    # Find longest common prefix

    def longestCommonPrefix(self, strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            if not strs:
                return ""
            shortest = min(strs,key=len)
            for i, ch in enumerate(shortest):
                for other in strs:
                    if other[i] != ch:
                        return shortest[:i]
            return shortest

###############################################################################
    # Find if a string contain valid brackets:

    def isValid(self, s: str) -> bool:

        bracket_map = {"(": ")", "[": "]", "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []

############################################################################
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newnode = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return newnode.next


############################################################################

    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        i = 0
        while i < len(nums):
            if nums[i] in seen:
                nums[:] = nums[:i] + nums[i + 1:]
            else:
                seen[nums[i]] = True
                i += 1
        return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[x] = nums[i + 1]
                x += 1
        return (x)

############################################################################

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[:] = nums[:i] + nums[i + 1:]
            else:
                i += 1
        return len(nums)

############################################################################
    #Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)


############################################################################

    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for i, num in enumerate(nums):
            if num == target:
                return i
            elif target > num:
                index = i + 1
        return index

###########################################################################

    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        s = self.countAndSay(n - 1)
        i, ch, tmp = 0, s[0], ''
        for j in range(1, len(s)):
            if s[j] != ch:
                tmp += str(j - i) + ch
                i, ch = j, s[j]
        tmp += str(len(s) - i) + ch
        return tmp

        # 2
        # """
        # :type n: int
        # :rtype: str
        # """
        # s = '1'
        # for i in range(n-1):
        #     count = 1
        #     temp = []
        #     for index in range(1, len(s)):
        #         if s[index] == s[index-1]:
        #             count += 1
        #         else:
        #             temp.append(str(count))
        #             temp.append(s[index-1])
        #             count = 1
        #     temp.append(str(count))
        #     temp.append(s[-1])
        #     s = ''.join(temp)
        # return s

        # 3
        # result = '1'
        # for _ in range(n-1):
        #     prev = result
        #     result = ''
        #     j = 0
        #     while j < len(prev):
        #         cur = prev[j]
        #         cnt = 1
        #         j += 1
        #         while j < len(prev) and prev[j] == cur:
        #             cnt += 1
        #             j += 1
        #         result += str(cnt) + str(cur)
        # return result



    #####################################################

    def maxSubArray(self, nums: List[int]) -> int:
        # for i in range(1, len(nums)):
        #     if nums[i - 1] > 0:
        #         nums[i] += nums[i - 1]
        # return max(nums)

        """
        :type nums: List[int]
        :rtype: int
        """

        def divide_and_conquer(nums, i, j):
            if i == j - 1:
                return nums[i], nums[i], nums[i], nums[i]

            # we will compute :
            # a which is max contiguous sum in nums[i:j] including the first value
            # m which is max contiguous sum in nums[i:j] anywhere
            # b which is max contiguous sum in nums[i:j] including the last value
            # s which is the sum of all values in nums[i:j]

            # compute middle index to divide array in two halves
            i_mid = i + (j - i) // 2

            # compute a, m, b, s for left half
            a1, m1, b1, s1 = divide_and_conquer(nums, i, i_mid)

            # compute a, m, b, s for right half
            a2, m2, b2, s2 = divide_and_conquer(nums, i_mid, j)

            # combine a, m, b, s values from left and right halves to form a, m, b, s for whole array (bottom up)
            a = max(a1, s1 + a2)
            b = max(b2, s2 + b1)
            m = max(m1, m2, b1 + a2)
            s = s1 + s2
            return a, m, b, s

        _, m, _, _ = divide_and_conquer(nums, 0, len(nums))
        return m

    ####################################################################################################
    #Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
    # return the length of last word (last word means the last appearing word if we loop from left to right)
    # in the string.
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


    ####################################################################################################
    # Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Input: [1,2,3]
        Output: [1,2,4]
        Explanation: The array represents the integer 123.
        """
        s = ""
        for i in digits:
            s += str(i)
        s = int(s) + 1
        result = [int(x) for x in str(s)]
        return result

    ####################################################################################################
    # simple way
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        r = bin(a + b)
        return r[2:]

    #normay way:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry % 2)
            carry //= 2

        return result[::-1]


    ###################################################################################
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x

        while lo <= hi:
            mid = (lo + hi) // 2

            if mid * mid > x:
                hi = mid - 1
            elif mid * mid < x:
                lo = mid + 1
            else:
                return mid

        # When there is no perfect square, hi is the the value on the left
        # of where it would have been (rounding down). If we were rounding up,
        # we would return lo
        return hi


    #######################################################################################
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        cur1 = l1
        cur2 = l2
        newList = l1
        newNode1 = l1
        while cur1 and cur2:
            cur1.val = cur1.val + cur2.val + carry
            if cur1.val >= 10:
                cur1.val = cur1.val - 10
                carry = 1
            else:
                carry = 0
            newNode1 = cur1
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            cur1.val = cur1.val + carry
            if cur1.val >= 10:
                cur1.val = cur1.val - 10
                carry = 1
            else:
                carry = 0
            newNode1 = cur1
            cur1 = cur1.next
        if cur2:
            newNode1.next = cur2
            while cur2:
                cur2.val = cur2.val + carry
                if cur2.val >= 10:
                    cur2.val = cur2.val - 10
                    carry = 1
                else:
                    carry = 0
                newNode1 = cur2
                cur2 = cur2.next
        if carry:
            newNode = ListNode(1)
            newNode1.next = newNode
        return newList

    def addTwoNumbers(self, l1, l2):
        carry = 0
        res = n = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val)
        return res.next

    #########################################################################
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i
        return max_length

    #########################################################################
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)
        return res
    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

##################################################################################
    # brute force
    # def maxArea(self, height: List[int]) -> int:
    #     max_area = 0
    #     for i, num in enumerate(height):
    #         for j, n in enumerate(height[i+1:]):
    #             if n < num:
    #                 area = n * (j+1)
    #             else:
    #                 area = num * (j+1)
    #             max_area = max(max_area, area)
    #     return max_area
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        MAX = 0 
        x = len(height) - 1
        y = 0
        while x != y:
            if height[x] > height[y]:
                area = height[y] * (x - y)
                y += 1
            else:
                area = height[x] * (x - y)
                x -= 1
            MAX = max(MAX, area)
        return MAX

####################################################################
    # ! Find number of 1 bits in a number
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n != 0:
            n = n & n-1
            counter += 1
        return counter
