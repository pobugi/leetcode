class Solution:
    def reverseVowels(self, s: str) -> str:
        output = []
        vowels = []

        for letter in s:
            if self.is_vowel(letter):
                output.append("_")  # store the gaps for vowels
                vowels.append(letter)
            else:
                output.append(letter)

        # insert vowels back into the output
        for i in range(len(output)):
            if output[i] == "_":
                output[i] = vowels.pop()

        return "".join(output)

    def is_vowel(self, letter: str) -> bool:
        return letter.lower() in ["a", "e", "i", "o", "u"]
