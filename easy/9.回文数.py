class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_str_reverse = x_str[::-1]
        return x_str == x_str_reverse

if __name__ == "__main__":
    x_list = [121, -121, 10]
    for x in x_list:
        print(Solution().isPalindrome(x))
        