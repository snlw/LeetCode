# https://leetcode.com/problems/valid-phone-numbers/submissions/1300950481/

# ^ : Start of string or line
# $ : End of string

grep -E "^[0-9]{3}-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$" file.txt
