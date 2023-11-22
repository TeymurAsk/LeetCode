class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        dct = {1000:"M", 900: "CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40: "XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        while num !=0:
            for key in dct.keys():
                if num - key >= 0:
                    num -= key
                    result += dct[key]
                    break
        return result