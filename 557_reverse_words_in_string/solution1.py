# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"


def reverse_words(words):
    result = ""

    left = 0
    right = 0
    while right < len(words):
        while right < len(words) and words[right] != " ":
            right += 1
        slice = words[left:right]
        result += slice[::-1] + " "

        while right < len(words) and words[right] == " ":
            right += 1
        left = right

    return result


print(reverse_words("abc def"))
# print(reverse_words("Let's take LeetCode contest"))
