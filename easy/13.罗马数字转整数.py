class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900,
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }

        num = 0
        i = 0

        while True:
            if i >= len(s):
                break

            if s[i:i+2] in roman_dict:
                num += roman_dict[s[i:i+2]]
                i += 2
            else:
                num += roman_dict[s[i]]
                i += 1
        
        return num

if __name__ == "__main__":
    s_list = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    for s in s_list:
        print(Solution().romanToInt(s))