from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_dict = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
        }

        result = []
        pre_strs = []
        is_first = True

        for s in digits[::-1]:
            result = []
            chars = char_dict[s]
            
            if is_first:
                is_first = False
                for char in chars:
                    result.append(char)
            else:
                for pre_str in pre_strs:
                    for char in chars:
                        result.append(char+pre_str)
            pre_strs = result
        
        return result


if __name__ == "__main__":
    digits_list = ["23", "2"]

    for digits in digits_list:
        print(Solution().letterCombinations(digits))