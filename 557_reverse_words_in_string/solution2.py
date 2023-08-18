# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"


def reverse_words(words):

    words_arr = words.split()

    for i in range(len(words_arr)):
        words_arr[i] = words_arr[i][::-1]

    result = " ".join(words_arr)

    return result


print(reverse_words("abc def"))
print(reverse_words("Let's take LeetCode contest"))
