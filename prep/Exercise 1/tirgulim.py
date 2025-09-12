# def add_2_target(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i, j]
#     return []
# dd=[1, 2, 3, 4, 5, 6]
#
# print(add_2_target(dd, 9))
#
# def longest_sub_string(str):
#     my_set = set()
#     for s in str:
#         my_set.add(s)
#     return len(my_set)
#
# print(longest_sub_string("abcd"))
#
# def anagram_of_letters(s,t):
#     return sorted(s)==sorted(t)
# ff = anagram_of_letters("solomon", "nomolos")
# print(f"are they sorted?  {ff}")
#RECURSIVE APPROACH
# def fib(n):
#     if n<=2:
#         result= 1
#     else: result = fib(n-1)+fib(n-2)
#     return result
# def fib_Bottom_up(n):
#     memo={}
#     for i in range(1, n+1):
#         if i<=2:
#             result = 1
#         else:
#             result = memo[i-1] + memo[i-2]
#         memo[i]=result
#     return memo[n]
# print(fib_Bottom_up(10))
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         # s = "III"
#         # s = "MCMXCIV"
#         romani={
#             'I' : 1,
#             'V' : 5,
#             'X' : 10,
#             'L' : 50,
#             'C' : 100,
#             'D' : 500,
#             'M' : 1000
#         }
#         sum=0
#         for i in s:
#             if romani[i] < romani[i]:
#                 sum +=romani[i+1]-romani[i]
#             sum += romani[i]
#         return sum
dp = [[0] * (5) for _ in range(4)]
print(dp)