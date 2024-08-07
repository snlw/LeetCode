"""
https://leetcode.com/problems/integer-to-english-words/submissions/1347431406/?envType=daily-question&envId=2024-08-07

TC: O(log10 N)
SC: O(1)
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        lookup = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            }
        
        digits = {
            1000000000: "Billion",
            1000000: "Million",
            1000: "Thousand",
            1: ""
        }

        def convert(s):
            result = []
            if s >= 100:
                result.append(lookup[s // 100])
                result.append("Hundred")
                s = s % 100
            
            if s >= 20:
                result.append(lookup[s // 10 * 10])
                s = s % 10
            
            if s > 0:
                result.append(lookup[s])
                
            return " ".join(result)

        ans = []
        for val, label in digits.items():
            curr = num // val
            num = num % val
            if curr:
                ans.append(convert(curr))
                if label:
                    ans.append(label)

        return " ".join(ans)


