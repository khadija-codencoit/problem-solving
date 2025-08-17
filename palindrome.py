class Solution:
    def isPalindrome(self,x):
        if x < 0:
            return False
        str_x = str(x)
        return str_x == str_x[::-1]


solution = Solution()

print(solution.isPalindrome(121)) 



# value = input("Enter the value : ")

# reverse = value[::-1]

# if value == reverse:
#     print("Yes! this is palindrome")
# else:
#     print("This is not palindrome")