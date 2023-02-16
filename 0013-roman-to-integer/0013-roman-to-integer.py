class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev_value = 0
        total = 0
        for c in s:
            curr_value = roman_to_int_map[c]
            if curr_value > prev_value:
                total += curr_value - 2 * prev_value
            else:
                total += curr_value
            prev_value = curr_value
        return total
        