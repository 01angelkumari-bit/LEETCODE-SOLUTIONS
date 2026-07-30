class Solution:
    def calculate(self, s: str) -> int:

        stack = []         
        result = 0
        number = 0
        sign = 1

        for ch in s:

            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == '+':
                result += sign * number
                number = 0
                sign = 1

            elif ch == '-':
                result += sign * number
                number = 0
                sign = -1

            elif ch == '(':
                stack.append((result, sign))# Save current result as well as sign
                result = 0
                sign = 1

            elif ch == ')':
                result += sign * number        # Finish current number
                number = 0

                prev_result, prev_sign = stack.pop()

                result = prev_result + prev_sign * result

        # Add the last number (if expression doesn't end with ')')
        result += sign * number

        return result