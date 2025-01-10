class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands = ["", "M", "MM", "MMM"]

        i1 = num % 10
        i10 = num % 100 // 10
        i100 = num % 1000 // 100
        i1000 = num % 10000 // 1000

        return f"{thousands[i1000]}{hundreds[i100]}{tens[i10]}{ones[i1]}"
