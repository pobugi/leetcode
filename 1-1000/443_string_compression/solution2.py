class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        while i < len(chars):
            curr = chars[i]
            count = 0
            while i < len(chars) and chars[i] == curr:
                count += 1
                chars.pop(i)
            if count > 1:
                chars.insert(i, curr)
                i += 1
                for char in str(count):
                    chars.insert(i, char)
                    i += 1
            else:
                chars.insert(i, curr)
                i += 1
        print(chars)
        return len(chars)


chars = ["a", "a", "b", "b", "c", "c", "c", "d"]  # "a2b2c3
s = Solution()
print(s.compress(chars))
