# 242. Valid Anagram 
# Example 1: 
# Input: s = "racecar", t = "carrace"
# Output: true
# Example 2: 
# Input: s = "jar", t = "jam"
# Output: false

def isAnagram(s, t) -> bool:
    # S and T; Key is the char and Value is how many times that letter shows up
    # We will compare if S and T are the same
    if len(s) != len(t):
        return False
    countS = {}
    countT = {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
        
# 1. Two Sum
# Example 1:
# Input: nums = [3, 4, 5, 6], target 7
# Output: [0,1]

def twoSum(nums, target) -> list[int]:
    # Key = Value, Value = Index
    map = {}
    for i, x in enumerate(nums):
        diff = target - x 
        if diff in map:
            return [map[diff], i]
        map[x] = i

def duplicates(nums):
    # Set to determine if the number is already in the set
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

# 125. Valid Palindrome 
# Example 1: 
# Input: s = "Was it a car or a cat I saw?"
# Output: True
def validPalindrome(s) -> bool:


