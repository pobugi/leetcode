"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.


Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""


def fizzbuzz(n):
    if (not n % 3) and (not n % 5):
        return "FizzBuzz"
    if not n % 3:
        return "Fizz"
    if not n % 5:
        return "Buzz"
    return str(n)


def solution(n):
    return [
        fizzbuzz(i) for i in range(1, n + 1)
    ]


print(solution(15))
