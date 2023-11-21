# QUESTIONS
# Can we be passed empty string?
# Account for malformed roman numerals? (Spaces, special characters, bad formatting)
# Are we checking for invalid?

# Naive first impression solution
# Basic logic of the solution is to count the value of each character
# The challenge comes with the C, X and I characters since they 
# change values depending on the proceeding character

# TODO - Refactor naive solution by identifying the add/subtract patterns
#        likely using a hashmap

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0

        # Iterate through each char in roman numeral string (array)
        # for i, char in enumerate(s):
        while i < len(s):
            print(s[i])
            # IF char = M add 1000
            if s[i] == 'M':
                result += 1000
            # IF char = D add 500
            if s[i] == 'D':
                result += 500
            # IF char = C add 100
            if s[i] == 'C':
                # AND precedes D add 400
                if i + 1 < len(s) and s[i + 1] == 'D':
                    result += 400
                    i += 1
                # AND precedes M add 900
                elif i + 1 < len(s) and s[i + 1] == 'M':
                    result += 900
                    i += 1
                # ELSE add 100
                else:
                    result += 100
            # IF char = L add 50
            if s[i] == 'L':
                result += 50
            # IF char = X 
            if s[i] == 'X':
                # AND precedes L add 40
                if i + 1 < len(s) and s[i + 1] == 'L':
                    result += 40
                    i += 1
                # AND precedes C add 90
                elif i + 1 < len(s) and s[i + 1] == 'C':
                    result += 90
                    i += 1
                # ELSE add 10
                else:
                    result += 10
            # IF char = V add 5
            if s[i] == 'V':
                result += 5
            # IF char = I
            if s[i] == 'I':
                # AND precedes V add 4
                if i + 1 < len(s) and s[i + 1] == 'V':
                    result += 4
                    i += 1
                # AND precedes X add 9
                elif i + 1 < len(s) and s[i + 1] == 'X':
                    result += 9
                    i += 1
                # ELSE add 1
                else:
                    result += 1
            i += 1
            

        return result