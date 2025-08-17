class Solution:
    def romanToInt(self, s: str) -> int:
        model = {
            "I": "1",
            "V": "5",
            "X": "10",
            "L": "50",
            "C": "100",
            "D": "500",
            "M": "1000"
        }
        sum = 0

        for data in s:
            value = model.get(data)
            sum += int(value)

        print(sum)

solution = Solution()
solution.romanToInt()


# def roman_to_integer(number):
#     model = {
#         "I": "1",
#         "V": "5",
#         "X": "10",
#         "L": "50",
#         "C": "100",
#         "D": "500",
#         "M": "1000"
#     }
#     sum = 0

#     for data in number:
#         value = model.get(data)
#         sum += int(value)

#     print(sum)


# s = input()
# roman_to_integer(s)